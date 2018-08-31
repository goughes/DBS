#!/usr/bin/env python
from distutils.core import setup

setup(name = 'pycurl-client',
        version = '3.3.160',
        maintainer = 'CMS DWMWM Group',
        maintainer_email = 'hn-cms-dmDevelopment@cern.ch',
        packages = ['RestClient',
                    'RestClient.AuthHandling',
                    'RestClient.ErrorHandling',
                    'RestClient.ProxyPlugins',
                    'RestClient.RequestHandling'],
        package_dir = {'' : 'PycurlClient/src/python/'},
        install_requires = ['python-cjson', 'pycurl'],
        url = "https://github.com/dmwm/DBS",
    )
