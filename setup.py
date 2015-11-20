#!/usr/bin/env python
"""
Soprano - A library for cracking crystals!
by Simone Sturniolo et al.
Copyright whatever whatever (TODO)

v 0.1
"""

# Python 2-to-3 compatibility code
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from distutils.core import setup

setup(name='Soprano',
      version='0.1',
      packages=['soprano'],
      # For data files. Example: 'soprano': ['data/*.json']
      package_data={'soprano': 'data/*.json'},
      # For scripts - just put the paths
      scripts=[],
      )
