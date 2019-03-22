# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyriandx',
    version='0.1.0',
    description='Simple API wrapper for Pieriandx web services',
    long_description=readme,
    author='Nicholas Clark',
    author_email='nick.clark@umccr.org',
    url='https://github.com/umccr/pyriandx',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

