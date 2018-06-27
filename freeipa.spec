# Define ONLY_CLIENT to only make the ipa-client and ipa-python
# subpackages
%{!?ONLY_CLIENT:%global ONLY_CLIENT 0}
%if %{ONLY_CLIENT}
    %global enable_server_option --disable-server
%else
    %global enable_server_option --enable-server
%endif

# Build with ipatests
%if ! %{ONLY_CLIENT}
    %global with_ipatests 1
%endif
%if 0%{?with_ipatests}
    %global with_ipatests_option --with-ipatests
%else
    %global with_ipatests_option --without-ipatests
%endif

%if 0%{!?with_python3:1}
%if 0%{?rhel}
%global with_python3 0
%else
%global with_python3 1
%endif
%endif

# lint is not executed during rpmbuild
# %%global with_lint 1
%if 0%{?with_lint}
    %global linter_options --enable-pylint --with-jslint
%else
    %global linter_options --disable-pylint --without-jslint
%endif

%global alt_name ipa
%if 0%{?rhel}
# 1.15.1-7: certauth (http://krbdev.mit.edu/rt/Ticket/Display.html?id=8561)
%global krb5_version 1.15.1-4
# 0.7.16: https://github.com/drkjam/netaddr/issues/71
%global python_netaddr_version 0.7.5-8
# Require 4.6.0-4 which brings RC4 for FIPS + trust fixes to priv. separation
%global samba_version 4.6.0-4
%global selinux_policy_version 3.12.1-153
%global slapi_nis_version 0.56.0-4
%else
# 1.15.1-7: certauth (http://krbdev.mit.edu/rt/Ticket/Display.html?id=8561)
%global krb5_version 1.15.1-7
# 0.7.16: https://github.com/drkjam/netaddr/issues/71
%global python_netaddr_version 0.7.16
# Require 4.6.0-4 which brings RC4 for FIPS + trust fixes to priv. separation
%global samba_version 2:4.6.0-4
%global selinux_policy_version 3.13.1-158.4
%global slapi_nis_version 0.56.1
%endif

%define krb5_base_version %(LC_ALL=C rpm -q --qf '%%{VERSION}' krb5-devel | grep -Eo '^[^.]+\.[^.]+')

%global plugin_dir %{_libdir}/dirsrv/plugins
%global etc_systemd_dir %{_sysconfdir}/systemd/system
%global gettext_domain ipa

%define _hardened_build 1

# Work-around fact that RPM SPEC parser does not accept
# "Version: 4.6.90.dev201806272025+git7c2dba191" in freeipa.spec.in used for Autoconf string replacement
%define IPA_VERSION 4.6.90.dev201806272025+git7c2dba191
%define AT_SIGN @
# redefine IPA_VERSION only if its value matches the Autoconf placeholder
%if "%{IPA_VERSION}" == "%{AT_SIGN}VERSION%{AT_SIGN}"
	%define IPA_VERSION nonsense.to.please.RPM.SPEC.parser
%endif

Name:           freeipa
Version:        %{IPA_VERSION}
Release:        0%{?dist}
Summary:        The Identity, Policy and Audit system

Group:          System Environment/Base
License:        GPLv3+
URL:            http://www.freeipa.org/
Source0:        freeipa-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  openldap-devel
# For KDB DAL version, make explicit dependency so that increase of version
# will cause the build to fail due to unsatisfied dependencies.
# DAL version change may cause code crash or memory leaks, it is better to fail early.
%if 0%{?fedora} > 25
BuildRequires: krb5-kdb-version = 6.1
%endif
BuildRequires:  krb5-devel >= %{krb5_version}
# 1.27.4: xmlrpc_curl_xportparms.gssapi_delegation
BuildRequires:  xmlrpc-c-devel >= 1.27.4
BuildRequires:  popt-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif # with_python3
# %{_unitdir}, %{_tmpfilesdir}
BuildRequires:  systemd
# systemd-tmpfiles which is executed from make install requires apache user
BuildRequires:  httpd
BuildRequires:  nspr-devel
BuildRequires:  nss-devel
BuildRequires:  openssl-devel
BuildRequires:  libini_config-devel
BuildRequires:  cyrus-sasl-devel
%if ! %{ONLY_CLIENT}
# 1.3.3.9: DS_Sleep (https://fedorahosted.org/389/ticket/48005)
BuildRequires:  389-ds-base-devel >= 1.3.3.9
BuildRequires:  svrcore-devel
%if 0%{?rhel}
BuildRequires:  samba-devel >= 4.0.0
%else
BuildRequires:  samba-devel >= 2:4.0.0
%endif
BuildRequires:  libtalloc-devel
BuildRequires:  libtevent-devel
BuildRequires:  libuuid-devel
BuildRequires:  libsss_idmap-devel
BuildRequires:  libsss_certmap-devel
# 1.15.3: sss_nss_getlistbycert (https://pagure.io/SSSD/sssd/issue/3050)
BuildRequires:  libsss_nss_idmap-devel >= 1.15.3
BuildRequires:  rhino
BuildRequires:  libverto-devel
BuildRequires:  libunistring-devel
BuildRequires:  python-lesscpy
%endif # ONLY_CLIENT

#
# Build dependencies for makeapi/makeaci
# makeapi/makeaci is using Python 2 only for now
#
BuildRequires:  python-ldap
BuildRequires:  python-netaddr
BuildRequires:  python2-pyasn1
BuildRequires:  python2-pyasn1-modules
BuildRequires:  python2-dns
BuildRequires:  python-six
BuildRequires:  python2-libsss_nss_idmap
BuildRequires:  python2-cffi

#
# Build dependencies for wheel packaging and PyPI upload
#
%if 0%{?with_wheels}
BuildRequires:  dbus-glib-devel
BuildRequires:  libffi-devel
BuildRequires:  python2-tox
BuildRequires:  python2-twine
BuildRequires:  python2-wheel
%if 0%{?with_python3}
BuildRequires:  python3-tox
BuildRequires:  python3-twine
BuildRequires:  python3-wheel
%endif
%endif # with_wheels

#
# Build dependencies for lint
#
%if 0%{?with_lint}
BuildRequires:  samba-python
# 1.6: x509.Name.rdns (https://github.com/pyca/cryptography/issues/3199)
BuildRequires:  python2-cryptography >= 1.6
BuildRequires:  python-gssapi >= 1.2.0-5
%if 0%{?fedora} >= 26
BuildRequires:  python2-pylint
%else
BuildRequires:  pylint >= 1.7
%endif
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1096506
BuildRequires:  python2-polib
BuildRequires:  python2-libipa_hbac
BuildRequires:  python2-lxml
# 5.0.0: QRCode.print_ascii
BuildRequires:  python-qrcode-core >= 5.0.0
# 1.15: python-dns changed return type in to_text() method in PY3
BuildRequires:  python2-dns >= 1.15
BuildRequires:  jsl
BuildRequires:  python2-yubico
# pki Python package
BuildRequires:  pki-base-python2
BuildRequires:  python-pytest-multihost
BuildRequires:  python-pytest-sourceorder
# 0.4.2: Py3 fix https://bugzilla.redhat.com/show_bug.cgi?id=1476150
BuildRequires:  python-jwcrypto >= 0.4.2
# 0.3: sd_notify (https://pagure.io/freeipa/issue/5825)
BuildRequires:  python2-custodia >= 0.3.1
BuildRequires:  dbus-python
BuildRequires:  python2-dateutil
BuildRequires:  python-enum34
BuildRequires:  python-netifaces
BuildRequires:  python2-sss
BuildRequires:  python2-sss-murmur
BuildRequires:  python2-sssdconfig
BuildRequires:  python2-nose
BuildRequires:  python2-paste
BuildRequires:  systemd-python
BuildRequires:  python2-jinja2
BuildRequires:  python2-augeas

%if 0%{?with_python3}
# FIXME: this depedency is missing - server will not work
#BuildRequires:  python3-samba
# 1.6: x509.Name.rdns (https://github.com/pyca/cryptography/issues/3199)
BuildRequires:  python3-cryptography >= 1.6
BuildRequires:  python3-gssapi >= 1.2.0
BuildRequires:  python3-pylint >= 1.7
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1096506
BuildRequires:  python3-polib
BuildRequires:  python3-libipa_hbac
BuildRequires:  python3-memcached
BuildRequires:  python3-lxml
# 5.0.0: QRCode.print_ascii
BuildRequires:  python3-qrcode-core >= 5.0.0
# 1.15: python-dns changed return type in to_text() method in PY3
BuildRequires:  python3-dns >= 1.15
BuildRequires:  python3-yubico
# pki Python package
BuildRequires:  pki-base-python3
BuildRequires:  python3-pytest-multihost
BuildRequires:  python3-pytest-sourceorder
# 0.4.2: Py3 fix https://bugzilla.redhat.com/show_bug.cgi?id=1476150
BuildRequires:  python3-jwcrypto >= 0.4.2
# 0.3: sd_notify (https://pagure.io/freeipa/issue/5825)
BuildRequires:  python3-custodia >= 0.3.1
BuildRequires:  python3-dbus
BuildRequires:  python3-dateutil
BuildRequires:  python3-enum34
BuildRequires:  python3-netifaces
BuildRequires:  python3-sss
BuildRequires:  python3-sss-murmur
BuildRequires:  python3-sssdconfig
BuildRequires:  python3-libsss_nss_idmap
BuildRequires:  python3-nose
BuildRequires:  python3-paste
BuildRequires:  python3-systemd
BuildRequires:  python3-jinja2
BuildRequires:  python3-augeas
BuildRequires:  python3-netaddr
BuildRequires:  python3-pyasn1
BuildRequires:  python3-pyasn1-modules
BuildRequires:  python3-pyldap
%endif # with_python3
%endif # with_lint

#
# Build dependencies for unit tests
#
%if ! %{ONLY_CLIENT}
BuildRequires:  libcmocka-devel
BuildRequires:  nss_wrapper
# Required by ipa_kdb_tests
BuildRequires:  %{_libdir}/krb5/plugins/kdb/db2.so
%endif # ONLY_CLIENT

%description
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).


%if ! %{ONLY_CLIENT}

%package server
Summary: The IPA authentication server
Group: System Environment/Base
Requires: %{name}-server-common = %{version}-%{release}
Requires: %{name}-client = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
%if 0%{?with_python3}
Requires: python3-ipaserver = %{version}-%{release}
%else
Requires: python2-ipaserver = %{version}-%{release}
%endif
Requires: 389-ds-base >= 1.3.5.14
Requires: openldap-clients > 2.4.35-4
Requires: nss >= 3.14.3-12.0
Requires: nss-tools >= 3.14.3-12.0
Requires(post): krb5-server >= %{krb5_version}
Requires(post): krb5-server >= %{krb5_base_version}, krb5-server < %{krb5_base_version}.100
Requires: krb5-pkinit-openssl >= %{krb5_version}
Requires: cyrus-sasl-gssapi%{?_isa}
Requires: ntp
Requires: httpd >= 2.4.6-31
%if 0%{with_python3}
Requires: python3-mod_wsgi
%else
Requires: mod_wsgi
%endif
Requires: mod_auth_gssapi >= 1.5.0
# 1.0.14-3: https://bugzilla.redhat.com/show_bug.cgi?id=1431206
Requires: mod_nss >= 1.0.14-3
Requires: mod_session
# 0.9.9: https://github.com/adelton/mod_lookup_identity/pull/3
Requires: mod_lookup_identity >= 0.9.9
Requires: python-ldap >= 2.4.15
Requires: python-gssapi >= 1.2.0-5
Requires: acl
Requires: systemd-units >= 38
Requires(pre): shadow-utils
Requires(pre): systemd-units
Requires(post): systemd-units
Requires: selinux-policy >= %{selinux_policy_version}
Requires(post): selinux-policy-base >= %{selinux_policy_version}
Requires: slapi-nis >= %{slapi_nis_version}
Requires: pki-ca >= 10.4.0-1
Requires: pki-kra >= 10.4.0-1
Requires(preun): python systemd-units
Requires(postun): python systemd-units
Requires: policycoreutils >= 2.1.12-5
Requires: tar
# certmonger-0.79.4-2 fixes newlines in PEM files
Requires(pre): certmonger >= 0.79.4-2
Requires(pre): 389-ds-base >= 1.3.5.14
Requires: fontawesome-fonts
Requires: open-sans-fonts
Requires: openssl
Requires: softhsm >= 2.0.0rc1-1
Requires: p11-kit
Requires: systemd-python
Requires: %{etc_systemd_dir}
Requires: gzip
Requires: oddjob
# 0.7.0-2: https://pagure.io/gssproxy/pull-request/172
Requires: gssproxy >= 0.7.0-2
# 1.15.2: FindByNameAndCertificate (https://pagure.io/SSSD/sssd/issue/3050)
Requires: sssd-dbus >= 1.15.2

Provides: %{alt_name}-server = %{version}
Conflicts: %{alt_name}-server
Obsoletes: %{alt_name}-server < %{version}

# With FreeIPA 3.3, package freeipa-server-selinux was obsoleted as the
# entire SELinux policy is stored in the system policy
Obsoletes: freeipa-server-selinux < 3.3.0

# upgrade path from monolithic -server to -server + -server-dns
Obsoletes: %{name}-server <= 4.2.0

# Versions of nss-pam-ldapd < 0.8.4 require a mapping from uniqueMember to
# member.
Conflicts: nss-pam-ldapd < 0.8.4

%description server
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.


%package -n python2-ipaserver
Summary: Python libraries used by IPA server
Group: System Environment/Libraries
BuildArch: noarch
%{?python_provide:%python_provide python2-ipaserver}
%{!?python_provide:Provides: python-ipaserver = %{version}-%{release}}
Requires: %{name}-server-common = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
Requires: python2-ipaclient = %{version}-%{release}
Requires: python2-custodia >= 0.3.1
Requires: python-ldap >= 2.4.15
Requires: python2-lxml
Requires: python-gssapi >= 1.2.0-5
Requires: python2-sssdconfig
Requires: python2-pyasn1
Requires: dbus-python
Requires: python2-dns >= 1.15
Requires: python-kdcproxy >= 0.3
Requires: rpm-libs
Requires: pki-base-python2
Requires: python2-augeas

%description -n python2-ipaserver
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.


%if 0%{?with_python3}

%package -n python3-ipaserver
Summary: Python libraries used by IPA server
Group: System Environment/Libraries
BuildArch: noarch
%{?python_provide:%python_provide python3-ipaserver}
Requires: %{name}-server-common = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
Requires: python3-ipaclient = %{version}-%{release}
Requires: python3-custodia >= 0.3.1
# we need pre-requires since earlier versions may break upgrade
Requires(pre): python3-pyldap >= 2.4.35.1-2
Requires: python3-lxml
Requires: python3-gssapi >= 1.2.0
Requires: python3-sssdconfig
Requires: python3-pyasn1
Requires: python3-dbus
Requires: python3-dns >= 1.15
Requires: python3-kdcproxy >= 0.3
Requires: python3-augeas
Requires: rpm-libs
Requires: pki-base-python3

%description -n python3-ipaserver
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.

%endif  # with_python3


%package server-common
Summary: Common files used by IPA server
Group: System Environment/Base
BuildArch: noarch
Requires: %{name}-client-common = %{version}-%{release}
Requires: httpd >= 2.4.6-31
Requires: systemd-units >= 38
Requires: custodia >= 0.3.1

Provides: %{alt_name}-server-common = %{version}
Conflicts: %{alt_name}-server-common
Obsoletes: %{alt_name}-server-common < %{version}

%description server-common
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.


%package server-dns
Summary: IPA integrated DNS server with support for automatic DNSSEC signing
Group: System Environment/Base
BuildArch: noarch
Requires: %{name}-server = %{version}-%{release}
Requires: bind-dyndb-ldap >= 11.0-2
Requires: bind >= 9.11.0-6.P2
Requires: bind-utils >= 9.11.0-6.P2
Requires: bind-pkcs11 >= 9.11.0-6.P2
Requires: bind-pkcs11-utils >= 9.11.0-6.P2
Requires: opendnssec >= 1.4.6-4
# Keep python2 dependencies until DNSSEC daemons are ported to Python 3
Requires: python2
Requires: python2-ipalib
Requires: python2-ipaserver

Provides: %{alt_name}-server-dns = %{version}
Conflicts: %{alt_name}-server-dns
Obsoletes: %{alt_name}-server-dns < %{version}

# upgrade path from monolithic -server to -server + -server-dns
Obsoletes: %{name}-server <= 4.2.0

%description server-dns
IPA integrated DNS server with support for automatic DNSSEC signing.
Integrated DNS server is BIND 9. OpenDNSSEC provides key management.


%package server-trust-ad
Summary: Virtual package to install packages required for Active Directory trusts
Group: System Environment/Base
Requires: %{name}-server = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
Requires: samba-python
Requires: samba >= %{samba_version}
Requires: samba-winbind
Requires: libsss_idmap
Requires: python-libsss_nss_idmap
Requires: python-sss
# We use alternatives to divert winbind_krb5_locator.so plugin to libkrb5
# on the installes where server-trust-ad subpackage is installed because
# IPA AD trusts cannot be used at the same time with the locator plugin
# since Winbindd will be configured in a different mode
Requires(post): %{_sbindir}/update-alternatives
Requires(post): python
Requires(postun): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

Provides: %{alt_name}-server-trust-ad = %{version}
Conflicts: %{alt_name}-server-trust-ad
Obsoletes: %{alt_name}-server-trust-ad < %{version}

%description server-trust-ad
Cross-realm trusts with Active Directory in IPA require working Samba 4
installation. This package is provided for convenience to install all required
dependencies at once.

%endif # ONLY_CLIENT


%package client
Summary: IPA authentication for use on clients
Group: System Environment/Base
Requires: %{name}-client-common = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
%if 0%{?with_python3}
Requires: python3-ipaclient = %{version}-%{release}
%else
Requires: python2-ipaclient = %{version}-%{release}
%endif
Requires: python-ldap
Requires: cyrus-sasl-gssapi%{?_isa}
Requires: ntp
Requires: krb5-workstation >= %{krb5_version}
Requires: authconfig
Requires: curl
# NIS domain name config: /usr/lib/systemd/system/*-domainname.service
Requires: initscripts
Requires: libcurl >= 7.21.7-2
Requires: xmlrpc-c >= 1.27.4
Requires: sssd >= 1.14.0
Requires: python-sssdconfig
# certmonger-0.79.4-2 fixes newlines in PEM files
Requires: certmonger >= 0.79.4-2
Requires: nss-tools
Requires: bind-utils
Requires: oddjob-mkhomedir
Requires: python-gssapi >= 1.2.0-5
Requires: libsss_autofs
Requires: autofs
Requires: libnfsidmap
Requires: nfs-utils
Requires(post): policycoreutils

Provides: %{alt_name}-client = %{version}
Conflicts: %{alt_name}-client
Obsoletes: %{alt_name}-client < %{version}

Provides: %{alt_name}-admintools = %{version}
Conflicts: %{alt_name}-admintools
Obsoletes: %{alt_name}-admintools < 4.4.1

Obsoletes: %{name}-admintools < 4.4.1
Provides: %{name}-admintools = %{version}-%{release}

%description client
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.
This package provides command-line tools for IPA administrators.


%package -n python2-ipaclient
Summary: Python libraries used by IPA client
Group: System Environment/Libraries
BuildArch: noarch
%{?python_provide:%python_provide python2-ipaclient}
%{!?python_provide:Provides: python-ipaclient = %{version}-%{release}}
Requires: %{name}-client-common = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
Requires: python2-ipalib = %{version}-%{release}
Requires: python2-dns >= 1.15
Requires: python2-jinja2

%description -n python2-ipaclient
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.


%if 0%{?with_python3}

%package -n python3-ipaclient
Summary: Python libraries used by IPA client
Group: System Environment/Libraries
BuildArch: noarch
%{?python_provide:%python_provide python3-ipaclient}
Requires: %{name}-client-common = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
Requires: python3-ipalib = %{version}-%{release}
Requires: python3-dns >= 1.15
Requires: python3-jinja2

%description -n python3-ipaclient
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.

%endif  # with_python3


%package client-common
Summary: Common files used by IPA client
Group: System Environment/Base
BuildArch: noarch

Provides: %{alt_name}-client-common = %{version}
Conflicts: %{alt_name}-client-common
Obsoletes: %{alt_name}-client-common < %{version}

%description client-common
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.


%package python-compat
Summary: Compatiblity package for Python libraries used by IPA
Group: System Environment/Libraries
BuildArch: noarch
Obsoletes: %{name}-python < 4.2.91
Provides: %{name}-python = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
%if 0%{?with_python3}
Requires: python3-ipalib = %{version}-%{release}
%else
Requires: python2-ipalib = %{version}-%{release}
%endif

Provides: %{alt_name}-python-compat = %{version}
Conflicts: %{alt_name}-python-compat
Obsoletes: %{alt_name}-python-compat < %{version}

Obsoletes: %{alt_name}-python < 4.2.91
Provides: %{alt_name}-python = %{version}

%description python-compat
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
This is a compatibility package to accommodate %{name}-python split into
python2-ipalib and %{name}-common. Packages still depending on
%{name}-python should be fixed to depend on python2-ipaclient or
%{name}-common instead.


%package -n python2-ipalib
Summary: Python libraries used by IPA
Group: System Environment/Libraries
BuildArch: noarch
Conflicts: %{name}-python < 4.2.91
%{?python_provide:%python_provide python2-ipalib}
%{!?python_provide:Provides: python-ipalib = %{version}-%{release}}
Provides: python2-ipapython = %{version}-%{release}
%{?python_provide:%python_provide python2-ipapython}
%{!?python_provide:Provides: python-ipapython = %{version}-%{release}}
Provides: python2-ipaplatform = %{version}-%{release}
%{?python_provide:%python_provide python2-ipaplatform}
%{!?python_provide:Provides: python-ipaplatform = %{version}-%{release}}
Requires: %{name}-common = %{version}-%{release}
Requires: python-gssapi >= 1.2.0-5
Requires: gnupg
Requires: keyutils
Requires: pyOpenSSL
Requires: python >= 2.7.9
Requires: python2-cryptography >= 1.6
Requires: python-netaddr >= %{python_netaddr_version}
Requires: python2-libipa_hbac
Requires: python-qrcode-core >= 5.0.0
Requires: python2-pyasn1
Requires: python2-pyasn1-modules
Requires: python2-dateutil
Requires: python2-yubico >= 1.2.3
Requires: python2-sss-murmur
Requires: dbus-python
Requires: python2-setuptools
Requires: python-six
# 0.4.2: Py3 fix https://bugzilla.redhat.com/show_bug.cgi?id=1476150
Requires: python-jwcrypto >= 0.4.2
Requires: python2-cffi
Requires: python-ldap >= 2.4.15
Requires: python2-requests
Requires: python2-dns >= 1.15
Requires: python-enum34
Requires: python-netifaces >= 0.10.4
Requires: pyusb

Conflicts: %{alt_name}-python < %{version}

%description -n python2-ipalib
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are using IPA, you need to install this package.


%if 0%{?with_python3}

%package -n python3-ipalib
Summary: Python3 libraries used by IPA
Group: System Environment/Libraries
BuildArch: noarch
%{?python_provide:%python_provide python3-ipalib}
Provides: python3-ipapython = %{version}-%{release}
%{?python_provide:%python_provide python3-ipapython}
Provides: python3-ipaplatform = %{version}-%{release}
%{?python_provide:%python_provide python3-ipaplatform}
Requires: %{name}-common = %{version}-%{release}
Requires: python3-gssapi >= 1.2.0
Requires: gnupg
Requires: keyutils
Requires: python3-pyOpenSSL
Requires: python3-cryptography >= 1.6
Requires: python3-netaddr >= %{python_netaddr_version}
Requires: python3-libipa_hbac
Requires: python3-qrcode-core >= 5.0.0
Requires: python3-pyasn1
Requires: python3-pyasn1-modules
Requires: python3-dateutil
# fixes searching for yubikeys in python3
Requires: python3-yubico >= 1.3.2-7
Requires: python3-sss-murmur
Requires: python3-dbus
Requires: python3-setuptools
Requires: python3-six
# 0.4.2: Py3 fix https://bugzilla.redhat.com/show_bug.cgi?id=1476150
Requires: python3-jwcrypto >= 0.4.2
Requires: python3-cffi
# we need pre-requires since earlier versions may break upgrade
Requires(pre): python3-pyldap >= 2.4.35.1-2
Requires: python3-requests
Requires: python3-dns >= 1.15
Requires: python3-netifaces >= 0.10.4
Requires: python3-pyusb

%description -n python3-ipalib
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are using IPA with Python 3, you need to install this package.

%endif # with_python3


%package common
Summary: Common files used by IPA
Group: System Environment/Libraries
BuildArch: noarch
Conflicts: %{name}-python < 4.2.91

Provides: %{alt_name}-common = %{version}
Conflicts: %{alt_name}-common
Obsoletes: %{alt_name}-common < %{version}

Conflicts: %{alt_name}-python < %{version}

%description common
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are using IPA, you need to install this package.


%if 0%{?with_ipatests}

%package -n python2-ipatests
Summary: IPA tests and test tools
BuildArch: noarch
Obsoletes: %{name}-tests < 4.2.91
Provides: %{name}-tests = %{version}-%{release}
%{?python_provide:%python_provide python2-ipatests}
%{!?python_provide:Provides: python-ipatests = %{version}-%{release}}
Requires: python2-ipaclient = %{version}-%{release}
Requires: python2-ipaserver = %{version}-%{release}
Requires: tar
Requires: xz
Requires: python2-nose
Requires: pytest >= 2.6
Requires: python2-paste
Requires: python2-coverage
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1096506
Requires: python2-polib
Requires: python-pytest-multihost >= 0.5
Requires: python-pytest-sourceorder
Requires: ldns-utils
Requires: python2-sssdconfig
Requires: python2-cryptography >= 1.6
Requires: iptables

Provides: %{alt_name}-tests = %{version}
Conflicts: %{alt_name}-tests
Obsoletes: %{alt_name}-tests < %{version}

%description -n python2-ipatests
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
This package contains tests that verify IPA functionality.


%if 0%{?with_python3}

%package -n python3-ipatests
Summary: IPA tests and test tools
BuildArch: noarch
%{?python_provide:%python_provide python3-ipatests}
Requires: python3-ipaclient = %{version}-%{release}
Requires: python3-ipaserver = %{version}-%{release}
Requires: tar
Requires: xz
Requires: python3-nose
Requires: python3-pytest >= 2.6
Requires: python3-coverage
Requires: python3-polib
Requires: python3-pytest-multihost >= 0.5
Requires: python3-pytest-sourceorder
Requires: ldns-utils
Requires: python3-sssdconfig
Requires: python3-cryptography >= 1.6
Requires: iptables

%description -n python3-ipatests
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
This package contains tests that verify IPA functionality under Python 3.

%endif # with_python3

%endif # with_ipatests


%prep
%setup -n freeipa-%{version} -q
%if 0%{?with_python3}
# Workaround: We want to build Python things twice. To be sure we do not mess
# up something, do two separate builds in separate directories.
cp -r %{_builddir}/freeipa-%{version} %{_builddir}/freeipa-%{version}-python3
%endif # with_python3


%build
# UI compilation segfaulted on some arches when the stack was lower (#1040576)
export JAVA_STACK_SIZE="8m"
# PATH is workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1005235
export PATH=/usr/bin:/usr/sbin:$PATH
export PYTHON=%{__python2}
# Workaround: make sure all shebangs are pointing to Python 2
# This should be solved properly using setuptools
# and this hack should be removed.
find \
	! -name '*.pyc' -a \
	! -name '*.pyo' -a \
	-type f -exec grep -qsm1 '^#!.*\bpython' {} \; \
	-exec sed -i -e '1 s|^#!.*\bpython[^ ]*|#!%{__python2}|' {} \;

%if 0%{?with_python3}
# TODO: temporary solution until all scripts are ported to python3,
# TODO: workaround: some scripts are copied over, so the are always py2.
# We have to explicitly set python3 here for ported files here
PY3_SUBST_PATHS='
client/ipa-certupdate
client/ipa-client-automount
client/ipa-client-install
daemons/ipa-otpd/test.py
install/certmonger/ipa-server-guard
install/certmonger/dogtag-ipa-ca-renew-agent-submit
install/oddjob/com.redhat.idm.trust-fetch-domains
install/restart_scripts/renew_ra_cert_pre
install/restart_scripts/renew_ca_cert
install/restart_scripts/renew_ra_cert
install/restart_scripts/restart_httpd
install/restart_scripts/renew_kdc_cert
install/restart_scripts/stop_pkicad
install/restart_scripts/restart_dirsrv
install/tools/ipa-advise
install/tools/ipa-adtrust-install
install/tools/ipa-backup
install/tools/ipa-ca-install
install/tools/ipa-cacert-manage
install/tools/ipa-compat-manage
install/tools/ipa-csreplica-manage
install/tools/ipa-custodia
install/tools/ipa-dns-install
install/tools/ipa-httpd-kdcproxy
install/tools/ipa-kra-install
install/tools/ipa-ldap-updater
install/tools/ipa-managed-entries
install/tools/ipa-nis-manage
install/tools/ipa-otptoken-import
install/tools/ipa-pkinit-manage
install/tools/ipa-pki-retrieve-key
install/tools/ipa-replica-conncheck
install/tools/ipa-replica-install
install/tools/ipa-replica-manage
install/tools/ipa-replica-prepare
install/tools/ipa-restore
install/tools/ipa-server-certinstall
install/tools/ipa-server-install
install/tools/ipa-server-upgrade
install/tools/ipa-winsync-migrate
install/tools/ipactl
ipa
'
for P in $PY3_SUBST_PATHS; do
    sed -i -e '1 s|^#!\s\?.*\bpython[0-9]*|#!%{__python3}|' $P
done;

%endif # with_python3

%configure --with-vendor-suffix=-%{release} \
           %{enable_server_option} \
           %{with_ipatests_option} \
           %{linter_options}

# -Onone is workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1398405
%make_build -Onone

%if 0%{?with_python3}
pushd %{_builddir}/freeipa-%{version}-python3
export PYTHON=%{__python3}
# Workaround: make sure all shebangs are pointing to Python 3
# This should be solved properly using setuptools
# and this hack should be removed.
find \
	! -name '*.pyc' -a \
	! -name '*.pyo' -a \
	-type f -exec grep -qsm1 '^#!.*\bpython' {} \; \
	-exec sed -i -e '1 s|^#!.*\bpython[^ ]*|#!%{__python3}|' {} \;
%configure --with-vendor-suffix=-%{release} \
           %{enable_server_option} \
           %{with_ipatests_option} \
           %{linter_options}
popd
%endif # with_python3

%check
make %{?_smp_mflags} check VERBOSE=yes LIBDIR=%{_libdir}


%install
# Please put as much logic as possible into make install. It allows:
# - easier porting to other distributions
# - rapid devel & install cycle using make install
#   (instead of full RPM build and installation each time)
#
# All files and directories created by spec install should be marked as ghost.
# (These are typically configuration files created by IPA installer.)
# All other artifacts should be created by make install.
#
# Exception to this rule are test programs which where want to install
# Python2/3 versions at the same time so we need to rename them. Yuck.

%if 0%{?with_python3}
# Python 3 installation needs to be done first. Subsequent Python 2 install
# will overwrite /usr/bin/ipa and other scripts with variants using
# python2 shebang.
pushd %{_builddir}/freeipa-%{version}-python3
(cd ipaclient && %make_install)
(cd ipalib && %make_install)
(cd ipaplatform && %make_install)
(cd ipapython && %make_install)
%if ! %{ONLY_CLIENT}
(cd ipaserver && %make_install)
%endif # ONLY_CLIENT
%if 0%{?with_ipatests}
(cd ipatests && %make_install)
%endif # with_ipatests
popd

%if 0%{?with_ipatests}
mv %{buildroot}%{_bindir}/ipa-run-tests %{buildroot}%{_bindir}/ipa-run-tests-%{python3_version}
mv %{buildroot}%{_bindir}/ipa-test-config %{buildroot}%{_bindir}/ipa-test-config-%{python3_version}
mv %{buildroot}%{_bindir}/ipa-test-task %{buildroot}%{_bindir}/ipa-test-task-%{python3_version}
ln -s %{_bindir}/ipa-run-tests-%{python3_version} %{buildroot}%{_bindir}/ipa-run-tests-3
ln -s %{_bindir}/ipa-test-config-%{python3_version} %{buildroot}%{_bindir}/ipa-test-config-3
ln -s %{_bindir}/ipa-test-task-%{python3_version} %{buildroot}%{_bindir}/ipa-test-task-3
%endif # with_ipatests

%endif # with_python3

# Python 2 installation
%make_install

%if 0%{?with_ipatests}
mv %{buildroot}%{_bindir}/ipa-run-tests %{buildroot}%{_bindir}/ipa-run-tests-%{python2_version}
mv %{buildroot}%{_bindir}/ipa-test-config %{buildroot}%{_bindir}/ipa-test-config-%{python2_version}
mv %{buildroot}%{_bindir}/ipa-test-task %{buildroot}%{_bindir}/ipa-test-task-%{python2_version}
ln -s %{_bindir}/ipa-run-tests-%{python2_version} %{buildroot}%{_bindir}/ipa-run-tests-2
ln -s %{_bindir}/ipa-test-config-%{python2_version} %{buildroot}%{_bindir}/ipa-test-config-2
ln -s %{_bindir}/ipa-test-task-%{python2_version} %{buildroot}%{_bindir}/ipa-test-task-2
# test framework defaults to Python 2
ln -s %{_bindir}/ipa-run-tests-%{python2_version} %{buildroot}%{_bindir}/ipa-run-tests
ln -s %{_bindir}/ipa-test-config-%{python2_version} %{buildroot}%{_bindir}/ipa-test-config
ln -s %{_bindir}/ipa-test-task-%{python2_version} %{buildroot}%{_bindir}/ipa-test-task
%endif # with_ipatests

# remove files which are useful only for make uninstall
find %{buildroot} -wholename '*/site-packages/*/install_files.txt' -exec rm {} \;

%find_lang %{gettext_domain}

%if ! %{ONLY_CLIENT}
# Remove .la files from libtool - we don't want to package
# these files
rm %{buildroot}/%{plugin_dir}/libipa_pwd_extop.la
rm %{buildroot}/%{plugin_dir}/libipa_enrollment_extop.la
rm %{buildroot}/%{plugin_dir}/libipa_winsync.la
rm %{buildroot}/%{plugin_dir}/libipa_repl_version.la
rm %{buildroot}/%{plugin_dir}/libipa_uuid.la
rm %{buildroot}/%{plugin_dir}/libipa_modrdn.la
rm %{buildroot}/%{plugin_dir}/libipa_lockout.la
rm %{buildroot}/%{plugin_dir}/libipa_cldap.la
rm %{buildroot}/%{plugin_dir}/libipa_dns.la
rm %{buildroot}/%{plugin_dir}/libipa_sidgen.la
rm %{buildroot}/%{plugin_dir}/libipa_sidgen_task.la
rm %{buildroot}/%{plugin_dir}/libipa_extdom_extop.la
rm %{buildroot}/%{plugin_dir}/libipa_range_check.la
rm %{buildroot}/%{plugin_dir}/libipa_otp_counter.la
rm %{buildroot}/%{plugin_dir}/libipa_otp_lasttoken.la
rm %{buildroot}/%{plugin_dir}/libtopology.la
rm %{buildroot}/%{_libdir}/krb5/plugins/kdb/ipadb.la
rm %{buildroot}/%{_libdir}/samba/pdb/ipasam.la

# So we can own our Apache configuration
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
/bin/touch %{buildroot}%{_sysconfdir}/httpd/conf.d/ipa.conf
/bin/touch %{buildroot}%{_sysconfdir}/httpd/conf.d/ipa-kdc-proxy.conf
/bin/touch %{buildroot}%{_sysconfdir}/httpd/conf.d/ipa-pki-proxy.conf
/bin/touch %{buildroot}%{_sysconfdir}/httpd/conf.d/ipa-rewrite.conf
/bin/touch %{buildroot}%{_usr}/share/ipa/html/ca.crt
/bin/touch %{buildroot}%{_usr}/share/ipa/html/kerberosauth.xpi
/bin/touch %{buildroot}%{_usr}/share/ipa/html/krb.con
/bin/touch %{buildroot}%{_usr}/share/ipa/html/krb.js
/bin/touch %{buildroot}%{_usr}/share/ipa/html/krb5.ini
/bin/touch %{buildroot}%{_usr}/share/ipa/html/krbrealm.con

mkdir -p %{buildroot}%{_libdir}/krb5/plugins/libkrb5
touch %{buildroot}%{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so

%endif # ONLY_CLIENT

/bin/touch %{buildroot}%{_sysconfdir}/ipa/default.conf
/bin/touch %{buildroot}%{_sysconfdir}/ipa/ca.crt

%if ! %{ONLY_CLIENT}
mkdir -p %{buildroot}%{_sysconfdir}/cron.d
%endif # ONLY_CLIENT


%clean
rm -rf %{buildroot}


%if ! %{ONLY_CLIENT}

%post server
# NOTE: systemd specific section
    /bin/systemctl --system daemon-reload 2>&1 || :
# END
if [ $1 -gt 1 ] ; then
    /bin/systemctl condrestart certmonger.service 2>&1 || :
fi
/bin/systemctl reload-or-try-restart dbus
/bin/systemctl reload-or-try-restart oddjobd

%tmpfiles_create ipa.conf

%posttrans server
# don't execute upgrade and restart of IPA when server is not installed
python2 -c "import sys; from ipaserver.install import installutils; sys.exit(0 if installutils.is_ipa_configured() else 1);" > /dev/null 2>&1

if [  $? -eq 0 ]; then
    # This is necessary for Fedora system upgrades which by default
    # work with the network being offline
    /bin/systemctl start network-online.target

    # This must be run in posttrans so that updates from previous
    # execution that may no longer be shipped are not applied.
    /usr/sbin/ipa-server-upgrade --quiet >/dev/null || :

    # Restart IPA processes. This must be also run in postrans so that plugins
    # and software is in consistent state
    # NOTE: systemd specific section

    /bin/systemctl is-enabled ipa.service >/dev/null 2>&1
    if [  $? -eq 0 ]; then
        /bin/systemctl restart ipa.service >/dev/null 2>&1 || :
    fi
fi
# END


%preun server
if [ $1 = 0 ]; then
# NOTE: systemd specific section
    /bin/systemctl --quiet stop ipa.service || :
    /bin/systemctl --quiet disable ipa.service || :
    /bin/systemctl reload-or-try-restart dbus
    /bin/systemctl reload-or-try-restart oddjobd
# END
fi


%pre server
# Stop ipa_kpasswd if it exists before upgrading so we don't have a
# zombie process when we're done.
if [ -e /usr/sbin/ipa_kpasswd ]; then
# NOTE: systemd specific section
    /bin/systemctl stop ipa_kpasswd.service >/dev/null 2>&1 || :
# END
fi

# create users and groups
# create kdcproxy group and user
getent group kdcproxy >/dev/null || groupadd -f -r kdcproxy
getent passwd kdcproxy >/dev/null || useradd -r -g kdcproxy -s /sbin/nologin -d / -c "IPA KDC Proxy User" kdcproxy
# create ipaapi group and user
getent group ipaapi >/dev/null || groupadd -f -r ipaapi
getent passwd ipaapi >/dev/null || useradd -r -g ipaapi -s /sbin/nologin -d / -c "IPA Framework User" ipaapi
# add apache to ipaaapi group
id -Gn apache | grep '\bipaapi\b' >/dev/null || usermod apache -a -G ipaapi

%postun server-trust-ad
if [ "$1" -ge "1" ]; then
    if [ "`readlink %{_sysconfdir}/alternatives/winbind_krb5_locator.so`" == "/dev/null" ]; then
        %{_sbindir}/alternatives --set winbind_krb5_locator.so /dev/null
    fi
fi


%post server-trust-ad
%{_sbindir}/update-alternatives --install %{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so \
        winbind_krb5_locator.so /dev/null 90
/bin/systemctl reload-or-try-restart dbus
/bin/systemctl reload-or-try-restart oddjobd


%posttrans server-trust-ad
python2 -c "import sys; from ipaserver.install import installutils; sys.exit(0 if installutils.is_ipa_configured() else 1);" > /dev/null 2>&1
if [  $? -eq 0 ]; then
# NOTE: systemd specific section
    /bin/systemctl try-restart httpd.service >/dev/null 2>&1 || :
# END
fi


%preun server-trust-ad
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove winbind_krb5_locator.so /dev/null
    /bin/systemctl reload-or-try-restart dbus
    /bin/systemctl reload-or-try-restart oddjobd
fi

%endif # ONLY_CLIENT


%post client
if [ $1 -gt 1 ] ; then
    # Has the client been configured?
    restore=0
    test -f '/var/lib/ipa-client/sysrestore/sysrestore.index' && restore=$(wc -l '/var/lib/ipa-client/sysrestore/sysrestore.index' | awk '{print $1}')

    if [ -f '/etc/sssd/sssd.conf' -a $restore -ge 2 ]; then
        if ! grep -E -q '/var/lib/sss/pubconf/krb5.include.d/' /etc/krb5.conf  2>/dev/null ; then
            echo "includedir /var/lib/sss/pubconf/krb5.include.d/" > /etc/krb5.conf.ipanew
            cat /etc/krb5.conf >> /etc/krb5.conf.ipanew
            mv -Z /etc/krb5.conf.ipanew /etc/krb5.conf
        fi
    fi

    if [ $restore -ge 2 ]; then
        if grep -E -q '\s*pkinit_anchors = FILE:/etc/ipa/ca.crt$' /etc/krb5.conf 2>/dev/null; then
            sed -E 's|(\s*)pkinit_anchors = FILE:/etc/ipa/ca.crt$|\1pkinit_anchors = FILE:/var/lib/ipa-client/pki/kdc-ca-bundle.pem\n\1pkinit_pool = FILE:/var/lib/ipa-client/pki/ca-bundle.pem|' /etc/krb5.conf >/etc/krb5.conf.ipanew
            mv -Z /etc/krb5.conf.ipanew /etc/krb5.conf
            cp /etc/ipa/ca.crt /var/lib/ipa-client/pki/kdc-ca-bundle.pem
            cp /etc/ipa/ca.crt /var/lib/ipa-client/pki/ca-bundle.pem
        fi
    fi

    if [ -f '/etc/sysconfig/ntpd' -a $restore -ge 2 ]; then
        if grep -E -q 'OPTIONS=.*-u ntp:ntp' /etc/sysconfig/ntpd 2>/dev/null; then
            sed -r '/OPTIONS=/ { s/\s+-u ntp:ntp\s+/ /; s/\s*-u ntp:ntp\s*// }' /etc/sysconfig/ntpd >/etc/sysconfig/ntpd.ipanew
            mv -Z /etc/sysconfig/ntpd.ipanew /etc/sysconfig/ntpd

            /bin/systemctl condrestart ntpd.service 2>&1 || :
        fi
    fi

    if [ $restore -ge 2 ]; then
        python2 -c 'from ipaclient.install.client import update_ipa_nssdb; update_ipa_nssdb()' >/var/log/ipaupgrade.log 2>&1
    fi
fi


%triggerin client -- openssh-server
# Has the client been configured?
restore=0
test -f '/var/lib/ipa-client/sysrestore/sysrestore.index' && restore=$(wc -l '/var/lib/ipa-client/sysrestore/sysrestore.index' | awk '{print $1}')

if [ -f '/etc/ssh/sshd_config' -a $restore -ge 2 ]; then
    if grep -E -q '^(AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys|PubKeyAgent /usr/bin/sss_ssh_authorizedkeys %u)$' /etc/ssh/sshd_config 2>/dev/null; then
        sed -r '
            /^(AuthorizedKeysCommand(User|RunAs)|PubKeyAgentRunAs)[ \t]/ d
        ' /etc/ssh/sshd_config >/etc/ssh/sshd_config.ipanew

        if /usr/sbin/sshd -t -f /dev/null -o 'AuthorizedKeysCommand=/usr/bin/sss_ssh_authorizedkeys' -o 'AuthorizedKeysCommandUser=nobody' 2>/dev/null; then
            sed -ri '
                s/^PubKeyAgent (.+) %u$/AuthorizedKeysCommand \1/
                s/^AuthorizedKeysCommand .*$/\0\nAuthorizedKeysCommandUser nobody/
            ' /etc/ssh/sshd_config.ipanew
        elif /usr/sbin/sshd -t -f /dev/null -o 'AuthorizedKeysCommand=/usr/bin/sss_ssh_authorizedkeys' -o 'AuthorizedKeysCommandRunAs=nobody' 2>/dev/null; then
            sed -ri '
                s/^PubKeyAgent (.+) %u$/AuthorizedKeysCommand \1/
                s/^AuthorizedKeysCommand .*$/\0\nAuthorizedKeysCommandRunAs nobody/
            ' /etc/ssh/sshd_config.ipanew
        elif /usr/sbin/sshd -t -f /dev/null -o 'PubKeyAgent=/usr/bin/sss_ssh_authorizedkeys %u' -o 'PubKeyAgentRunAs=nobody' 2>/dev/null; then
            sed -ri '
                s/^AuthorizedKeysCommand (.+)$/PubKeyAgent \1 %u/
                s/^PubKeyAgent .*$/\0\nPubKeyAgentRunAs nobody/
            ' /etc/ssh/sshd_config.ipanew
        fi

        mv -Z /etc/ssh/sshd_config.ipanew /etc/ssh/sshd_config
        chmod 600 /etc/ssh/sshd_config

        /bin/systemctl condrestart sshd.service 2>&1 || :
    fi
fi


%if ! %{ONLY_CLIENT}

%files server
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%{_sbindir}/ipa-backup
%{_sbindir}/ipa-restore
%{_sbindir}/ipa-ca-install
%{_sbindir}/ipa-kra-install
%{_sbindir}/ipa-server-install
%{_sbindir}/ipa-replica-conncheck
%{_sbindir}/ipa-replica-install
%{_sbindir}/ipa-replica-prepare
%{_sbindir}/ipa-replica-manage
%{_sbindir}/ipa-csreplica-manage
%{_sbindir}/ipa-server-certinstall
%{_sbindir}/ipa-server-upgrade
%{_sbindir}/ipa-ldap-updater
%{_sbindir}/ipa-otptoken-import
%{_sbindir}/ipa-compat-manage
%{_sbindir}/ipa-nis-manage
%{_sbindir}/ipa-managed-entries
%{_sbindir}/ipactl
%{_sbindir}/ipa-advise
%{_sbindir}/ipa-cacert-manage
%{_sbindir}/ipa-winsync-migrate
%{_sbindir}/ipa-pkinit-manage
%{_libexecdir}/certmonger/dogtag-ipa-ca-renew-agent-submit
%{_libexecdir}/certmonger/ipa-server-guard
%dir %{_libexecdir}/ipa
%{_libexecdir}/ipa/ipa-custodia
%{_libexecdir}/ipa/ipa-dnskeysyncd
%{_libexecdir}/ipa/ipa-dnskeysync-replica
%{_libexecdir}/ipa/ipa-ods-exporter
%{_libexecdir}/ipa/ipa-httpd-kdcproxy
%{_libexecdir}/ipa/ipa-pki-retrieve-key
%{_libexecdir}/ipa/ipa-otpd
%dir %{_libexecdir}/ipa/oddjob
%attr(0755,root,root) %{_libexecdir}/ipa/oddjob/org.freeipa.server.conncheck
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freeipa.server.conf
%config(noreplace) %{_sysconfdir}/oddjobd.conf.d/ipa-server.conf
%dir %{_libexecdir}/ipa/certmonger
%attr(755,root,root) %{_libexecdir}/ipa/certmonger/*
# NOTE: systemd specific section
%attr(644,root,root) %{_unitdir}/ipa.service
%attr(644,root,root) %{_unitdir}/ipa-otpd.socket
%attr(644,root,root) %{_unitdir}/ipa-otpd@.service
%attr(644,root,root) %{_unitdir}/ipa-dnskeysyncd.service
%attr(644,root,root) %{_unitdir}/ipa-ods-exporter.socket
%attr(644,root,root) %{_unitdir}/ipa-ods-exporter.service
# END
%attr(755,root,root) %{plugin_dir}/libipa_pwd_extop.so
%attr(755,root,root) %{plugin_dir}/libipa_enrollment_extop.so
%attr(755,root,root) %{plugin_dir}/libipa_winsync.so
%attr(755,root,root) %{plugin_dir}/libipa_repl_version.so
%attr(755,root,root) %{plugin_dir}/libipa_uuid.so
%attr(755,root,root) %{plugin_dir}/libipa_modrdn.so
%attr(755,root,root) %{plugin_dir}/libipa_lockout.so
%attr(755,root,root) %{plugin_dir}/libipa_cldap.so
%attr(755,root,root) %{plugin_dir}/libipa_dns.so
%attr(755,root,root) %{plugin_dir}/libipa_range_check.so
%attr(755,root,root) %{plugin_dir}/libipa_otp_counter.so
%attr(755,root,root) %{plugin_dir}/libipa_otp_lasttoken.so
%attr(755,root,root) %{plugin_dir}/libtopology.so
%attr(755,root,root) %{plugin_dir}/libipa_sidgen.so
%attr(755,root,root) %{plugin_dir}/libipa_sidgen_task.so
%attr(755,root,root) %{plugin_dir}/libipa_extdom_extop.so
%attr(755,root,root) %{_libdir}/krb5/plugins/kdb/ipadb.so
%{_mandir}/man1/ipa-replica-conncheck.1*
%{_mandir}/man1/ipa-replica-install.1*
%{_mandir}/man1/ipa-replica-manage.1*
%{_mandir}/man1/ipa-csreplica-manage.1*
%{_mandir}/man1/ipa-replica-prepare.1*
%{_mandir}/man1/ipa-server-certinstall.1*
%{_mandir}/man1/ipa-server-install.1*
%{_mandir}/man1/ipa-server-upgrade.1*
%{_mandir}/man1/ipa-ca-install.1*
%{_mandir}/man1/ipa-kra-install.1*
%{_mandir}/man1/ipa-compat-manage.1*
%{_mandir}/man1/ipa-nis-manage.1*
%{_mandir}/man1/ipa-managed-entries.1*
%{_mandir}/man1/ipa-ldap-updater.1*
%{_mandir}/man8/ipactl.8*
%{_mandir}/man1/ipa-backup.1*
%{_mandir}/man1/ipa-restore.1*
%{_mandir}/man1/ipa-advise.1*
%{_mandir}/man1/ipa-otptoken-import.1*
%{_mandir}/man1/ipa-cacert-manage.1*
%{_mandir}/man1/ipa-winsync-migrate.1*
%{_mandir}/man1/ipa-pkinit-manage.1*


%files -n python2-ipaserver
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%{python2_sitelib}/ipaserver
%{python2_sitelib}/ipaserver-*.egg-info


%if 0%{?with_python3}

%files -n python3-ipaserver
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%{python3_sitelib}/ipaserver
%{python3_sitelib}/ipaserver-*.egg-info

%endif # with_python3


%files server-common
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%ghost %verify(not owner group) %dir %{_sharedstatedir}/kdcproxy
%dir %attr(0755,root,root) %{_sysconfdir}/ipa/kdcproxy
%config(noreplace) %{_sysconfdir}/sysconfig/ipa-dnskeysyncd
%config(noreplace) %{_sysconfdir}/sysconfig/ipa-ods-exporter
%config(noreplace) %{_sysconfdir}/ipa/kdcproxy/kdcproxy.conf
# NOTE: systemd specific section
%{_tmpfilesdir}/ipa.conf
%attr(644,root,root) %{_unitdir}/ipa-custodia.service
%ghost %attr(644,root,root) %{etc_systemd_dir}/httpd.d/ipa.conf
# END
%dir %{_usr}/share/ipa
%{_usr}/share/ipa/wsgi.py*
%{_usr}/share/ipa/kdcproxy.wsgi
%{_usr}/share/ipa/*.ldif
%{_usr}/share/ipa/*.uldif
%{_usr}/share/ipa/*.template
%dir %{_usr}/share/ipa/advise
%dir %{_usr}/share/ipa/advise/legacy
%{_usr}/share/ipa/advise/legacy/*.template
%dir %{_usr}/share/ipa/profiles
%{_usr}/share/ipa/profiles/README
%{_usr}/share/ipa/profiles/*.cfg
%dir %{_usr}/share/ipa/html
%{_usr}/share/ipa/html/ffconfig.js
%{_usr}/share/ipa/html/ffconfig_page.js
%{_usr}/share/ipa/html/ssbrowser.html
%{_usr}/share/ipa/html/browserconfig.html
%{_usr}/share/ipa/html/unauthorized.html
%dir %{_usr}/share/ipa/migration
%{_usr}/share/ipa/migration/error.html
%{_usr}/share/ipa/migration/index.html
%{_usr}/share/ipa/migration/invalid.html
%{_usr}/share/ipa/migration/migration.py*
%dir %{_usr}/share/ipa/ui
%{_usr}/share/ipa/ui/index.html
%{_usr}/share/ipa/ui/reset_password.html
%{_usr}/share/ipa/ui/sync_otp.html
%{_usr}/share/ipa/ui/*.ico
%{_usr}/share/ipa/ui/*.css
%{_usr}/share/ipa/ui/*.js
%dir %{_usr}/share/ipa/ui/css
%{_usr}/share/ipa/ui/css/*.css
%dir %{_usr}/share/ipa/ui/js
%dir %{_usr}/share/ipa/ui/js/dojo
%{_usr}/share/ipa/ui/js/dojo/dojo.js
%dir %{_usr}/share/ipa/ui/js/libs
%{_usr}/share/ipa/ui/js/libs/*.js
%dir %{_usr}/share/ipa/ui/js/freeipa
%{_usr}/share/ipa/ui/js/freeipa/app.js
%{_usr}/share/ipa/ui/js/freeipa/core.js
%dir %{_usr}/share/ipa/ui/js/plugins
%dir %{_usr}/share/ipa/ui/images
%{_usr}/share/ipa/ui/images/*.jpg
%{_usr}/share/ipa/ui/images/*.png
%dir %{_usr}/share/ipa/wsgi
%{_usr}/share/ipa/wsgi/plugins.py*
%dir %{_sysconfdir}/ipa
%dir %{_sysconfdir}/ipa/html
%config(noreplace) %{_sysconfdir}/ipa/html/ffconfig.js
%config(noreplace) %{_sysconfdir}/ipa/html/ffconfig_page.js
%config(noreplace) %{_sysconfdir}/ipa/html/ssbrowser.html
%config(noreplace) %{_sysconfdir}/ipa/html/unauthorized.html
%config(noreplace) %{_sysconfdir}/ipa/html/browserconfig.html
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/httpd/conf.d/ipa-rewrite.conf
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/httpd/conf.d/ipa.conf
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/httpd/conf.d/ipa-kdc-proxy.conf
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/httpd/conf.d/ipa-pki-proxy.conf
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/ipa/kdcproxy/ipa-kdc-proxy.conf
%dir %attr(0755,root,root) %{_sysconfdir}/ipa/dnssec
%{_usr}/share/ipa/ipa.conf
%{_usr}/share/ipa/ipa-rewrite.conf
%{_usr}/share/ipa/ipa-pki-proxy.conf
%ghost %attr(0644,root,apache) %config(noreplace) %{_usr}/share/ipa/html/ca.crt
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/kerberosauth.xpi
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/krb.con
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/krb.js
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/krb5.ini
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/krbrealm.con
%dir %{_usr}/share/ipa/updates/
%{_usr}/share/ipa/updates/*
%dir %{_localstatedir}/lib/ipa
%attr(700,root,root) %dir %{_localstatedir}/lib/ipa/backup
%attr(700,root,root) %dir %{_localstatedir}/lib/ipa/gssproxy
%attr(700,root,root) %dir %{_localstatedir}/lib/ipa/sysrestore
%attr(700,root,root) %dir %{_localstatedir}/lib/ipa/sysupgrade
%attr(755,root,root) %dir %{_localstatedir}/lib/ipa/pki-ca
%ghost %{_localstatedir}/lib/ipa/pki-ca/publish
%ghost %{_localstatedir}/named/dyndb-ldap/ipa
%dir %attr(0700,root,root) %{_sysconfdir}/ipa/custodia
%dir %{_usr}/share/ipa/schema.d
%attr(0644,root,root) %{_usr}/share/ipa/schema.d/README
%attr(0644,root,root) %{_usr}/share/ipa/gssapi.login
%{_usr}/share/ipa/ipakrb5.aug

%files server-dns
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%{_sbindir}/ipa-dns-install
%{_mandir}/man1/ipa-dns-install.1*


%files server-trust-ad
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%{_sbindir}/ipa-adtrust-install
%{_usr}/share/ipa/smb.conf.empty
%attr(755,root,root) %{_libdir}/samba/pdb/ipasam.so
%{_mandir}/man1/ipa-adtrust-install.1*
%ghost %{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so
%{_sysconfdir}/dbus-1/system.d/oddjob-ipa-trust.conf
%{_sysconfdir}/oddjobd.conf.d/oddjobd-ipa-trust.conf
%%attr(755,root,root) %{_libexecdir}/ipa/oddjob/com.redhat.idm.trust-fetch-domains

%endif # ONLY_CLIENT


%files client
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%{_sbindir}/ipa-client-install
%{_sbindir}/ipa-client-automount
%{_sbindir}/ipa-certupdate
%{_sbindir}/ipa-getkeytab
%{_sbindir}/ipa-rmkeytab
%{_sbindir}/ipa-join
%{_bindir}/ipa
%config %{_sysconfdir}/bash_completion.d
%{_mandir}/man1/ipa.1*
%{_mandir}/man1/ipa-getkeytab.1*
%{_mandir}/man1/ipa-rmkeytab.1*
%{_mandir}/man1/ipa-client-install.1*
%{_mandir}/man1/ipa-client-automount.1*
%{_mandir}/man1/ipa-certupdate.1*
%{_mandir}/man1/ipa-join.1*


%files -n python2-ipaclient
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%dir %{python_sitelib}/ipaclient
%{python_sitelib}/ipaclient/*.py*
%dir %{python_sitelib}/ipaclient/install
%{python_sitelib}/ipaclient/install/*.py*
%dir %{python_sitelib}/ipaclient/plugins
%{python_sitelib}/ipaclient/plugins/*.py*
%dir %{python_sitelib}/ipaclient/remote_plugins
%{python_sitelib}/ipaclient/remote_plugins/*.py*
%dir %{python_sitelib}/ipaclient/remote_plugins/2_*
%{python_sitelib}/ipaclient/remote_plugins/2_*/*.py*
%dir %{python_sitelib}/ipaclient/csrgen
%dir %{python_sitelib}/ipaclient/csrgen/profiles
%{python_sitelib}/ipaclient/csrgen/profiles/*.json
%dir %{python_sitelib}/ipaclient/csrgen/rules
%{python_sitelib}/ipaclient/csrgen/rules/*.json
%dir %{python_sitelib}/ipaclient/csrgen/templates
%{python_sitelib}/ipaclient/csrgen/templates/*.tmpl
%{python_sitelib}/ipaclient-*.egg-info


%if 0%{?with_python3}

%files -n python3-ipaclient
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%dir %{python3_sitelib}/ipaclient
%{python3_sitelib}/ipaclient/*.py
%{python3_sitelib}/ipaclient/__pycache__/*.py*
%dir %{python3_sitelib}/ipaclient/install
%{python3_sitelib}/ipaclient/install/*.py
%{python3_sitelib}/ipaclient/install/__pycache__/*.py*
%dir %{python3_sitelib}/ipaclient/plugins
%{python3_sitelib}/ipaclient/plugins/*.py
%{python3_sitelib}/ipaclient/plugins/__pycache__/*.py*
%dir %{python3_sitelib}/ipaclient/remote_plugins
%{python3_sitelib}/ipaclient/remote_plugins/*.py
%{python3_sitelib}/ipaclient/remote_plugins/__pycache__/*.py*
%dir %{python3_sitelib}/ipaclient/remote_plugins/2_*
%{python3_sitelib}/ipaclient/remote_plugins/2_*/*.py
%{python3_sitelib}/ipaclient/remote_plugins/2_*/__pycache__/*.py*
%dir %{python3_sitelib}/ipaclient/csrgen
%dir %{python3_sitelib}/ipaclient/csrgen/profiles
%{python3_sitelib}/ipaclient/csrgen/profiles/*.json
%dir %{python3_sitelib}/ipaclient/csrgen/rules
%{python3_sitelib}/ipaclient/csrgen/rules/*.json
%dir %{python3_sitelib}/ipaclient/csrgen/templates
%{python3_sitelib}/ipaclient/csrgen/templates/*.tmpl
%{python3_sitelib}/ipaclient-*.egg-info

%endif # with_python3


%files client-common
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%dir %attr(0755,root,root) %{_sysconfdir}/ipa/
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/ipa/default.conf
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/ipa/ca.crt
%dir %attr(0755,root,root) %{_sysconfdir}/ipa/nssdb
%ghost %config(noreplace) %{_sysconfdir}/ipa/nssdb/cert8.db
%ghost %config(noreplace) %{_sysconfdir}/ipa/nssdb/key3.db
%ghost %config(noreplace) %{_sysconfdir}/ipa/nssdb/secmod.db
%ghost %config(noreplace) %{_sysconfdir}/ipa/nssdb/pwdfile.txt
%ghost %config(noreplace) %{_sysconfdir}/pki/ca-trust/source/ipa.p11-kit
%dir %{_localstatedir}/lib/ipa-client
%dir %{_localstatedir}/lib/ipa-client/pki
%dir %{_localstatedir}/lib/ipa-client/sysrestore
%{_mandir}/man5/default.conf.5*


%files python-compat
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING


%files -n python2-ipalib
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%dir %{python_sitelib}/ipapython
%{python_sitelib}/ipapython/*.py*
%dir %{python_sitelib}/ipapython/install
%{python_sitelib}/ipapython/install/*.py*
%dir %{python_sitelib}/ipalib
%{python_sitelib}/ipalib/*.py*
%dir %{python_sitelib}/ipalib/install
%{python_sitelib}/ipalib/install/*.py*
%dir %{python_sitelib}/ipaplatform
%{python_sitelib}/ipaplatform/*
%{python_sitelib}/ipapython-*.egg-info
%{python_sitelib}/ipalib-*.egg-info
%{python_sitelib}/ipaplatform-*.egg-info


%files common -f %{gettext_domain}.lang
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING


%if 0%{?with_python3}

%files -n python3-ipalib
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING

%{python3_sitelib}/ipapython/
%{python3_sitelib}/ipalib/
%{python3_sitelib}/ipaplatform/
%{python3_sitelib}/ipapython-*.egg-info
%{python3_sitelib}/ipalib-*.egg-info
%{python3_sitelib}/ipaplatform-*.egg-info

%endif # with_python3


%if 0%{?with_ipatests}

%files -n python2-ipatests
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%{python_sitelib}/ipatests
%{python_sitelib}/ipatests-*.egg-info
%{_bindir}/ipa-run-tests
%{_bindir}/ipa-test-config
%{_bindir}/ipa-test-task
%{_bindir}/ipa-run-tests-2
%{_bindir}/ipa-test-config-2
%{_bindir}/ipa-test-task-2
%{_bindir}/ipa-run-tests-%{python2_version}
%{_bindir}/ipa-test-config-%{python2_version}
%{_bindir}/ipa-test-task-%{python2_version}
%{_mandir}/man1/ipa-run-tests.1*
%{_mandir}/man1/ipa-test-config.1*
%{_mandir}/man1/ipa-test-task.1*

%if 0%{?with_python3}

%files -n python3-ipatests
%defattr(-,root,root,-)
%doc README.md Contributors.txt
%license COPYING
%{python3_sitelib}/ipatests
%{python3_sitelib}/ipatests-*.egg-info
%{_bindir}/ipa-run-tests-3
%{_bindir}/ipa-test-config-3
%{_bindir}/ipa-test-task-3
%{_bindir}/ipa-run-tests-%{python3_version}
%{_bindir}/ipa-test-config-%{python3_version}
%{_bindir}/ipa-test-task-%{python3_version}

%endif # with_python3

%endif # with_ipatests


%changelog
* Tue Nov 26 2013 Petr Viktorin <pviktori@redhat.com> - 4.6.90.dev201806272025+git7c2dba191-
- Remove changelog. The history is kept in Git, downstreams have own logs.
# note, this entry is here to placate tools that expect a non-empty changelog
