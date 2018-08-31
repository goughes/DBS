#!/usr/bin/env python
from distutils.core import setup

setup(name = 'dbs-client',
        version = '3.3.160',
        maintainer = 'CMS DWMWM Group',
        maintainer_email = 'hn-cms-dmDevelopment@cern.ch',
        packages = ['dbs',
                    'dbs.apis',
                    'dbs.exceptions'],
        package_dir = {'' : 'Client/src/python/'},
        install_requires = ['pycurl-client'],
        url = "https://github.com/dmwm/DBS",
    )
