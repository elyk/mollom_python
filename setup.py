#!/usr/bin/env python

from distutils.core import setup

setup(name='mollom_python',
      version='1.0',
      description='A python client library for the Mollom REST API',
      author='Huan Lai',
      author_email='huan.lai@acquia.com',
      url='https://github.com/Mollom/mollom_python',
      requires=['requests_oauthlib'],
     )