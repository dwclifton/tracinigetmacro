#!/usr/bin/env python

import os.path
from setuptools import setup

setup(
    name = 'TracIniGetMacro',
    packages = ['iniget', 'welcome'],
    version = '0.11.3',

    author = 'Douglas Clifton',
    author_email = 'dwclifton@gmail.com',
    description = 'Trac.ini [section].option Macro',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    keywords = '0.11 dwclifton macro wiki',
    url = 'http://trac-hacks.org/wiki/IniGetMacro',
    license = 'BSD',

    classifiers = ['Framework :: Trac'],
    install_requires = ['Trac'],
    entry_points = {
        'trac.plugins': [
            'iniget.macro = iniget.macro',
            'welcome.macro = welcome.macro'
        ]
    }
)
