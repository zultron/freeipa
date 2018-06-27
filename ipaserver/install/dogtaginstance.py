# Authors: Ade Lee <alee@redhat.com>
#
# Copyright (C) 2014  Red Hat
# see file 'COPYING' for use and warranty information
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import base64
import logging

import ldap
import os
import shutil
import traceback
import dbus

from pki.client import PKIConnection
import pki.system

from ipalib import api, errors, x509
from ipalib.install import certmonger
from ipalib.constants import CA_DBUS_TIMEOUT
from ipaplatform import services
from ipaplatform.constants import constants
from ipaplatform.paths import paths
from ipapython import ipaldap
from ipapython import ipautil
from ipapython.dn import DN
from ipaserver.install import service
from ipaserver.install import installutils
from ipaserver.install import replication
from ipaserver.install.installutils import stopped_service

logger = logging.getLogger(__name__)


def get_security_domain():
    """
    Get the security domain from the REST interface on the local Dogtag CA
    This function will succeed if the local dogtag CA is up.
    """
    connection = PKIConnection(
        protocol='https',
        hostname=api.env.ca_host,
        port='8443'
    )
    domain_client = pki.system.SecurityDomainClient(connection)
    info = domain_client.get_security_domain_info()
    return info


def is_installing_replica(sys_type):
    """
    We expect only one of each type of Dogtag subsystem in an IPA deployment.
    That means that if a subsystem of the specified type has already been
    deployed - and therefore appears in the security domain - then we must be
    installing a replica.
    """
    info = get_security_domain()
    try:
        sys_list = info.systems[sys_type]
        return len(sys_list.hosts) > 0
    except KeyError:
        return False


class DogtagInstance(service.Service):
    """
    This is the base class for a Dogtag 10+ instance, which uses a
    shared tomcat instance and DS to host the relevant subsystems.

    It contains functions that will be common to installations of the
    CA, KRA, and eventually TKS and TPS.
    """

    tracking_reqs = None
    server_cert_name = None

    def __init__(self, realm, subsystem, service_desc, host_name=None,
                 nss_db=paths.PKI_TOMCAT_ALIAS_DIR, service_prefix=None):
        """Initializer"""

        super(DogtagInstance, self).__init__(
            'pki-tomcatd',
            service_desc=service_desc,
            realm_name=realm,
            service_user=constants.PKI_USER,
            service_prefix=service_prefix
        )

        self.admin_password = None
        self.fqdn = host_name
        self.pkcs12_info = None
        self.clone = False

        self.basedn = DN(('o', 'ipa%s' % subsystem.lower()))
        self.admin_user = "admin"
        self.admin_dn = DN(('uid', self.admin_user),
                           ('ou', 'people'), ('o', 'ipaca'))
        self.admin_groups = None
        self.tmp_agent_db = None
        self.subsystem = subsystem
        self.security_domain_name = "IPA"
        # replication parameters
        self.master_host = None
        self.master_replication_port = None
        self.subject_base = None
        self.nss_db = nss_db

    def is_installed(self):
        """
        Determine if subsystem instance has been installed.

        Returns True/False
        """
        return os.path.exists(os.path.join(
            paths.VAR_LIB_PKI_TOMCAT_DIR, self.subsystem.lower()))

    def spawn_instance(self, cfg_file, nolog_list=()):
        """
        Create and configure a new Dogtag instance using pkispawn.
        Passes in a configuration file with IPA-specific
        parameters.
        """
        subsystem = self.subsystem
        args = [paths.PKISPAWN,
                "-s", subsystem,
                "-f", cfg_file]

        with open(cfg_file) as f:
            logger.debug(
                'Contents of pkispawn configuration file (%s):\n%s',
                cfg_file, ipautil.nolog_replace(f.read(), nolog_list))

        try:
            ipautil.run(args, nolog=nolog_list)
        except ipautil.CalledProcessError as e:
            self.handle_setup_error(e)

    def clean_pkispawn_files(self):
        if self.tmp_agent_db is not None:
            shutil.rmtree(self.tmp_agent_db, ignore_errors=True)

        shutil.rmtree('/root/.dogtag/pki-tomcat/{subsystem}/'
                      .format(subsystem=self.subsystem.lower()),
                      ignore_errors=True)

    def restart_instance(self):
        self.restart('pki-tomcat')

    def start_instance(self):
        self.start('pki-tomcat')

    def stop_instance(self):
        try:
            self.stop('pki-tomcat')
        except Exception:
            logger.debug("%s", traceback.format_exc())
            logger.critical(
                "Failed to stop the Dogtag instance."
                "See the installation log for details.")

    def enable_client_auth_to_db(self, config):
        """
        Enable client auth connection to the internal db.
        Path to CS.cfg config file passed in.
        """

        with stopped_service('pki-tomcatd', 'pki-tomcat'):
            installutils.set_directive(
                config,
                'authz.instance.DirAclAuthz.ldap.ldapauth.authtype',
                'SslClientAuth', quotes=False, separator='=')
            installutils.set_directive(
                config,
                'authz.instance.DirAclAuthz.ldap.ldapauth.clientCertNickname',
                'subsystemCert cert-pki-ca', quotes=False, separator='=')
            installutils.set_directive(
                config,
                'authz.instance.DirAclAuthz.ldap.ldapconn.port', '636',
                quotes=False, separator='=')
            installutils.set_directive(
                config,
                'authz.instance.DirAclAuthz.ldap.ldapconn.secureConn',
                'true', quotes=False, separator='=')

            installutils.set_directive(
                config,
                'internaldb.ldapauth.authtype',
                'SslClientAuth', quotes=False, separator='=')

            installutils.set_directive(
                config,
                'internaldb.ldapauth.clientCertNickname',
                'subsystemCert cert-pki-ca', quotes=False, separator='=')
            installutils.set_directive(
                config,
                'internaldb.ldapconn.port', '636', quotes=False, separator='=')
            installutils.set_directive(
                config,
                'internaldb.ldapconn.secureConn', 'true', quotes=False,
                separator='=')
            # Remove internaldb password as is not needed anymore
            installutils.set_directive(paths.PKI_TOMCAT_PASSWORD_CONF,
                                       'internaldb', None)

    def uninstall(self):
        if self.is_installed():
            self.print_msg("Unconfiguring %s" % self.subsystem)

        try:
            ipautil.run([paths.PKIDESTROY,
                         "-i", 'pki-tomcat',
                         "-s", self.subsystem])
        except ipautil.CalledProcessError as e:
            logger.critical("failed to uninstall %s instance %s",
                            self.subsystem, e)

    def http_proxy(self):
        """ Update the http proxy file  """
        template_filename = (
            os.path.join(paths.USR_SHARE_IPA_DIR, "ipa-pki-proxy.conf"))
        sub_dict = dict(
            DOGTAG_PORT=8009,
            CLONE='' if self.clone else '#',
            FQDN=self.fqdn,
        )
        template = ipautil.template_file(template_filename, sub_dict)
        with open(paths.HTTPD_IPA_PKI_PROXY_CONF, "w") as fd:
            fd.write(template)

    def configure_certmonger_renewal(self):
        """
        Create a new CA type for certmonger that will retrieve updated
        certificates from the dogtag master server.
        """
        cmonger = services.knownservices.certmonger
        cmonger.enable()
        services.knownservices.messagebus.start()
        cmonger.start()

        bus = dbus.SystemBus()
        obj = bus.get_object('org.fedorahosted.certmonger',
                             '/org/fedorahosted/certmonger')
        iface = dbus.Interface(obj, 'org.fedorahosted.certmonger')
        for suffix, args in [('', ''), ('-reuse', ' --reuse-existing')]:
            name = 'dogtag-ipa-ca-renew-agent' + suffix
            path = iface.find_ca_by_nickname(name)
            if not path:
                command = paths.DOGTAG_IPA_CA_RENEW_AGENT_SUBMIT + args
                iface.add_known_ca(
                    name,
                    command,
                    dbus.Array([], dbus.Signature('s')),
                     # Give dogtag extra time to generate cert
                    timeout=CA_DBUS_TIMEOUT)

    def __get_pin(self):
        try:
            return certmonger.get_pin('internal')
        except IOError as e:
            logger.debug(
                'Unable to determine PIN for the Dogtag instance: %s', e)
            raise RuntimeError(e)

    def configure_renewal(self):
        """ Configure certmonger to renew system certs """
        pin = self.__get_pin()

        for nickname in self.tracking_reqs:
            try:
                certmonger.start_tracking(
                    certpath=self.nss_db,
                    ca='dogtag-ipa-ca-renew-agent',
                    nickname=nickname,
                    pin=pin,
                    pre_command='stop_pkicad',
                    post_command='renew_ca_cert "%s"' % nickname,
                )
            except RuntimeError as e:
                logger.error(
                    "certmonger failed to start tracking certificate: %s", e)

    def track_servercert(self):
        """
        Specifically do not tell certmonger to restart the CA. This will be
        done by the renewal script, renew_ca_cert once all the subsystem
        certificates are renewed.
        """
        pin = self.__get_pin()
        try:
            certmonger.start_tracking(
                certpath=self.nss_db,
                ca='dogtag-ipa-ca-renew-agent',
                nickname=self.server_cert_name,
                pin=pin,
                pre_command='stop_pkicad',
                post_command='renew_ca_cert "%s"' % self.server_cert_name)
        except RuntimeError as e:
            logger.error(
                "certmonger failed to start tracking certificate: %s", e)

    def stop_tracking_certificates(self, stop_certmonger=True):
        """Stop tracking our certificates. Called on uninstall.
        """
        self.print_msg(
            "Configuring certmonger to stop tracking system certificates "
            "for %s" % self.subsystem)

        cmonger = services.knownservices.certmonger
        services.knownservices.messagebus.start()
        cmonger.start()

        nicknames = list(self.tracking_reqs)
        if self.server_cert_name is not None:
            nicknames.append(self.server_cert_name)

        for nickname in nicknames:
            try:
                certmonger.stop_tracking(
                    self.nss_db, nickname=nickname)
            except RuntimeError as e:
                logger.error(
                    "certmonger failed to stop tracking certificate: %s", e)

        if stop_certmonger:
            cmonger.stop()

    @staticmethod
    def update_cert_cs_cfg(directive, cert, cs_cfg):
        """
        When renewing a Dogtag subsystem certificate the configuration file
        needs to get the new certificate as well.

        ``directive`` is the directive to update in CS.cfg
        cert is IPACertificate.
        cs_cfg is the path to the CS.cfg file
        """

        with stopped_service('pki-tomcatd', 'pki-tomcat'):
            installutils.set_directive(
                cs_cfg,
                directive,
                # the cert must be only the base64 string without headers
                (base64.b64encode(cert.public_bytes(x509.Encoding.DER))
                 .decode('ascii')),
                quotes=False,
                separator='=')

    def get_admin_cert(self):
        """
        Get the certificate for the admin user by checking the ldap entry
        for the user.  There should be only one certificate per user.
        """
        logger.debug('Trying to find the certificate for the admin user')
        conn = None

        try:
            ldap_uri = ipaldap.get_ldap_uri(protocol='ldapi', realm=self.realm)
            conn = ipaldap.LDAPClient(ldap_uri)
            conn.external_bind()

            entry_attrs = conn.get_entry(self.admin_dn, ['usercertificate'])
            admin_cert = entry_attrs.get('usercertificate')[0]

            # TODO(edewata) Add check to warn if there is more than one cert.
        finally:
            if conn is not None:
                conn.unbind()

        return admin_cert

    def handle_setup_error(self, e):
        logger.critical("Failed to configure %s instance: %s",
                        self.subsystem, e)
        logger.critical("See the installation logs and the following "
                        "files/directories for more information:")
        logger.critical("  %s", paths.TOMCAT_TOPLEVEL_DIR)

        raise RuntimeError("%s configuration failed." % self.subsystem)

    def __add_admin_to_group(self, group):
        dn = DN(('cn', group), ('ou', 'groups'), ('o', 'ipaca'))
        entry = api.Backend.ldap2.get_entry(dn)
        members = entry.get('uniqueMember', [])
        members.append(self.admin_dn)
        mod = [(ldap.MOD_REPLACE, 'uniqueMember', members)]
        try:
            api.Backend.ldap2.modify_s(dn, mod)
        except ldap.TYPE_OR_VALUE_EXISTS:
            # already there
            pass

    def setup_admin(self):
        self.admin_user = "admin-%s" % self.fqdn
        self.admin_password = ipautil.ipa_generate_password()
        self.admin_dn = DN(('uid', self.admin_user),
                           ('ou', 'people'), ('o', 'ipaca'))

        # remove user if left-over exists
        try:
            entry = api.Backend.ldap2.delete_entry(self.admin_dn)
        except errors.NotFound:
            pass

        # add user
        entry = api.Backend.ldap2.make_entry(
            self.admin_dn,
            objectclass=["top", "person", "organizationalPerson",
                         "inetOrgPerson", "cmsuser"],
            uid=[self.admin_user],
            cn=[self.admin_user],
            sn=[self.admin_user],
            usertype=['adminType'],
            mail=['root@localhost'],
            userPassword=[self.admin_password],
            userstate=['1']
        )
        api.Backend.ldap2.add_entry(entry)

        for group in self.admin_groups:
            self.__add_admin_to_group(group)

        # Now wait until the other server gets replicated this data
        ldap_uri = ipaldap.get_ldap_uri(self.master_host)
        master_conn = ipaldap.LDAPClient(ldap_uri)
        master_conn.gssapi_bind()
        replication.wait_for_entry(master_conn, entry.dn)
        del master_conn

    def __remove_admin_from_group(self, group):
        dn = DN(('cn', group), ('ou', 'groups'), ('o', 'ipaca'))
        mod = [(ldap.MOD_DELETE, 'uniqueMember', self.admin_dn)]
        try:
            api.Backend.ldap2.modify_s(dn, mod)
        except ldap.NO_SUCH_ATTRIBUTE:
            # already removed
            pass

    def teardown_admin(self):
        for group in self.admin_groups:
            self.__remove_admin_from_group(group)
        api.Backend.ldap2.delete_entry(self.admin_dn)

    def _use_ldaps_during_spawn(self, config, ds_cacert=paths.IPA_CA_CRT):
        config.set(self.subsystem, "pki_ds_ldaps_port", "636")
        config.set(self.subsystem, "pki_ds_secure_connection", "True")
        config.set(self.subsystem, "pki_ds_secure_connection_ca_pem_file",
                   ds_cacert)
