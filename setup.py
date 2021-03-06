#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages

setup(name		= 'python-yubico',
      version		= '1.1.0',
      description	= 'Python code for talking to Yubico\'s YubiKeys',
      author		= 'Fredrik Thulin',
      author_email	= 'fredrik@yubico.com',
      url		= 'http://www.yubico.com/',
      license		= 'BSD',
      packages		= ['yubico'],
      package_dir	= {'': 'Lib'},
      tests_require	= "nose >=0.10.0b1",
      test_suite	= "nose.collector",
     )
