#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Packing metadata for setuptools."""


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'hamster-lib',
    'flask-restful',
]

setup(
    name='hamster-flask-api',
    version='0.10.0',
    description="A Rest-API using flask.",
    long_description=readme + '\n\n' + history,
    author="Eric Goller",
    author_email='elbenfreund@ninjaduck.solutions',
    url='https://github.com/elbenfreund/hamster-flask-api',
    packages=[
        'hamster_flask_api',
    ],
    package_dir={'hamster_flask_api':
                 'hamster_flask_api'},
    install_requires=requirements,
    entry_points = {
        'console_scripts': ['hamster-flask-api=hamster_flask_api.hamster_flask_api:run']
    },
    license="GPL3",
    zip_safe=False,
    keywords='hamster-flask-api',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
