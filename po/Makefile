# Makefile for PO directory in any package using GNU gettext.
# Copyright (C) 1995-1997, 2000-2007, 2009-2010 by Ulrich Drepper <drepper@gnu.ai.mit.edu>
#
# This file can be copied and used freely without restrictions.  It can
# be used in projects which are not available under the GNU General Public
# License but which still want to provide support for the GNU gettext
# functionality.
# Please note that the actual code of GNU gettext is covered by the GNU
# General Public License and is *not* in the public domain.
#
# Origin: gettext-0.18.2
GETTEXT_MACRO_VERSION = 0.18

PACKAGE = freeipa
VERSION = 4.6.90.dev201806272043+gitfb34e05cd
PACKAGE_BUGREPORT = https://hosted.fedoraproject.org/projects/freeipa/newticket

SHELL = /bin/sh


srcdir = .
top_srcdir = ..


prefix = /usr
exec_prefix = /usr
datarootdir = ${prefix}/share
datadir = /usr/share
localedir = ${datarootdir}/locale
gettextsrcdir = $(datadir)/gettext/po

INSTALL = /usr/bin/install -c
INSTALL_DATA = ${INSTALL} -m 644

# We use $(mkdir_p).
# In automake <= 1.9.x, $(mkdir_p) is defined either as "mkdir -p --" or as
# "$(mkinstalldirs)" or as "$(install_sh) -d". For these automake versions,
# ${SHELL} /home/jman/git/freeipa-deps/freeipa/install-sh does not start with $(SHELL), so we add it.
# In automake >= 1.10, $(MKDIR_P) is derived from ${MKDIR_P}, which is defined
# either as "/path/to/mkdir -p" or ".../install-sh -c -d". For these automake
# versions, $(mkinstalldirs) and $(install_sh) are unused.
mkinstalldirs = $(SHELL) ${SHELL} /home/jman/git/freeipa-deps/freeipa/install-sh -d
install_sh = $(SHELL) ${SHELL} /home/jman/git/freeipa-deps/freeipa/install-sh
MKDIR_P = /usr/bin/mkdir -p
mkdir_p = $(MKDIR_P)

GMSGFMT_ = /usr/bin/msgfmt
GMSGFMT_no = /usr/bin/msgfmt
GMSGFMT_yes = /usr/bin/msgfmt
GMSGFMT = $(GMSGFMT_$(USE_MSGCTXT))
MSGFMT_ = /usr/bin/msgfmt
MSGFMT_no = /usr/bin/msgfmt
MSGFMT_yes = /usr/bin/msgfmt
MSGFMT = $(MSGFMT_$(USE_MSGCTXT))
XGETTEXT_ = /usr/bin/xgettext
XGETTEXT_no = /usr/bin/xgettext
XGETTEXT_yes = /usr/bin/xgettext
XGETTEXT = $(XGETTEXT_$(USE_MSGCTXT))
MSGMERGE = msgmerge
MSGMERGE_UPDATE = /usr/bin/msgmerge --update
MSGINIT = msginit
MSGCONV = msgconv
MSGFILTER = msgfilter

POFILES =  bn_IN.po ca.po cs.po de.po es.po eu.po fr.po hi.po hu.po id.po ja.po kn.po mr.po nl.po pa.po pl.po pt_BR.po ru.po sk.po tg.po uk.po zh_CN.po
GMOFILES =  bn_IN.gmo ca.gmo cs.gmo de.gmo es.gmo eu.gmo fr.gmo hi.gmo hu.gmo id.gmo ja.gmo kn.gmo mr.gmo nl.gmo pa.gmo pl.gmo pt_BR.gmo ru.gmo sk.gmo tg.gmo uk.gmo zh_CN.gmo
UPDATEPOFILES =  bn_IN.po-update ca.po-update cs.po-update de.po-update es.po-update eu.po-update fr.po-update hi.po-update hu.po-update id.po-update ja.po-update kn.po-update mr.po-update nl.po-update pa.po-update pl.po-update pt_BR.po-update ru.po-update sk.po-update tg.po-update uk.po-update zh_CN.po-update
DUMMYPOFILES =  bn_IN.nop ca.nop cs.nop de.nop es.nop eu.nop fr.nop hi.nop hu.nop id.nop ja.nop kn.nop mr.nop nl.nop pa.nop pl.nop pt_BR.nop ru.nop sk.nop tg.nop uk.nop zh_CN.nop
DISTFILES.common = Makefile.in.in remove-potcdate.sin \
$(DISTFILES.common.extra1) $(DISTFILES.common.extra2) $(DISTFILES.common.extra3)
DISTFILES = $(DISTFILES.common) Makevars POTFILES.in \
$(POFILES) $(GMOFILES) \
$(DISTFILES.extra1) $(DISTFILES.extra2) $(DISTFILES.extra3)

POTFILES = \
     .././daemons/ipa-otpd/internal.h \
     .././daemons/ipa-otpd/queue.c \
     .././daemons/ipa-otpd/parse.c \
     .././daemons/ipa-otpd/test.py \
     .././daemons/ipa-otpd/stdio.c \
     .././daemons/ipa-otpd/forward.c \
     .././daemons/ipa-otpd/main.c \
     .././daemons/ipa-otpd/query.c \
     .././daemons/ipa-otpd/bind.c \
     .././daemons/ipa-slapi-plugins/ipa-pwd-extop/prepost.c \
     .././daemons/ipa-slapi-plugins/ipa-pwd-extop/otpctrl.c \
     .././daemons/ipa-slapi-plugins/ipa-pwd-extop/encoding.c \
     .././daemons/ipa-slapi-plugins/ipa-pwd-extop/ipa_pwd_extop.c \
     .././daemons/ipa-slapi-plugins/ipa-pwd-extop/otpctrl.h \
     .././daemons/ipa-slapi-plugins/ipa-pwd-extop/common.c \
     .././daemons/ipa-slapi-plugins/ipa-pwd-extop/ipapwd.h \
     .././daemons/ipa-slapi-plugins/ipa-modrdn/ipa_modrdn.c \
     .././daemons/ipa-slapi-plugins/libotp/otp_token.h \
     .././daemons/ipa-slapi-plugins/libotp/otp_config.c \
     .././daemons/ipa-slapi-plugins/libotp/hotp.c \
     .././daemons/ipa-slapi-plugins/libotp/otp_config.h \
     .././daemons/ipa-slapi-plugins/libotp/otp_token.c \
     .././daemons/ipa-slapi-plugins/libotp/t_hotp.c \
     .././daemons/ipa-slapi-plugins/libotp/hotp.h \
     .././daemons/ipa-slapi-plugins/ipa-uuid/ipa_uuid.c \
     .././daemons/ipa-slapi-plugins/ipa-otp-counter/ldapmod.h \
     .././daemons/ipa-slapi-plugins/ipa-otp-counter/ldapmod.c \
     .././daemons/ipa-slapi-plugins/ipa-otp-counter/ipa_otp_counter.c \
     .././daemons/ipa-slapi-plugins/ipa-otp-counter/berval.c \
     .././daemons/ipa-slapi-plugins/ipa-otp-counter/berval.h \
     .././daemons/ipa-slapi-plugins/ipa-sidgen/ipa_sidgen_task.c \
     .././daemons/ipa-slapi-plugins/ipa-sidgen/ipa_sidgen.h \
     .././daemons/ipa-slapi-plugins/ipa-sidgen/ipa_sidgen.c \
     .././daemons/ipa-slapi-plugins/ipa-sidgen/ipa_sidgen_common.c \
     .././daemons/ipa-slapi-plugins/ipa-lockout/ipa_lockout.c \
     .././daemons/ipa-slapi-plugins/topology/topology_util.c \
     .././daemons/ipa-slapi-plugins/topology/topology_post.c \
     .././daemons/ipa-slapi-plugins/topology/topology_init.c \
     .././daemons/ipa-slapi-plugins/topology/topology_agmt.c \
     .././daemons/ipa-slapi-plugins/topology/topology_pre.c \
     .././daemons/ipa-slapi-plugins/topology/topology.h \
     .././daemons/ipa-slapi-plugins/topology/topology_cfg.c \
     .././daemons/ipa-slapi-plugins/common/util.h \
     .././daemons/ipa-slapi-plugins/ipa-extdom-extop/ipa_extdom_cmocka_tests.c \
     .././daemons/ipa-slapi-plugins/ipa-extdom-extop/ipa_extdom_common.c \
     .././daemons/ipa-slapi-plugins/ipa-extdom-extop/ipa_extdom_extop.c \
     .././daemons/ipa-slapi-plugins/ipa-extdom-extop/ipa_extdom.h \
     .././daemons/ipa-slapi-plugins/ipa-dns/ipa_dns.c \
     .././daemons/ipa-slapi-plugins/ipa-cldap/ipa_cldap_worker.c \
     .././daemons/ipa-slapi-plugins/ipa-cldap/ipa_cldap_tests.c \
     .././daemons/ipa-slapi-plugins/ipa-cldap/ipa_cldap.c \
     .././daemons/ipa-slapi-plugins/ipa-cldap/ipa_cldap.h \
     .././daemons/ipa-slapi-plugins/ipa-cldap/ipa_cldap_netlogon.c \
     .././daemons/ipa-slapi-plugins/ipa-otp-lasttoken/ipa_otp_lasttoken.c \
     .././daemons/ipa-slapi-plugins/ipa-enrollment/ipa_enrollment.c \
     .././daemons/ipa-slapi-plugins/ipa-winsync/ipa-winsync.h \
     .././daemons/ipa-slapi-plugins/ipa-winsync/ipa-winsync-config.c \
     .././daemons/ipa-slapi-plugins/ipa-winsync/ipa-winsync.c \
     .././daemons/ipa-slapi-plugins/ipa-version/ipa_repl_version.c \
     .././daemons/ipa-slapi-plugins/ipa-range-check/ipa_range_check.c \
     .././daemons/ipa-sam/ipa_sam.c \
     .././daemons/ipa-sam/ipa_sam.h \
     .././daemons/ipa-kdb/ipa_kdb_principals.c \
     .././daemons/ipa-kdb/tests/ipa_kdb_tests.c \
     .././daemons/ipa-kdb/ipa_kdb_common.c \
     .././daemons/ipa-kdb/ipa_kdb.c \
     .././daemons/ipa-kdb/ipa_kdb_passwords.c \
     .././daemons/ipa-kdb/ipa_kdb_mspac_private.h \
     .././daemons/ipa-kdb/ipa_kdb_mkey.c \
     .././daemons/ipa-kdb/ipa_kdb_audit_as.c \
     .././daemons/ipa-kdb/ipa_kdb.h \
     .././daemons/ipa-kdb/ipa_kdb_delegation.c \
     .././daemons/ipa-kdb/ipa_kdb_certauth.c \
     .././daemons/ipa-kdb/ipa_kdb_pwdpolicy.c \
     .././daemons/ipa-kdb/ipa_kdb_mspac.c \
     .././util/ipa_mspac.h \
     .././util/ipa_krb5.c \
     .././util/ipa_pwd_ntlm.c \
     .././util/ipa_pwd.c \
     .././util/ipa_krb5.h \
     .././util/ipa_pwd.h \
     .././doc/examples/examples.py \
     .././doc/examples/python-api.py \
     .././ipalib/config.py \
     .././ipalib/plugable.py \
     .././ipalib/request.py \
     .././ipalib/cli.py \
     .././ipalib/parameters.py \
     .././ipalib/aci.py \
     .././ipalib/rpc.py \
     .././ipalib/text.py \
     .././ipalib/__init__.py \
     .././ipalib/frontend.py \
     .././ipalib/base.py \
     .././ipalib/krb_utils.py \
     .././ipalib/util.py \
     .././ipalib/install/certstore.py \
     .././ipalib/install/__init__.py \
     .././ipalib/install/certmonger.py \
     .././ipalib/install/hostname.py \
     .././ipalib/install/service.py \
     .././ipalib/install/sysrestore.py \
     .././ipalib/install/kinit.py \
     .././ipalib/setup.py \
     .././ipalib/crud.py \
     .././ipalib/constants.py \
     .././ipalib/misc.py \
     .././ipalib/messages.py \
     .././ipalib/dns.py \
     .././ipalib/x509.py \
     .././ipalib/errors.py \
     .././ipalib/capabilities.py \
     .././ipalib/backend.py \
     .././ipalib/output.py \
     .././ipalib/pkcs10.py \
     .././pylint_plugins.py \
     .././install/share/wsgi.py \
     .././install/migration/migration.py \
     .././install/wsgi/plugins.py \
     .././ipasetup.py \
     .././contrib/nssciphersuite/nssciphersuite.py \
     .././contrib/copy-schema-to-ca-RHEL6.py \
     .././contrib/lite-server.py \
     .././ipaserver/__init__.py \
     .././ipaserver/advise/__init__.py \
     .././ipaserver/advise/base.py \
     .././ipaserver/advise/plugins/__init__.py \
     .././ipaserver/advise/plugins/fedora_authconfig.py \
     .././ipaserver/advise/plugins/smart_card_auth.py \
     .././ipaserver/advise/plugins/legacy_clients.py \
     .././ipaserver/topology.py \
     .././ipaserver/install/dsinstance.py \
     .././ipaserver/install/certs.py \
     .././ipaserver/install/ca.py \
     .././ipaserver/install/schemaupdate.py \
     .././ipaserver/install/ipa_server_upgrade.py \
     .././ipaserver/install/replication.py \
     .././ipaserver/install/custodiainstance.py \
     .././ipaserver/install/opendnssecinstance.py \
     .././ipaserver/install/ipa_backup.py \
     .././ipaserver/install/dogtag.py \
     .././ipaserver/install/ipa_replica_install.py \
     .././ipaserver/install/dogtaginstance.py \
     .././ipaserver/install/conncheck.py \
     .././ipaserver/install/kra.py \
     .././ipaserver/install/__init__.py \
     .././ipaserver/install/adtrustinstance.py \
     .././ipaserver/install/ipa_winsync_migrate.py \
     .././ipaserver/install/ntpinstance.py \
     .././ipaserver/install/odsexporterinstance.py \
     .././ipaserver/install/ipa_kra_install.py \
     .././ipaserver/install/ipa_otptoken_import.py \
     .././ipaserver/install/ipa_ldap_updater.py \
     .././ipaserver/install/plugins/rename_managed.py \
     .././ipaserver/install/plugins/update_managed_permissions.py \
     .././ipaserver/install/plugins/update_services.py \
     .././ipaserver/install/plugins/__init__.py \
     .././ipaserver/install/plugins/update_dna_shared_config.py \
     .././ipaserver/install/plugins/update_passsync.py \
     .././ipaserver/install/plugins/update_pacs.py \
     .././ipaserver/install/plugins/upload_cacrt.py \
     .././ipaserver/install/plugins/update_idranges.py \
     .././ipaserver/install/plugins/update_uniqueness.py \
     .././ipaserver/install/plugins/update_ca_topology.py \
     .././ipaserver/install/plugins/adtrust.py \
     .././ipaserver/install/plugins/update_fix_duplicate_cacrt_in_ldap.py \
     .././ipaserver/install/plugins/dns.py \
     .././ipaserver/install/plugins/update_referint.py \
     .././ipaserver/install/plugins/update_ldap_server_list.py \
     .././ipaserver/install/plugins/ca_renewal_master.py \
     .././ipaserver/install/plugins/update_nis.py \
     .././ipaserver/install/plugins/update_ra_cert_store.py \
     .././ipaserver/install/plugins/fix_replica_agreements.py \
     .././ipaserver/install/sysupgrade.py \
     .././ipaserver/install/httpinstance.py \
     .././ipaserver/install/ipa_cacert_manage.py \
     .././ipaserver/install/krbinstance.py \
     .././ipaserver/install/otpdinstance.py \
     .././ipaserver/install/adtrust.py \
     .././ipaserver/install/service.py \
     .././ipaserver/install/dnskeysyncinstance.py \
     .././ipaserver/install/dns.py \
     .././ipaserver/install/ipa_server_install.py \
     .././ipaserver/install/ipa_server_certinstall.py \
     .././ipaserver/install/ipa_replica_prepare.py \
     .././ipaserver/install/ipa_pkinit_manage.py \
     .././ipaserver/install/server/__init__.py \
     .././ipaserver/install/server/upgrade.py \
     .././ipaserver/install/server/replicainstall.py \
     .././ipaserver/install/server/install.py \
     .././ipaserver/install/bindinstance.py \
     .././ipaserver/install/ldapupdate.py \
     .././ipaserver/install/upgradeinstance.py \
     .././ipaserver/install/installutils.py \
     .././ipaserver/install/ipa_restore.py \
     .././ipaserver/install/krainstance.py \
     .././ipaserver/install/cainstance.py \
     .././ipaserver/setup.py \
     .././ipaserver/servroles.py \
     .././ipaserver/dcerpc.py \
     .././ipaserver/plugins/netgroup.py \
     .././ipaserver/plugins/config.py \
     .././ipaserver/plugins/ldap2.py \
     .././ipaserver/plugins/ca.py \
     .././ipaserver/plugins/automount.py \
     .././ipaserver/plugins/serverroles.py \
     .././ipaserver/plugins/vault.py \
     .././ipaserver/plugins/hbacsvc.py \
     .././ipaserver/plugins/location.py \
     .././ipaserver/plugins/batch.py \
     .././ipaserver/plugins/aci.py \
     .././ipaserver/plugins/otp.py \
     .././ipaserver/plugins/dogtag.py \
     .././ipaserver/plugins/rabase.py \
     .././ipaserver/plugins/hbactest.py \
     .././ipaserver/plugins/__init__.py \
     .././ipaserver/plugins/permission.py \
     .././ipaserver/plugins/sudorule.py \
     .././ipaserver/plugins/realmdomains.py \
     .././ipaserver/plugins/role.py \
     .././ipaserver/plugins/topology.py \
     .././ipaserver/plugins/session.py \
     .././ipaserver/plugins/radiusproxy.py \
     .././ipaserver/plugins/whoami.py \
     .././ipaserver/plugins/join.py \
     .././ipaserver/plugins/serverrole.py \
     .././ipaserver/plugins/krbtpolicy.py \
     .././ipaserver/plugins/caacl.py \
     .././ipaserver/plugins/otptoken.py \
     .././ipaserver/plugins/hbac.py \
     .././ipaserver/plugins/baseldap.py \
     .././ipaserver/plugins/xmlserver.py \
     .././ipaserver/plugins/sudocmd.py \
     .././ipaserver/plugins/ping.py \
     .././ipaserver/plugins/virtual.py \
     .././ipaserver/plugins/server.py \
     .././ipaserver/plugins/certmap.py \
     .././ipaserver/plugins/idrange.py \
     .././ipaserver/plugins/dnsserver.py \
     .././ipaserver/plugins/selinuxusermap.py \
     .././ipaserver/plugins/pwpolicy.py \
     .././ipaserver/plugins/misc.py \
     .././ipaserver/plugins/schema.py \
     .././ipaserver/plugins/certprofile.py \
     .././ipaserver/plugins/service.py \
     .././ipaserver/plugins/otpconfig.py \
     .././ipaserver/plugins/selfservice.py \
     .././ipaserver/plugins/passwd.py \
     .././ipaserver/plugins/dns.py \
     .././ipaserver/plugins/baseuser.py \
     .././ipaserver/plugins/stageuser.py \
     .././ipaserver/plugins/pkinit.py \
     .././ipaserver/plugins/hbacrule.py \
     .././ipaserver/plugins/domainlevel.py \
     .././ipaserver/plugins/hostgroup.py \
     .././ipaserver/plugins/delegation.py \
     .././ipaserver/plugins/idviews.py \
     .././ipaserver/plugins/cert.py \
     .././ipaserver/plugins/user.py \
     .././ipaserver/plugins/group.py \
     .././ipaserver/plugins/internal.py \
     .././ipaserver/plugins/servicedelegation.py \
     .././ipaserver/plugins/sudo.py \
     .././ipaserver/plugins/privilege.py \
     .././ipaserver/plugins/migration.py \
     .././ipaserver/plugins/hbacsvcgroup.py \
     .././ipaserver/plugins/automember.py \
     .././ipaserver/plugins/sudocmdgroup.py \
     .././ipaserver/plugins/trust.py \
     .././ipaserver/plugins/host.py \
     .././ipaserver/dns_data_management.py \
     .././ipaserver/secrets/__init__.py \
     .././ipaserver/secrets/kem.py \
     .././ipaserver/secrets/service.py \
     .././ipaserver/secrets/store.py \
     .././ipaserver/secrets/common.py \
     .././ipaserver/secrets/client.py \
     .././ipaserver/rpcserver.py \
     .././ipaserver/dnssec/odsmgr.py \
     .././ipaserver/dnssec/temp.py \
     .././ipaserver/dnssec/__init__.py \
     .././ipaserver/dnssec/ldapkeydb.py \
     .././ipaserver/dnssec/localhsm.py \
     .././ipaserver/dnssec/abshsm.py \
     .././ipaserver/dnssec/keysyncer.py \
     .././ipaserver/dnssec/syncrepl.py \
     .././ipaserver/dnssec/bindmgr.py \
     .././ipaserver/p11helper.py \
     .././ipapython/config.py \
     .././ipapython/dogtag.py \
     .././ipapython/__init__.py \
     .././ipapython/dnsutil.py \
     .././ipapython/certdb.py \
     .././ipapython/dn.py \
     .././ipapython/install/cli.py \
     .././ipapython/install/__init__.py \
     .././ipapython/install/util.py \
     .././ipapython/install/typing.py \
     .././ipapython/install/common.py \
     .././ipapython/install/core.py \
     .././ipapython/ipautil.py \
     .././ipapython/setup.py \
     .././ipapython/kerberos.py \
     .././ipapython/ipa_log_manager.py \
     .././ipapython/graph.py \
     .././ipapython/ipaldap.py \
     .././ipapython/cookie.py \
     .././ipapython/kernel_keyring.py \
     .././ipapython/ipavalidate.py \
     .././ipapython/admintool.py \
     .././ipapython/version.py \
     .././ipapython/session_storage.py \
     .././ipapython/ssh.py \
     .././ipapython/errors.py \
     .././ipapython/nsslib.py \
     .././client/ipa-join.c \
     .././client/ipa-rmkeytab.c \
     .././client/ipa-client-common.h \
     .././client/config.c \
     .././client/ipa-client-common.c \
     .././client/ipa-getkeytab.c \
     .././ipaclient/remote_plugins/2_156/netgroup.py \
     .././ipaclient/remote_plugins/2_156/config.py \
     .././ipaclient/remote_plugins/2_156/automount.py \
     .././ipaclient/remote_plugins/2_156/otptoken_yubikey.py \
     .././ipaclient/remote_plugins/2_156/vault.py \
     .././ipaclient/remote_plugins/2_156/hbacsvc.py \
     .././ipaclient/remote_plugins/2_156/batch.py \
     .././ipaclient/remote_plugins/2_156/aci.py \
     .././ipaclient/remote_plugins/2_156/hbactest.py \
     .././ipaclient/remote_plugins/2_156/__init__.py \
     .././ipaclient/remote_plugins/2_156/permission.py \
     .././ipaclient/remote_plugins/2_156/sudorule.py \
     .././ipaclient/remote_plugins/2_156/realmdomains.py \
     .././ipaclient/remote_plugins/2_156/role.py \
     .././ipaclient/remote_plugins/2_156/topology.py \
     .././ipaclient/remote_plugins/2_156/session.py \
     .././ipaclient/remote_plugins/2_156/radiusproxy.py \
     .././ipaclient/remote_plugins/2_156/join.py \
     .././ipaclient/remote_plugins/2_156/krbtpolicy.py \
     .././ipaclient/remote_plugins/2_156/caacl.py \
     .././ipaclient/remote_plugins/2_156/otptoken.py \
     .././ipaclient/remote_plugins/2_156/sudocmd.py \
     .././ipaclient/remote_plugins/2_156/ping.py \
     .././ipaclient/remote_plugins/2_156/server.py \
     .././ipaclient/remote_plugins/2_156/idrange.py \
     .././ipaclient/remote_plugins/2_156/selinuxusermap.py \
     .././ipaclient/remote_plugins/2_156/pwpolicy.py \
     .././ipaclient/remote_plugins/2_156/misc.py \
     .././ipaclient/remote_plugins/2_156/certprofile.py \
     .././ipaclient/remote_plugins/2_156/service.py \
     .././ipaclient/remote_plugins/2_156/otpconfig.py \
     .././ipaclient/remote_plugins/2_156/selfservice.py \
     .././ipaclient/remote_plugins/2_156/passwd.py \
     .././ipaclient/remote_plugins/2_156/dns.py \
     .././ipaclient/remote_plugins/2_156/stageuser.py \
     .././ipaclient/remote_plugins/2_156/pkinit.py \
     .././ipaclient/remote_plugins/2_156/hbacrule.py \
     .././ipaclient/remote_plugins/2_156/domainlevel.py \
     .././ipaclient/remote_plugins/2_156/hostgroup.py \
     .././ipaclient/remote_plugins/2_156/delegation.py \
     .././ipaclient/remote_plugins/2_156/idviews.py \
     .././ipaclient/remote_plugins/2_156/cert.py \
     .././ipaclient/remote_plugins/2_156/user.py \
     .././ipaclient/remote_plugins/2_156/group.py \
     .././ipaclient/remote_plugins/2_156/internal.py \
     .././ipaclient/remote_plugins/2_156/servicedelegation.py \
     .././ipaclient/remote_plugins/2_156/privilege.py \
     .././ipaclient/remote_plugins/2_156/migration.py \
     .././ipaclient/remote_plugins/2_156/hbacsvcgroup.py \
     .././ipaclient/remote_plugins/2_156/automember.py \
     .././ipaclient/remote_plugins/2_156/sudocmdgroup.py \
     .././ipaclient/remote_plugins/2_156/trust.py \
     .././ipaclient/remote_plugins/2_156/host.py \
     .././ipaclient/remote_plugins/__init__.py \
     .././ipaclient/remote_plugins/compat.py \
     .././ipaclient/remote_plugins/2_114/netgroup.py \
     .././ipaclient/remote_plugins/2_114/config.py \
     .././ipaclient/remote_plugins/2_114/automount.py \
     .././ipaclient/remote_plugins/2_114/otptoken_yubikey.py \
     .././ipaclient/remote_plugins/2_114/hbacsvc.py \
     .././ipaclient/remote_plugins/2_114/batch.py \
     .././ipaclient/remote_plugins/2_114/aci.py \
     .././ipaclient/remote_plugins/2_114/hbactest.py \
     .././ipaclient/remote_plugins/2_114/__init__.py \
     .././ipaclient/remote_plugins/2_114/permission.py \
     .././ipaclient/remote_plugins/2_114/sudorule.py \
     .././ipaclient/remote_plugins/2_114/realmdomains.py \
     .././ipaclient/remote_plugins/2_114/role.py \
     .././ipaclient/remote_plugins/2_114/session.py \
     .././ipaclient/remote_plugins/2_114/radiusproxy.py \
     .././ipaclient/remote_plugins/2_114/join.py \
     .././ipaclient/remote_plugins/2_114/krbtpolicy.py \
     .././ipaclient/remote_plugins/2_114/otptoken.py \
     .././ipaclient/remote_plugins/2_114/sudocmd.py \
     .././ipaclient/remote_plugins/2_114/ping.py \
     .././ipaclient/remote_plugins/2_114/idrange.py \
     .././ipaclient/remote_plugins/2_114/selinuxusermap.py \
     .././ipaclient/remote_plugins/2_114/pwpolicy.py \
     .././ipaclient/remote_plugins/2_114/misc.py \
     .././ipaclient/remote_plugins/2_114/service.py \
     .././ipaclient/remote_plugins/2_114/otpconfig.py \
     .././ipaclient/remote_plugins/2_114/selfservice.py \
     .././ipaclient/remote_plugins/2_114/passwd.py \
     .././ipaclient/remote_plugins/2_114/dns.py \
     .././ipaclient/remote_plugins/2_114/pkinit.py \
     .././ipaclient/remote_plugins/2_114/hbacrule.py \
     .././ipaclient/remote_plugins/2_114/hostgroup.py \
     .././ipaclient/remote_plugins/2_114/delegation.py \
     .././ipaclient/remote_plugins/2_114/idviews.py \
     .././ipaclient/remote_plugins/2_114/cert.py \
     .././ipaclient/remote_plugins/2_114/user.py \
     .././ipaclient/remote_plugins/2_114/group.py \
     .././ipaclient/remote_plugins/2_114/internal.py \
     .././ipaclient/remote_plugins/2_114/privilege.py \
     .././ipaclient/remote_plugins/2_114/migration.py \
     .././ipaclient/remote_plugins/2_114/hbacsvcgroup.py \
     .././ipaclient/remote_plugins/2_114/automember.py \
     .././ipaclient/remote_plugins/2_114/sudocmdgroup.py \
     .././ipaclient/remote_plugins/2_114/trust.py \
     .././ipaclient/remote_plugins/2_114/host.py \
     .././ipaclient/remote_plugins/schema.py \
     .././ipaclient/remote_plugins/2_49/netgroup.py \
     .././ipaclient/remote_plugins/2_49/config.py \
     .././ipaclient/remote_plugins/2_49/automount.py \
     .././ipaclient/remote_plugins/2_49/hbacsvc.py \
     .././ipaclient/remote_plugins/2_49/batch.py \
     .././ipaclient/remote_plugins/2_49/aci.py \
     .././ipaclient/remote_plugins/2_49/hbactest.py \
     .././ipaclient/remote_plugins/2_49/__init__.py \
     .././ipaclient/remote_plugins/2_49/permission.py \
     .././ipaclient/remote_plugins/2_49/sudorule.py \
     .././ipaclient/remote_plugins/2_49/role.py \
     .././ipaclient/remote_plugins/2_49/session.py \
     .././ipaclient/remote_plugins/2_49/join.py \
     .././ipaclient/remote_plugins/2_49/krbtpolicy.py \
     .././ipaclient/remote_plugins/2_49/entitle.py \
     .././ipaclient/remote_plugins/2_49/sudocmd.py \
     .././ipaclient/remote_plugins/2_49/ping.py \
     .././ipaclient/remote_plugins/2_49/idrange.py \
     .././ipaclient/remote_plugins/2_49/selinuxusermap.py \
     .././ipaclient/remote_plugins/2_49/pwpolicy.py \
     .././ipaclient/remote_plugins/2_49/misc.py \
     .././ipaclient/remote_plugins/2_49/service.py \
     .././ipaclient/remote_plugins/2_49/selfservice.py \
     .././ipaclient/remote_plugins/2_49/passwd.py \
     .././ipaclient/remote_plugins/2_49/dns.py \
     .././ipaclient/remote_plugins/2_49/pkinit.py \
     .././ipaclient/remote_plugins/2_49/hbacrule.py \
     .././ipaclient/remote_plugins/2_49/hostgroup.py \
     .././ipaclient/remote_plugins/2_49/delegation.py \
     .././ipaclient/remote_plugins/2_49/cert.py \
     .././ipaclient/remote_plugins/2_49/user.py \
     .././ipaclient/remote_plugins/2_49/group.py \
     .././ipaclient/remote_plugins/2_49/internal.py \
     .././ipaclient/remote_plugins/2_49/privilege.py \
     .././ipaclient/remote_plugins/2_49/migration.py \
     .././ipaclient/remote_plugins/2_49/hbacsvcgroup.py \
     .././ipaclient/remote_plugins/2_49/automember.py \
     .././ipaclient/remote_plugins/2_49/sudocmdgroup.py \
     .././ipaclient/remote_plugins/2_49/trust.py \
     .././ipaclient/remote_plugins/2_49/host.py \
     .././ipaclient/remote_plugins/2_164/netgroup.py \
     .././ipaclient/remote_plugins/2_164/config.py \
     .././ipaclient/remote_plugins/2_164/automount.py \
     .././ipaclient/remote_plugins/2_164/otptoken_yubikey.py \
     .././ipaclient/remote_plugins/2_164/vault.py \
     .././ipaclient/remote_plugins/2_164/hbacsvc.py \
     .././ipaclient/remote_plugins/2_164/batch.py \
     .././ipaclient/remote_plugins/2_164/aci.py \
     .././ipaclient/remote_plugins/2_164/hbactest.py \
     .././ipaclient/remote_plugins/2_164/__init__.py \
     .././ipaclient/remote_plugins/2_164/permission.py \
     .././ipaclient/remote_plugins/2_164/sudorule.py \
     .././ipaclient/remote_plugins/2_164/realmdomains.py \
     .././ipaclient/remote_plugins/2_164/role.py \
     .././ipaclient/remote_plugins/2_164/topology.py \
     .././ipaclient/remote_plugins/2_164/session.py \
     .././ipaclient/remote_plugins/2_164/radiusproxy.py \
     .././ipaclient/remote_plugins/2_164/join.py \
     .././ipaclient/remote_plugins/2_164/krbtpolicy.py \
     .././ipaclient/remote_plugins/2_164/caacl.py \
     .././ipaclient/remote_plugins/2_164/otptoken.py \
     .././ipaclient/remote_plugins/2_164/sudocmd.py \
     .././ipaclient/remote_plugins/2_164/ping.py \
     .././ipaclient/remote_plugins/2_164/server.py \
     .././ipaclient/remote_plugins/2_164/idrange.py \
     .././ipaclient/remote_plugins/2_164/selinuxusermap.py \
     .././ipaclient/remote_plugins/2_164/pwpolicy.py \
     .././ipaclient/remote_plugins/2_164/misc.py \
     .././ipaclient/remote_plugins/2_164/certprofile.py \
     .././ipaclient/remote_plugins/2_164/service.py \
     .././ipaclient/remote_plugins/2_164/otpconfig.py \
     .././ipaclient/remote_plugins/2_164/selfservice.py \
     .././ipaclient/remote_plugins/2_164/passwd.py \
     .././ipaclient/remote_plugins/2_164/dns.py \
     .././ipaclient/remote_plugins/2_164/stageuser.py \
     .././ipaclient/remote_plugins/2_164/pkinit.py \
     .././ipaclient/remote_plugins/2_164/hbacrule.py \
     .././ipaclient/remote_plugins/2_164/domainlevel.py \
     .././ipaclient/remote_plugins/2_164/hostgroup.py \
     .././ipaclient/remote_plugins/2_164/delegation.py \
     .././ipaclient/remote_plugins/2_164/idviews.py \
     .././ipaclient/remote_plugins/2_164/cert.py \
     .././ipaclient/remote_plugins/2_164/user.py \
     .././ipaclient/remote_plugins/2_164/group.py \
     .././ipaclient/remote_plugins/2_164/internal.py \
     .././ipaclient/remote_plugins/2_164/servicedelegation.py \
     .././ipaclient/remote_plugins/2_164/privilege.py \
     .././ipaclient/remote_plugins/2_164/migration.py \
     .././ipaclient/remote_plugins/2_164/hbacsvcgroup.py \
     .././ipaclient/remote_plugins/2_164/automember.py \
     .././ipaclient/remote_plugins/2_164/sudocmdgroup.py \
     .././ipaclient/remote_plugins/2_164/trust.py \
     .././ipaclient/remote_plugins/2_164/host.py \
     .././ipaclient/__init__.py \
     .././ipaclient/__main__.py \
     .././ipaclient/frontend.py \
     .././ipaclient/csrgen_ffi.py \
     .././ipaclient/install/automount.py \
     .././ipaclient/install/__init__.py \
     .././ipaclient/install/ipachangeconf.py \
     .././ipaclient/install/ipa_certupdate.py \
     .././ipaclient/install/sssd.py \
     .././ipaclient/install/ipadiscovery.py \
     .././ipaclient/install/client.py \
     .././ipaclient/install/ntpconf.py \
     .././ipaclient/install/ipa_client_install.py \
     .././ipaclient/setup.py \
     .././ipaclient/plugins/ca.py \
     .././ipaclient/plugins/automount.py \
     .././ipaclient/plugins/otptoken_yubikey.py \
     .././ipaclient/plugins/vault.py \
     .././ipaclient/plugins/location.py \
     .././ipaclient/plugins/hbactest.py \
     .././ipaclient/plugins/__init__.py \
     .././ipaclient/plugins/permission.py \
     .././ipaclient/plugins/sudorule.py \
     .././ipaclient/plugins/topology.py \
     .././ipaclient/plugins/rpcclient.py \
     .././ipaclient/plugins/otptoken.py \
     .././ipaclient/plugins/csrgen.py \
     .././ipaclient/plugins/server.py \
     .././ipaclient/plugins/certmap.py \
     .././ipaclient/plugins/idrange.py \
     .././ipaclient/plugins/misc.py \
     .././ipaclient/plugins/certprofile.py \
     .././ipaclient/plugins/service.py \
     .././ipaclient/plugins/passwd.py \
     .././ipaclient/plugins/dns.py \
     .././ipaclient/plugins/hbacrule.py \
     .././ipaclient/plugins/cert.py \
     .././ipaclient/plugins/user.py \
     .././ipaclient/plugins/internal.py \
     .././ipaclient/plugins/migration.py \
     .././ipaclient/plugins/automember.py \
     .././ipaclient/plugins/trust.py \
     .././ipaclient/plugins/host.py \
     .././ipaclient/csrgen.py \
     .././ipatests/test_ipaserver/httptest.py \
     .././ipatests/test_ipaserver/test_topology_plugin.py \
     .././ipatests/test_ipaserver/test_dnssec.py \
     .././ipatests/test_ipaserver/test_ipap11helper.py \
     .././ipatests/test_ipaserver/test_serverroles.py \
     .././ipatests/test_ipaserver/__init__.py \
     .././ipatests/test_ipaserver/test_ldap.py \
     .././ipatests/test_ipaserver/test_secrets.py \
     .././ipatests/test_ipaserver/test_install/__init__.py \
     .././ipatests/test_ipaserver/test_install/test_service.py \
     .././ipatests/test_ipaserver/test_install/test_adtrustinstance.py \
     .././ipatests/test_ipaserver/test_rpcserver.py \
     .././ipatests/test_ipaserver/test_otptoken_import.py \
     .././ipatests/test_ipaserver/test_kadmin.py \
     .././ipatests/test_ipaserver/test_version_comparison.py \
     .././ipatests/test_ipaserver/test_changepw.py \
     .././ipatests/test_cmdline/cmdline.py \
     .././ipatests/test_cmdline/__init__.py \
     .././ipatests/test_cmdline/test_ipagetkeytab.py \
     .././ipatests/test_cmdline/test_cli.py \
     .././ipatests/test_cmdline/test_help.py \
     .././ipatests/__init__.py \
     .././ipatests/i18n.py \
     .././ipatests/util.py \
     .././ipatests/setup.py \
     .././ipatests/test_integration/test_forced_client_reenrollment.py \
     .././ipatests/test_integration/test_service_permissions.py \
     .././ipatests/test_integration/test_server_del.py \
     .././ipatests/test_integration/test_dnssec.py \
     .././ipatests/test_integration/test_idviews.py \
     .././ipatests/test_integration/test_legacy_clients.py \
     .././ipatests/test_integration/create_caless_pki.py \
     .././ipatests/test_integration/test_topology.py \
     .././ipatests/test_integration/test_dns_locations.py \
     .././ipatests/test_integration/test_vault.py \
     .././ipatests/test_integration/__init__.py \
     .././ipatests/test_integration/test_http_kdc_proxy.py \
     .././ipatests/test_integration/test_caless.py \
     .././ipatests/test_integration/test_trust.py \
     .././ipatests/test_integration/test_replication_layouts.py \
     .././ipatests/test_integration/base.py \
     .././ipatests/test_integration/test_backup_and_restore.py \
     .././ipatests/test_integration/test_kerberos_flags.py \
     .././ipatests/test_integration/test_installation.py \
     .././ipatests/test_integration/test_advise.py \
     .././ipatests/test_integration/test_netgroup.py \
     .././ipatests/test_integration/test_ordering.py \
     .././ipatests/test_integration/test_customized_ds_config_install.py \
     .././ipatests/test_integration/test_simple_replication.py \
     .././ipatests/test_integration/test_external_ca.py \
     .././ipatests/test_integration/test_testconfig.py \
     .././ipatests/test_integration/test_sudo.py \
     .././ipatests/test_integration/test_topologies.py \
     .././ipatests/test_integration/test_replica_promotion.py \
     .././ipatests/test_util.py \
     .././ipatests/test_xmlrpc/testcert.py \
     .././ipatests/test_xmlrpc/test_idviews_plugin.py \
     .././ipatests/test_xmlrpc/test_caacl_profile_enforcement.py \
     .././ipatests/test_xmlrpc/test_pwpolicy_plugin.py \
     .././ipatests/test_xmlrpc/test_servicedelegation_plugin.py \
     .././ipatests/test_xmlrpc/test_selinuxusermap_plugin.py \
     .././ipatests/test_xmlrpc/test_kerberos_principal_aliases.py \
     .././ipatests/test_xmlrpc/test_radiusproxy_plugin.py \
     .././ipatests/test_xmlrpc/test_hbacsvcgroup_plugin.py \
     .././ipatests/test_xmlrpc/test_realmdomains_plugin.py \
     .././ipatests/test_xmlrpc/test_host_plugin.py \
     .././ipatests/test_xmlrpc/__init__.py \
     .././ipatests/test_xmlrpc/test_role_plugin.py \
     .././ipatests/test_xmlrpc/test_certprofile_plugin.py \
     .././ipatests/test_xmlrpc/test_location_plugin.py \
     .././ipatests/test_xmlrpc/test_config_plugin.py \
     .././ipatests/test_xmlrpc/test_permission_plugin.py \
     .././ipatests/test_xmlrpc/test_whoami_plugin.py \
     .././ipatests/test_xmlrpc/test_automember_plugin.py \
     .././ipatests/test_xmlrpc/test_attr.py \
     .././ipatests/test_xmlrpc/test_sudorule_plugin.py \
     .././ipatests/test_xmlrpc/test_trust_plugin.py \
     .././ipatests/test_xmlrpc/test_dns_plugin.py \
     .././ipatests/test_xmlrpc/test_add_remove_cert_cmd.py \
     .././ipatests/test_xmlrpc/test_vault_plugin.py \
     .././ipatests/test_xmlrpc/test_ca_plugin.py \
     .././ipatests/test_xmlrpc/test_external_members.py \
     .././ipatests/test_xmlrpc/test_old_permission_plugin.py \
     .././ipatests/test_xmlrpc/test_user_plugin.py \
     .././ipatests/test_xmlrpc/test_hostgroup_plugin.py \
     .././ipatests/test_xmlrpc/test_sudocmdgroup_plugin.py \
     .././ipatests/test_xmlrpc/tracker/service_plugin.py \
     .././ipatests/test_xmlrpc/tracker/sudocmd_plugin.py \
     .././ipatests/test_xmlrpc/tracker/host_plugin.py \
     .././ipatests/test_xmlrpc/tracker/kerberos_aliases.py \
     .././ipatests/test_xmlrpc/tracker/__init__.py \
     .././ipatests/test_xmlrpc/tracker/group_plugin.py \
     .././ipatests/test_xmlrpc/tracker/hostgroup_plugin.py \
     .././ipatests/test_xmlrpc/tracker/base.py \
     .././ipatests/test_xmlrpc/tracker/user_plugin.py \
     .././ipatests/test_xmlrpc/tracker/server_plugin.py \
     .././ipatests/test_xmlrpc/tracker/automember_plugin.py \
     .././ipatests/test_xmlrpc/tracker/certmapdata.py \
     .././ipatests/test_xmlrpc/tracker/location_plugin.py \
     .././ipatests/test_xmlrpc/tracker/sudocmdgroup_plugin.py \
     .././ipatests/test_xmlrpc/tracker/stageuser_plugin.py \
     .././ipatests/test_xmlrpc/tracker/ca_plugin.py \
     .././ipatests/test_xmlrpc/tracker/caacl_plugin.py \
     .././ipatests/test_xmlrpc/tracker/certprofile_plugin.py \
     .././ipatests/test_xmlrpc/tracker/idview_plugin.py \
     .././ipatests/test_xmlrpc/tracker/certmap_plugin.py \
     .././ipatests/test_xmlrpc/test_nesting.py \
     .././ipatests/test_xmlrpc/test_caacl_plugin.py \
     .././ipatests/test_xmlrpc/test_netgroup_plugin.py \
     .././ipatests/test_xmlrpc/mock_trust.py \
     .././ipatests/test_xmlrpc/test_hbac_plugin.py \
     .././ipatests/test_xmlrpc/test_ping_plugin.py \
     .././ipatests/test_xmlrpc/test_delegation_plugin.py \
     .././ipatests/test_xmlrpc/test_cert_plugin.py \
     .././ipatests/test_xmlrpc/test_certmap_plugin.py \
     .././ipatests/test_xmlrpc/test_baseldap_plugin.py \
     .././ipatests/test_xmlrpc/objectclasses.py \
     .././ipatests/test_xmlrpc/test_hbactest_plugin.py \
     .././ipatests/test_xmlrpc/test_batch_plugin.py \
     .././ipatests/test_xmlrpc/test_krbtpolicy.py \
     .././ipatests/test_xmlrpc/test_service_plugin.py \
     .././ipatests/test_xmlrpc/xmlrpc_test.py \
     .././ipatests/test_xmlrpc/test_sudocmd_plugin.py \
     .././ipatests/test_xmlrpc/test_range_plugin.py \
     .././ipatests/test_xmlrpc/test_selfservice_plugin.py \
     .././ipatests/test_xmlrpc/test_passwd_plugin.py \
     .././ipatests/test_xmlrpc/test_stageuser_plugin.py \
     .././ipatests/test_xmlrpc/test_group_plugin.py \
     .././ipatests/test_xmlrpc/test_privilege_plugin.py \
     .././ipatests/test_xmlrpc/test_dns_realmdomains_integration.py \
     .././ipatests/test_xmlrpc/test_replace.py \
     .././ipatests/test_xmlrpc/test_automount_plugin.py \
     .././ipatests/data.py \
     .././ipatests/test_install/__init__.py \
     .././ipatests/test_install/test_updates.py \
     .././ipatests/test_pkcs10/test_pkcs10.py \
     .././ipatests/test_pkcs10/__init__.py \
     .././ipatests/test_ipapython/test_ssh.py \
     .././ipatests/test_ipapython/test_session_storage.py \
     .././ipatests/test_ipapython/test_keyring.py \
     .././ipatests/test_ipapython/test_ipautil.py \
     .././ipatests/test_ipapython/test_ipavalidate.py \
     .././ipatests/test_ipapython/__init__.py \
     .././ipatests/test_ipapython/test_dn.py \
     .././ipatests/test_ipapython/test_cookie.py \
     .././ipatests/test_ipapython/test_kerberos.py \
     .././ipatests/test_ipaclient/__init__.py \
     .././ipatests/test_ipaclient/test_csrgen.py \
     .././ipatests/pytest_plugins/beakerlib.py \
     .././ipatests/pytest_plugins/__init__.py \
     .././ipatests/pytest_plugins/nose_compat.py \
     .././ipatests/pytest_plugins/declarative.py \
     .././ipatests/pytest_plugins/additional_config.py \
     .././ipatests/pytest_plugins/integration/config.py \
     .././ipatests/pytest_plugins/integration/__init__.py \
     .././ipatests/pytest_plugins/integration/tasks.py \
     .././ipatests/pytest_plugins/integration/env_config.py \
     .././ipatests/pytest_plugins/integration/host.py \
     .././ipatests/conftest.py \
     .././ipatests/test_ipalib/test_base.py \
     .././ipatests/test_ipalib/test_plugable.py \
     .././ipatests/test_ipalib/test_rpc.py \
     .././ipatests/test_ipalib/test_x509.py \
     .././ipatests/test_ipalib/__init__.py \
     .././ipatests/test_ipalib/test_aci.py \
     .././ipatests/test_ipalib/test_frontend.py \
     .././ipatests/test_ipalib/test_text.py \
     .././ipatests/test_ipalib/test_output.py \
     .././ipatests/test_ipalib/test_cli.py \
     .././ipatests/test_ipalib/test_crud.py \
     .././ipatests/test_ipalib/test_parameters.py \
     .././ipatests/test_ipalib/test_errors.py \
     .././ipatests/test_ipalib/test_messages.py \
     .././ipatests/test_ipalib/test_backend.py \
     .././ipatests/test_ipalib/test_capabilities.py \
     .././ipatests/test_ipalib/test_config.py \
     .././ipatests/test_webui/test_realmdomains.py \
     .././ipatests/test_webui/data_sudo.py \
     .././ipatests/test_webui/test_host.py \
     .././ipatests/test_webui/data_hostgroup.py \
     .././ipatests/test_webui/test_idviews.py \
     .././ipatests/test_webui/test_dns.py \
     .././ipatests/test_webui/test_vault.py \
     .././ipatests/test_webui/test_pwpolicy.py \
     .././ipatests/test_webui/test_navigation.py \
     .././ipatests/test_webui/__init__.py \
     .././ipatests/test_webui/test_hostgroup.py \
     .././ipatests/test_webui/data_user.py \
     .././ipatests/test_webui/test_trust.py \
     .././ipatests/test_webui/test_delegation.py \
     .././ipatests/test_webui/task_range.py \
     .././ipatests/test_webui/data_vault.py \
     .././ipatests/test_webui/data_group.py \
     .././ipatests/test_webui/data_hbac.py \
     .././ipatests/test_webui/test_hbac.py \
     .././ipatests/test_webui/test_automount.py \
     .././ipatests/test_webui/test_user.py \
     .././ipatests/test_webui/test_range.py \
     .././ipatests/test_webui/test_cert.py \
     .././ipatests/test_webui/test_selinuxusermap.py \
     .././ipatests/test_webui/ui_driver.py \
     .././ipatests/test_webui/test_group.py \
     .././ipatests/test_webui/data_netgroup.py \
     .././ipatests/test_webui/data_idviews.py \
     .././ipatests/test_webui/test_netgroup.py \
     .././ipatests/test_webui/test_service.py \
     .././ipatests/test_webui/test_rbac.py \
     .././ipatests/test_webui/test_krbtpolicy.py \
     .././ipatests/test_webui/test_automember.py \
     .././ipatests/test_webui/test_selfservice.py \
     .././ipatests/test_webui/test_sudo.py \
     .././ipatests/test_webui/test_config.py \
     .././pypi/test_placeholder.py \
     .././pypi/ipa/setup.py \
     .././pypi/ipaserver/setup.py \
     .././pypi/ipaserver/ipaserver/__init__.py \
     .././pypi/ipatests/setup.py \
     .././pypi/ipatests/ipatests/__init__.py \
     .././pypi/ipaplatform/setup.py \
     .././pypi/ipaplatform/ipaplatform/__init__.py \
     .././pypi/freeipa/setup.py \
     .././ipaplatform/redhat/__init__.py \
     .././ipaplatform/redhat/paths.py \
     .././ipaplatform/redhat/constants.py \
     .././ipaplatform/redhat/authconfig.py \
     .././ipaplatform/redhat/tasks.py \
     .././ipaplatform/redhat/services.py \
     .././ipaplatform/__init__.py \
     .././ipaplatform/paths.py \
     .././ipaplatform/fedora/__init__.py \
     .././ipaplatform/fedora/paths.py \
     .././ipaplatform/fedora/constants.py \
     .././ipaplatform/fedora/tasks.py \
     .././ipaplatform/fedora/services.py \
     .././ipaplatform/setup.py \
     .././ipaplatform/base/__init__.py \
     .././ipaplatform/base/paths.py \
     .././ipaplatform/base/constants.py \
     .././ipaplatform/base/tasks.py \
     .././ipaplatform/base/services.py \
     .././ipaplatform/constants.py \
     .././ipaplatform/tasks.py \
     .././ipaplatform/services.py \
     .././ipaplatform/debian/__init__.py \
     .././ipaplatform/debian/paths.py \
     .././ipaplatform/debian/constants.py \
     .././ipaplatform/debian/tasks.py \
     .././ipaplatform/debian/services.py \
     .././ipaplatform/rhel/__init__.py \
     .././ipaplatform/rhel/paths.py \
     .././ipaplatform/rhel/constants.py \
     .././ipaplatform/rhel/tasks.py \
     .././ipaplatform/rhel/services.py \
     .././ignore_import_errors.py \
     .././asn1/ipa_asn1.c \
     .././asn1/ipa_asn1.h \
     .././asn1/asn1c/INTEGER.h \
     .././asn1/asn1c/GKNewKeys.h \
     .././asn1/asn1c/der_encoder.h \
     .././asn1/asn1c/asn_internal.h \
     .././asn1/asn1c/per_support.c \
     .././asn1/asn1c/OCTET_STRING.h \
     .././asn1/asn1c/constr_SEQUENCE_OF.h \
     .././asn1/asn1c/constr_CHOICE.h \
     .././asn1/asn1c/NativeInteger.h \
     .././asn1/asn1c/constraints.h \
     .././asn1/asn1c/GetKeytabControl.h \
     .././asn1/asn1c/per_encoder.c \
     .././asn1/asn1c/constr_TYPE.h \
     .././asn1/asn1c/asn_system.h \
     .././asn1/asn1c/asn_application.h \
     .././asn1/asn1c/asn_codecs_prim.c \
     .././asn1/asn1c/GKReply.c \
     .././asn1/asn1c/per_opentype.h \
     .././asn1/asn1c/TypeValuePair.c \
     .././asn1/asn1c/der_encoder.c \
     .././asn1/asn1c/KrbKey.c \
     .././asn1/asn1c/constr_SEQUENCE.c \
     .././asn1/asn1c/BIT_STRING.c \
     .././asn1/asn1c/xer_encoder.c \
     .././asn1/asn1c/xer_encoder.h \
     .././asn1/asn1c/asn_codecs_prim.h \
     .././asn1/asn1c/OCTET_STRING.c \
     .././asn1/asn1c/ber_tlv_length.c \
     .././asn1/asn1c/ber_tlv_tag.c \
     .././asn1/asn1c/GKNewKeys.c \
     .././asn1/asn1c/NativeEnumerated.h \
     .././asn1/asn1c/per_decoder.c \
     .././asn1/asn1c/ber_decoder.h \
     .././asn1/asn1c/ber_decoder.c \
     .././asn1/asn1c/NativeInteger.c \
     .././asn1/asn1c/GKReply.h \
     .././asn1/asn1c/constr_SEQUENCE_OF.c \
     .././asn1/asn1c/constr_CHOICE.c \
     .././asn1/asn1c/KrbKey.h \
     .././asn1/asn1c/ber_tlv_length.h \
     .././asn1/asn1c/asn_SEQUENCE_OF.c \
     .././asn1/asn1c/constr_TYPE.c \
     .././asn1/asn1c/ber_tlv_tag.h \
     .././asn1/asn1c/GKCurrentKeys.h \
     .././asn1/asn1c/xer_decoder.c \
     .././asn1/asn1c/per_decoder.h \
     .././asn1/asn1c/BIT_STRING.h \
     .././asn1/asn1c/per_opentype.c \
     .././asn1/asn1c/Int32.h \
     .././asn1/asn1c/constr_SET_OF.c \
     .././asn1/asn1c/GetKeytabControl.c \
     .././asn1/asn1c/xer_support.c \
     .././asn1/asn1c/TypeValuePair.h \
     .././asn1/asn1c/NativeEnumerated.c \
     .././asn1/asn1c/per_support.h \
     .././asn1/asn1c/asn_codecs.h \
     .././asn1/asn1c/GKCurrentKeys.c \
     .././asn1/asn1c/constr_SET_OF.h \
     .././asn1/asn1c/asn_SEQUENCE_OF.h \
     .././asn1/asn1c/xer_support.h \
     .././asn1/asn1c/per_encoder.h \
     .././asn1/asn1c/asn_SET_OF.h \
     .././asn1/asn1c/asn_SET_OF.c \
     .././asn1/asn1c/Int32.c \
     .././asn1/asn1c/INTEGER.c \
     .././asn1/asn1c/constraints.c \
     .././asn1/asn1c/xer_decoder.h \
     .././asn1/asn1c/constr_SEQUENCE.h

CATALOGS =  bn_IN.gmo ca.gmo cs.gmo de.gmo es.gmo eu.gmo fr.gmo hi.gmo hu.gmo id.gmo ja.gmo kn.gmo mr.gmo nl.gmo pa.gmo pl.gmo pt_BR.gmo ru.gmo sk.gmo tg.gmo uk.gmo zh_CN.gmo

# Makevars gets inserted here. (Don't remove this line!)
# Makefile variables for PO directory in any package using GNU gettext.

# Usually the message domain is the same as the package name.
DOMAIN = ipa

# These two variables depend on the location of this directory.
subdir = po
top_builddir = ..

# These options get passed to xgettext.
XGETTEXT_OPTIONS = --from-code="UTF-8" --keyword=_

# This is the copyright holder that gets inserted into the header of the
# $(DOMAIN).pot file.  Set this to the copyright holder of the surrounding
# package.  (Note that the msgstr strings, extracted from the package's
# sources, belong to the copyright holder of the package.)  Translators are
# expected to transfer the copyright for their translations to this person
# or entity, or to disclaim their copyright.  The empty string stands for
# the public domain; in this case the translators are expected to disclaim
# their copyright.
COPYRIGHT_HOLDER = Red Hat

# This tells whether or not to prepend "GNU " prefix to the package
# name that gets inserted into the header of the $(DOMAIN).pot file.
# Possible values are "yes", "no", or empty.  If it is empty, try to
# detect it automatically by scanning the files in $(top_srcdir) for
# "GNU packagename" string.
PACKAGE_GNU = no

# This is the email address or URL to which the translators shall report
# bugs in the untranslated strings:
# - Strings which are not entire sentences, see the maintainer guidelines
#   in the GNU gettext documentation, section 'Preparing Strings'.
# - Strings which use unclear terms or require additional context to be
#   understood.
# - Strings which make invalid assumptions about notation of date, time or
#   money.
# - Pluralisation problems.
# - Incorrect English spelling.
# - Incorrect formatting.
# It can be your email address, or a mailing list address where translators
# can write to without being subscribed, or the URL of a web page through
# which the translators can contact you.
MSGID_BUGS_ADDRESS = https://fedorahosted.org/freeipa/newticket

# This is the list of locale categories, beyond LC_MESSAGES, for which the
# message catalogs shall be used.  It is usually empty.
EXTRA_LOCALE_CATEGORIES =

# This tells whether the $(DOMAIN).pot file contains messages with an 'msgctxt'
# context.  Possible values are "yes" and "no".  Set this to yes if the
# package uses functions taking also a message context, like pgettext(), or
# if in $(XGETTEXT_OPTIONS) you define keywords with a context argument.
USE_MSGCTXT = no

# These options get passed to msgmerge.
# Useful options are in particular:
#   --previous            to keep previous msgids of translated messages,
#   --quiet               to reduce the verbosity.
MSGMERGE_OPTIONS = --no-fuzzy-matching

# These options get passed to msginit.
# If you want to disable line wrapping when writing PO files, add
# --no-wrap to MSGMERGE_OPTIONS, XGETTEXT_OPTIONS, and
# MSGINIT_OPTIONS.
MSGINIT_OPTIONS = --no-translator

# This tells whether or not to regenerate a PO file when $(DOMAIN).pot
# has changed.  Possible values are "yes" and "no".  Set this to no if
# the POT file is checked in the repository and the version control
# program ignores timestamps.

# FreeIPA downloads PO files from Zanata so we do not need to re-generate them.
PO_DEPENDS_ON_POT = no

# This tells whether or not to forcibly update $(DOMAIN).pot and
# regenerate PO files on "make dist".  Possible values are "yes" and
# "no".  Set this to no if the POT file and PO files are maintained
# externally.
DIST_DEPENDS_ON_UPDATE_PO = no

.SUFFIXES:
.SUFFIXES: .po .gmo .mo .sed .sin .nop .po-create .po-update

.po.mo:
	@echo "$(MSGFMT) -c -o $@ $<"; \
	$(MSGFMT) -c -o t-$@ $< && mv t-$@ $@

.po.gmo:
	@lang=`echo $* | sed -e 's,.*/,,'`; \
	test "$(srcdir)" = . && cdcmd="" || cdcmd="cd $(srcdir) && "; \
	echo "$${cdcmd}rm -f $${lang}.gmo && $(GMSGFMT) -c --statistics --verbose -o $${lang}.gmo $${lang}.po"; \
	cd $(srcdir) && rm -f $${lang}.gmo && $(GMSGFMT) -c --statistics --verbose -o t-$${lang}.gmo $${lang}.po && mv t-$${lang}.gmo $${lang}.gmo

.sin.sed:
	sed -e '/^#/d' $< > t-$@
	mv t-$@ $@


all: all-yes

all-yes: stamp-po
all-no:

# Ensure that the gettext macros and this Makefile.in.in are in sync.
CHECK_MACRO_VERSION = \
	test "$(GETTEXT_MACRO_VERSION)" = "0.18" \
	  || { echo "*** error: gettext infrastructure mismatch: using a Makefile.in.in from gettext version $(GETTEXT_MACRO_VERSION) but the autoconf macros are from gettext version 0.18" 1>&2; \
	       exit 1; \
	     }

# $(srcdir)/$(DOMAIN).pot is only created when needed. When xgettext finds no
# internationalized messages, no $(srcdir)/$(DOMAIN).pot is created (because
# we don't want to bother translators with empty POT files). We assume that
# LINGUAS is empty in this case, i.e. $(POFILES) and $(GMOFILES) are empty.
# In this case, stamp-po is a nop (i.e. a phony target).

# stamp-po is a timestamp denoting the last time at which the CATALOGS have
# been loosely updated. Its purpose is that when a developer or translator
# checks out the package via CVS, and the $(DOMAIN).pot file is not in CVS,
# "make" will update the $(DOMAIN).pot and the $(CATALOGS), but subsequent
# invocations of "make" will do nothing. This timestamp would not be necessary
# if updating the $(CATALOGS) would always touch them; however, the rule for
# $(POFILES) has been designed to not touch files that don't need to be
# changed.
stamp-po: $(srcdir)/$(DOMAIN).pot
	@$(CHECK_MACRO_VERSION)
	test ! -f $(srcdir)/$(DOMAIN).pot || \
	  test -z "$(GMOFILES)" || $(MAKE) $(GMOFILES)
	@test ! -f $(srcdir)/$(DOMAIN).pot || { \
	  echo "touch stamp-po" && \
	  echo timestamp > stamp-poT && \
	  mv stamp-poT stamp-po; \
	}

# Note: Target 'all' must not depend on target '$(DOMAIN).pot-update',
# otherwise packages like GCC can not be built if only parts of the source
# have been downloaded.

# This target rebuilds $(DOMAIN).pot; it is an expensive operation.
# Note that $(DOMAIN).pot is not touched if it doesn't need to be changed.
# The determination of whether the package xyz is a GNU one is based on the
# heuristic whether some file in the top level directory mentions "GNU xyz".
# If GNU 'find' is available, we avoid grepping through monster files.
$(DOMAIN).pot-update: $(POTFILES) $(srcdir)/POTFILES.in remove-potcdate.sed
	if { if (LC_ALL=C find --version) 2>/dev/null | grep GNU >/dev/null; then \
	       LC_ALL=C find -L $(top_srcdir) -maxdepth 1 -type f -size -10000000c -exec grep 'GNU freeipa' /dev/null '{}' ';' 2>/dev/null; \
	     else \
	       LC_ALL=C grep 'GNU freeipa' $(top_srcdir)/* 2>/dev/null; \
	     fi; \
	   } | grep -v 'libtool:' >/dev/null; then \
	  package_gnu='GNU '; \
	else \
	  package_gnu=''; \
	fi; \
	if test -n '$(MSGID_BUGS_ADDRESS)' || test '$(PACKAGE_BUGREPORT)' = '@'PACKAGE_BUGREPORT'@'; then \
	  msgid_bugs_address='$(MSGID_BUGS_ADDRESS)'; \
	else \
	  msgid_bugs_address='$(PACKAGE_BUGREPORT)'; \
	fi; \
	case `$(XGETTEXT) --version | sed 1q | sed -e 's,^[^0-9]*,,'` in \
	  '' | 0.[0-9] | 0.[0-9].* | 0.1[0-5] | 0.1[0-5].* | 0.16 | 0.16.[0-1]*) \
	    $(XGETTEXT) --default-domain=$(DOMAIN) --directory=$(top_srcdir) \
	      --add-comments=TRANSLATORS: $(XGETTEXT_OPTIONS)  \
	      --files-from=$(srcdir)/POTFILES.in \
	      --copyright-holder='$(COPYRIGHT_HOLDER)' \
	      --msgid-bugs-address="$$msgid_bugs_address" \
	    ;; \
	  *) \
	    $(XGETTEXT) --default-domain=$(DOMAIN) --directory=$(top_srcdir) \
	      --add-comments=TRANSLATORS: $(XGETTEXT_OPTIONS)  \
	      --files-from=$(srcdir)/POTFILES.in \
	      --copyright-holder='$(COPYRIGHT_HOLDER)' \
	      --package-name="$${package_gnu}freeipa" \
	      --package-version='4.6.90.dev201806272043+gitfb34e05cd' \
	      --msgid-bugs-address="$$msgid_bugs_address" \
	    ;; \
	esac
	test ! -f $(DOMAIN).po || { \
	  if test -f $(srcdir)/$(DOMAIN).pot; then \
	    sed -f remove-potcdate.sed < $(srcdir)/$(DOMAIN).pot > $(DOMAIN).1po && \
	    sed -f remove-potcdate.sed < $(DOMAIN).po > $(DOMAIN).2po && \
	    if cmp $(DOMAIN).1po $(DOMAIN).2po >/dev/null 2>&1; then \
	      rm -f $(DOMAIN).1po $(DOMAIN).2po $(DOMAIN).po; \
	    else \
	      rm -f $(DOMAIN).1po $(DOMAIN).2po $(srcdir)/$(DOMAIN).pot && \
	      mv $(DOMAIN).po $(srcdir)/$(DOMAIN).pot; \
	    fi; \
	  else \
	    mv $(DOMAIN).po $(srcdir)/$(DOMAIN).pot; \
	  fi; \
	}

# This rule has no dependencies: we don't need to update $(DOMAIN).pot at
# every "make" invocation, only create it when it is missing.
# Only "make $(DOMAIN).pot-update" or "make dist" will force an update.
$(srcdir)/$(DOMAIN).pot:
	$(MAKE) $(DOMAIN).pot-update

# This target rebuilds a PO file if $(DOMAIN).pot has changed.
# Note that a PO file is not touched if it doesn't need to be changed.
$(POFILES): $(srcdir)/$(DOMAIN).pot
	@lang=`echo $@ | sed -e 's,.*/,,' -e 's/\.po$$//'`; \
	if test -f "$(srcdir)/$${lang}.po"; then \
	  test "$(srcdir)" = . && cdcmd="" || cdcmd="cd $(srcdir) && "; \
	  echo "$${cdcmd}$(MSGMERGE_UPDATE) $(MSGMERGE_OPTIONS) --lang=$${lang} $${lang}.po $(DOMAIN).pot"; \
	  cd $(srcdir) \
	    && { case `$(MSGMERGE_UPDATE) --version | sed 1q | sed -e 's,^[^0-9]*,,'` in \
	           '' | 0.[0-9] | 0.[0-9].* | 0.1[0-7] | 0.1[0-7].*) \
	             $(MSGMERGE_UPDATE) $(MSGMERGE_OPTIONS) $${lang}.po $(DOMAIN).pot;; \
	           *) \
	             $(MSGMERGE_UPDATE) $(MSGMERGE_OPTIONS) --lang=$${lang} $${lang}.po $(DOMAIN).pot;; \
	         esac; \
	       }; \
	else \
	  $(MAKE) $${lang}.po-create; \
	fi


install: install-exec install-data
install-exec:
install-data: install-data-yes
	if test "$(PACKAGE)" = "gettext-tools"; then \
	  $(mkdir_p) $(DESTDIR)$(gettextsrcdir); \
	  for file in $(DISTFILES.common) Makevars.template; do \
	    $(INSTALL_DATA) $(srcdir)/$$file \
			    $(DESTDIR)$(gettextsrcdir)/$$file; \
	  done; \
	  for file in Makevars; do \
	    rm -f $(DESTDIR)$(gettextsrcdir)/$$file; \
	  done; \
	else \
	  : ; \
	fi
install-data-no: all
install-data-yes: all
	@catalogs='$(CATALOGS)'; \
	for cat in $$catalogs; do \
	  cat=`basename $$cat`; \
	  lang=`echo $$cat | sed -e 's/\.gmo$$//'`; \
	  dir=$(localedir)/$$lang/LC_MESSAGES; \
	  $(mkdir_p) $(DESTDIR)$$dir; \
	  if test -r $$cat; then realcat=$$cat; else realcat=$(srcdir)/$$cat; fi; \
	  $(INSTALL_DATA) $$realcat $(DESTDIR)$$dir/$(DOMAIN).mo; \
	  echo "installing $$realcat as $(DESTDIR)$$dir/$(DOMAIN).mo"; \
	  for lc in '' $(EXTRA_LOCALE_CATEGORIES); do \
	    if test -n "$$lc"; then \
	      if (cd $(DESTDIR)$(localedir)/$$lang && LC_ALL=C ls -l -d $$lc 2>/dev/null) | grep ' -> ' >/dev/null; then \
	        link=`cd $(DESTDIR)$(localedir)/$$lang && LC_ALL=C ls -l -d $$lc | sed -e 's/^.* -> //'`; \
	        mv $(DESTDIR)$(localedir)/$$lang/$$lc $(DESTDIR)$(localedir)/$$lang/$$lc.old; \
	        mkdir $(DESTDIR)$(localedir)/$$lang/$$lc; \
	        (cd $(DESTDIR)$(localedir)/$$lang/$$lc.old && \
	         for file in *; do \
	           if test -f $$file; then \
	             ln -s ../$$link/$$file $(DESTDIR)$(localedir)/$$lang/$$lc/$$file; \
	           fi; \
	         done); \
	        rm -f $(DESTDIR)$(localedir)/$$lang/$$lc.old; \
	      else \
	        if test -d $(DESTDIR)$(localedir)/$$lang/$$lc; then \
	          :; \
	        else \
	          rm -f $(DESTDIR)$(localedir)/$$lang/$$lc; \
	          mkdir $(DESTDIR)$(localedir)/$$lang/$$lc; \
	        fi; \
	      fi; \
	      rm -f $(DESTDIR)$(localedir)/$$lang/$$lc/$(DOMAIN).mo; \
	      ln -s ../LC_MESSAGES/$(DOMAIN).mo $(DESTDIR)$(localedir)/$$lang/$$lc/$(DOMAIN).mo 2>/dev/null || \
	      ln $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/$(DOMAIN).mo $(DESTDIR)$(localedir)/$$lang/$$lc/$(DOMAIN).mo 2>/dev/null || \
	      cp -p $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/$(DOMAIN).mo $(DESTDIR)$(localedir)/$$lang/$$lc/$(DOMAIN).mo; \
	      echo "installing $$realcat link as $(DESTDIR)$(localedir)/$$lang/$$lc/$(DOMAIN).mo"; \
	    fi; \
	  done; \
	done

install-strip: install

installdirs: installdirs-exec installdirs-data
installdirs-exec:
installdirs-data: installdirs-data-yes
	if test "$(PACKAGE)" = "gettext-tools"; then \
	  $(mkdir_p) $(DESTDIR)$(gettextsrcdir); \
	else \
	  : ; \
	fi
installdirs-data-no:
installdirs-data-yes:
	@catalogs='$(CATALOGS)'; \
	for cat in $$catalogs; do \
	  cat=`basename $$cat`; \
	  lang=`echo $$cat | sed -e 's/\.gmo$$//'`; \
	  dir=$(localedir)/$$lang/LC_MESSAGES; \
	  $(mkdir_p) $(DESTDIR)$$dir; \
	  for lc in '' $(EXTRA_LOCALE_CATEGORIES); do \
	    if test -n "$$lc"; then \
	      if (cd $(DESTDIR)$(localedir)/$$lang && LC_ALL=C ls -l -d $$lc 2>/dev/null) | grep ' -> ' >/dev/null; then \
	        link=`cd $(DESTDIR)$(localedir)/$$lang && LC_ALL=C ls -l -d $$lc | sed -e 's/^.* -> //'`; \
	        mv $(DESTDIR)$(localedir)/$$lang/$$lc $(DESTDIR)$(localedir)/$$lang/$$lc.old; \
	        mkdir $(DESTDIR)$(localedir)/$$lang/$$lc; \
	        (cd $(DESTDIR)$(localedir)/$$lang/$$lc.old && \
	         for file in *; do \
	           if test -f $$file; then \
	             ln -s ../$$link/$$file $(DESTDIR)$(localedir)/$$lang/$$lc/$$file; \
	           fi; \
	         done); \
	        rm -f $(DESTDIR)$(localedir)/$$lang/$$lc.old; \
	      else \
	        if test -d $(DESTDIR)$(localedir)/$$lang/$$lc; then \
	          :; \
	        else \
	          rm -f $(DESTDIR)$(localedir)/$$lang/$$lc; \
	          mkdir $(DESTDIR)$(localedir)/$$lang/$$lc; \
	        fi; \
	      fi; \
	    fi; \
	  done; \
	done

# Define this as empty until I found a useful application.
installcheck:

uninstall: uninstall-exec uninstall-data
uninstall-exec:
uninstall-data: uninstall-data-yes
	if test "$(PACKAGE)" = "gettext-tools"; then \
	  for file in $(DISTFILES.common) Makevars.template; do \
	    rm -f $(DESTDIR)$(gettextsrcdir)/$$file; \
	  done; \
	else \
	  : ; \
	fi
uninstall-data-no:
uninstall-data-yes:
	catalogs='$(CATALOGS)'; \
	for cat in $$catalogs; do \
	  cat=`basename $$cat`; \
	  lang=`echo $$cat | sed -e 's/\.gmo$$//'`; \
	  for lc in LC_MESSAGES $(EXTRA_LOCALE_CATEGORIES); do \
	    rm -f $(DESTDIR)$(localedir)/$$lang/$$lc/$(DOMAIN).mo; \
	  done; \
	done

check: all

info dvi ps pdf html tags TAGS ctags CTAGS ID:

mostlyclean:
	rm -f remove-potcdate.sed
	rm -f stamp-poT
	rm -f core core.* $(DOMAIN).po $(DOMAIN).1po $(DOMAIN).2po *.new.po
	rm -fr *.o

clean: mostlyclean

distclean: clean
	rm -f Makefile Makefile.in POTFILES *.mo

maintainer-clean: distclean
	@echo "This command is intended for maintainers to use;"
	@echo "it deletes files that may require special tools to rebuild."
	rm -f stamp-po $(GMOFILES)

distdir = $(top_builddir)/$(PACKAGE)-$(VERSION)/$(subdir)
dist distdir:
	$(MAKE) update-po
	@$(MAKE) dist2
# This is a separate target because 'update-po' must be executed before.
dist2: stamp-po $(DISTFILES)
	dists="$(DISTFILES)"; \
	if test "$(PACKAGE)" = "gettext-tools"; then \
	  dists="$$dists Makevars.template"; \
	fi; \
	if test -f $(srcdir)/$(DOMAIN).pot; then \
	  dists="$$dists $(DOMAIN).pot stamp-po"; \
	fi; \
	if test -f $(srcdir)/ChangeLog; then \
	  dists="$$dists ChangeLog"; \
	fi; \
	for i in 0 1 2 3 4 5 6 7 8 9; do \
	  if test -f $(srcdir)/ChangeLog.$$i; then \
	    dists="$$dists ChangeLog.$$i"; \
	  fi; \
	done; \
	if test -f $(srcdir)/LINGUAS; then dists="$$dists LINGUAS"; fi; \
	for file in $$dists; do \
	  if test -f $$file; then \
	    cp -p $$file $(distdir) || exit 1; \
	  else \
	    cp -p $(srcdir)/$$file $(distdir) || exit 1; \
	  fi; \
	done

update-po: Makefile
	$(MAKE) $(DOMAIN).pot-update
	test -z "$(UPDATEPOFILES)" || $(MAKE) $(UPDATEPOFILES)
	$(MAKE) update-gmo

# General rule for creating PO files.

.nop.po-create:
	@lang=`echo $@ | sed -e 's/\.po-create$$//'`; \
	echo "File $$lang.po does not exist. If you are a translator, you can create it through 'msginit'." 1>&2; \
	exit 1

# General rule for updating PO files.

.nop.po-update:
	@lang=`echo $@ | sed -e 's/\.po-update$$//'`; \
	if test "$(PACKAGE)" = "gettext-tools"; then PATH=`pwd`/../src:$$PATH; fi; \
	tmpdir=`pwd`; \
	echo "$$lang:"; \
	test "$(srcdir)" = . && cdcmd="" || cdcmd="cd $(srcdir) && "; \
	echo "$${cdcmd}$(MSGMERGE) $(MSGMERGE_OPTIONS) --lang=$$lang $$lang.po $(DOMAIN).pot -o $$lang.new.po"; \
	cd $(srcdir); \
	if { case `$(MSGMERGE) --version | sed 1q | sed -e 's,^[^0-9]*,,'` in \
	       '' | 0.[0-9] | 0.[0-9].* | 0.1[0-7] | 0.1[0-7].*) \
	         $(MSGMERGE) $(MSGMERGE_OPTIONS) -o $$tmpdir/$$lang.new.po $$lang.po $(DOMAIN).pot;; \
	       *) \
	         $(MSGMERGE) $(MSGMERGE_OPTIONS) --lang=$$lang -o $$tmpdir/$$lang.new.po $$lang.po $(DOMAIN).pot;; \
	     esac; \
	   }; then \
	  if cmp $$lang.po $$tmpdir/$$lang.new.po >/dev/null 2>&1; then \
	    rm -f $$tmpdir/$$lang.new.po; \
	  else \
	    if mv -f $$tmpdir/$$lang.new.po $$lang.po; then \
	      :; \
	    else \
	      echo "msgmerge for $$lang.po failed: cannot move $$tmpdir/$$lang.new.po to $$lang.po" 1>&2; \
	      exit 1; \
	    fi; \
	  fi; \
	else \
	  echo "msgmerge for $$lang.po failed!" 1>&2; \
	  rm -f $$tmpdir/$$lang.new.po; \
	fi

$(DUMMYPOFILES):

update-gmo: Makefile $(GMOFILES)
	@:

# Recreate Makefile by invoking config.status. Explicitly invoke the shell,
# because execution permission bits may not work on the current file system.
# Use /bin/sh, which is the shell determined by autoconf for the use by its
# scripts, not $(SHELL) which is hardwired to /bin/sh and may be deficient.
Makefile: Makefile.in.in Makevars $(top_builddir)/config.status POTFILES.in LINGUAS
	cd $(top_builddir) \
	  && /bin/sh ./config.status $(subdir)/$@.in po-directories

force:

# Tell versions [3.59,3.63) of GNU make not to export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
# Special Makefile rules for English message catalogs with quotation marks.

DISTFILES.common.extra1 = quot.sed boldquot.sed en@quot.header en@boldquot.header insert-header.sin Rules-quot

.SUFFIXES: .insert-header .po-update-en

en@quot.po-create:
	$(MAKE) en@quot.po-update
en@boldquot.po-create:
	$(MAKE) en@boldquot.po-update

en@quot.po-update: en@quot.po-update-en
en@boldquot.po-update: en@boldquot.po-update-en

.insert-header.po-update-en:
	@lang=`echo $@ | sed -e 's/\.po-update-en$$//'`; \
	if test "$(PACKAGE)" = "gettext-tools"; then PATH=`pwd`/../src:$$PATH; GETTEXTLIBDIR=`cd $(top_srcdir)/src && pwd`; export GETTEXTLIBDIR; fi; \
	tmpdir=`pwd`; \
	echo "$$lang:"; \
	ll=`echo $$lang | sed -e 's/@.*//'`; \
	LC_ALL=C; export LC_ALL; \
	cd $(srcdir); \
	if $(MSGINIT) -i $(DOMAIN).pot --no-translator -l $$lang -o - 2>/dev/null | sed -f $$tmpdir/$$lang.insert-header | $(MSGCONV) -t UTF-8 | $(MSGFILTER) sed -f `echo $$lang | sed -e 's/.*@//'`.sed 2>/dev/null > $$tmpdir/$$lang.new.po; then \
	  if cmp $$lang.po $$tmpdir/$$lang.new.po >/dev/null 2>&1; then \
	    rm -f $$tmpdir/$$lang.new.po; \
	  else \
	    if mv -f $$tmpdir/$$lang.new.po $$lang.po; then \
	      :; \
	    else \
	      echo "creation of $$lang.po failed: cannot move $$tmpdir/$$lang.new.po to $$lang.po" 1>&2; \
	      exit 1; \
	    fi; \
	  fi; \
	else \
	  echo "creation of $$lang.po failed!" 1>&2; \
	  rm -f $$tmpdir/$$lang.new.po; \
	fi

en@quot.insert-header: insert-header.sin
	sed -e '/^#/d' -e 's/HEADER/en@quot.header/g' $(srcdir)/insert-header.sin > en@quot.insert-header

en@boldquot.insert-header: insert-header.sin
	sed -e '/^#/d' -e 's/HEADER/en@boldquot.header/g' $(srcdir)/insert-header.sin > en@boldquot.insert-header

mostlyclean: mostlyclean-quot
mostlyclean-quot:
	rm -f *.insert-header
include Makefile.hack
