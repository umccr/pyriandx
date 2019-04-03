# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

from pyriandx import __version__, __author__, __title__, __description__
with open('LICENSE') as f:
    license = f.read()

here = os.path.dirname(__file__)
with open(os.path.join(here, 'requirements.txt')) as f:
    packages = f.readlines()

setup(
    name='pyriandx',
    version=__version__,
    description=__description__,
    long_description=open('README.md').read(),
    author=__author__,
    url='https://github.com/umccr/pyriandx',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'pyriandx': ['json/*.json']},
    install_requires=packages,
    entry_points = {'console_scripts': ['pyriandx=pyriandx.__main__:main']}
)

