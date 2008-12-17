#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import os.path
from setuptools import setup

setup(
    name = 'TracIniGetMacro',
    packages = ['inigetmacro'],
    version = '0.11.0.1',

    author = 'Douglas Clifton',
    author_email = 'dwclifton@gmail.com',
    description = 'Trac.ini [section].option Macro',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    keywords = '0.11 dwclifton macro wiki',
    url = 'http://trac-hacks.org/wiki/IniGetMacro',
    license = 'BSD',

    classifiers = [
        'Framework :: Trac',
    ],
    
    install_requires = ['Trac'],

    entry_points = {
        'trac.plugins': [
            'inigetmacro.macro = inigetmacro.macro',
        ]
    }
)
