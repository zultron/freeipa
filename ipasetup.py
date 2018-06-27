# Copyright (C) 2016  Red Hat
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
from distutils import log
import os
import sys
from setuptools.command.build_py import build_py as setuptools_build_py


class build_py(setuptools_build_py):
    """Exclude NAME.install subpackage from wheels
    """
    def initialize_options(self):
        setuptools_build_py.initialize_options(self)
        self.skip_package = None

    def finalize_options(self):
        setuptools_build_py.finalize_options(self)
        omit = os.environ.get('IPA_OMIT_INSTALL', '0')
        if omit == '1':
            distname = self.distribution.metadata.name
            self.skip_package = '{}.install'.format(distname)
            log.warn("bdist_wheel: Ignore package: %s",
                     self.skip_package)

    def build_module(self, module, module_file, package):
        if isinstance(package, str):
            package = package.split('.')
        name = '.'.join(list(package) + [module])
        if self.skip_package and name.startswith(self.skip_package):
            # remove file in case it has been copied to build/lib before
            outfile = self.get_module_outfile(self.build_lib, package, module)
            try:
                os.unlink(outfile)
            except OSError:
                pass
        else:
            return setuptools_build_py.build_module(self, module,
                                                    module_file, package)

import setuptools

VERSION = '4.6.90.dev201806272043+gitfb34e05cd'

SETUPTOOLS_VERSION = tuple(int(v) for v in setuptools.__version__.split("."))

# backwards compatibility with setuptools 0.9.8, split off +gitHASH suffix
# PEP 440 was introduced in setuptools 8.
if SETUPTOOLS_VERSION < (8, 0, 0):
    VERSION = VERSION.split('+')[0]


PACKAGE_VERSION = {
    'cryptography': 'cryptography >= 1.6',
    'custodia': 'custodia >= 0.3.1',
    'dnspython': 'dnspython >= 1.15',
    'gssapi': 'gssapi >= 1.2.0',
    'ipaclient': 'ipaclient == {}'.format(VERSION),
    'ipalib': 'ipalib == {}'.format(VERSION),
    'ipaplatform': 'ipaplatform == {}'.format(VERSION),
    'ipapython': 'ipapython == {}'.format(VERSION),
    'ipaserver': 'ipaserver == {}'.format(VERSION),
    'jwcrypto': 'jwcrpyto >= 0.4.2',
    'kdcproxy': 'kdcproxy >= 0.3',
    'netifaces': 'netifaces >= 0.10.4',
    'pyldap': 'pyldap >= 2.4.15',
    'python-yubico': 'python-yubico >= 1.2.3',
    'qrcode': 'qrcode >= 5.0',
}


common_args = dict(
    version=VERSION,
    license="GPLv3",
    author="FreeIPA Developers",
    author_email="freeipa-devel@redhat.com",
    maintainer="FreeIPA Developers",
    maintainer_email="freeipa-devel@redhat.com",
    url="http://www.freeipa.org/",
    download_url="http://www.freeipa.org/page/Downloads",
    platforms=["Linux", "Solaris", "Unix"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: System Administrators",
        ("License :: OSI Approved :: "
         "GNU General Public License v3 (GPLv3)"),
        "Programming Language :: C",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Security",
        ("Topic :: System :: Systems Administration :: "
         "Authentication/Directory :: LDAP"),
    ],
)

local_path = os.path.dirname(os.path.abspath(sys.argv[0]))
old_path = os.path.abspath(os.getcwd())


def ipasetup(name, doc, **kwargs):
    doclines = doc.split("\n")

    install_requires = list(kwargs.pop('install_requires', []))
    for i, entry in enumerate(install_requires):
        install_requires[i] = PACKAGE_VERSION.get(entry, entry)

    setup_kwargs = common_args.copy()
    setup_kwargs.update(
        name=name,
        description=doclines[0],
        long_description="\n".join(doclines[:2]),
        install_requires=install_requires,
        **kwargs
    )
    # exclude setup helpers from getting installed
    epd = setup_kwargs.setdefault('exclude_package_data', {})
    epd.setdefault('', []).extend(['*/setup.py', '*/ipasetup.py'])
    # exclude NAME.install from wheels
    cmdclass = setup_kwargs.setdefault('cmdclass', {})
    cmdclass['build_py'] = build_py

    # Env markers like ":python_version<'3'" are not supported by
    # setuptools < 18.0.
    if 'extras_require' in setup_kwargs and SETUPTOOLS_VERSION < (18, 0, 0):
        for k in list(setup_kwargs['extras_require']):
            if not k.startswith(':'):
                continue
            values = setup_kwargs['extras_require'].pop(k)
            req = setup_kwargs.setdefault('install_requires', [])
            if k == ":python_version<'3'":
                if sys.version_info.major == 2:
                    req.extend(values)
            elif k == ":python_version>='3'":
                if sys.version_info.major >= 3:
                    req.extend(values)
            else:
                raise ValueError(k, values)

    os.chdir(local_path)
    try:
        # BEFORE importing distutils, remove MANIFEST. distutils doesn't
        # properly update it when the contents of directories change.
        if os.path.isfile('MANIFEST'):
            os.unlink('MANIFEST')
        from setuptools import setup
        return setup(**setup_kwargs)
    finally:
        os.chdir(old_path)
