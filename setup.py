#!/usr/bin/env python

from setuptools import setup, find_packages
from os.path import join, dirname
import rut

setup(
    name='rut',
    version='0.0.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts': ['rut = rut.main:main']
        },
    )
