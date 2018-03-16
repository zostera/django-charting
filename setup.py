#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import charting

from setuptools import setup

version = charting.__version__

if sys.argv[-1] == 'publish':
    # os.system('cd docs && make html')
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='django-charting',
    version=version,
    description="""Charts for Django made simple""",
    long_description=readme + '\n\n' + history,
    author='Dylan Verheul',
    author_email='dylan@zostera.nl',
    url='https://github.com/zostera/django-charts',
    packages=[
        "charting",
    ],
    include_package_data=True,
    install_requires=[
        "Django > 1.4",
    ],
    license="Apache License 2.0",
    zip_safe=False,
    keywords='django-charting',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
