#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copyright 2020 Devon (Gorialis) R

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import pathlib

from setuptools import setup


ROOT = pathlib.Path(__file__).parent
VERSION = "2020.10.30"

# 3.5 and lower doesn't support using pathlib.Path objects directly in open
with open(str(ROOT / 'README.rst'), 'r', encoding='utf-8') as f:
    README = f.read()


setup(
    name="ttf-opensans",
    author="Devon (Gorialis) R",
    url="https://github.com/Gorialis/ttf-opensans",

    license='Apache 2.0',
    description='ttf-opensans is a Python package vending the Open Sans font by Steve Matteson.',
    long_description=README,
    long_description_content_type='text/x-rst',
    project_urls={
        'Code': 'https://github.com/Gorialis/ttf-opensans',
        'Issue tracker': 'https://github.com/Gorialis/ttf-opensans/issues'
    },

    version=VERSION,
    packages=['ttf_opensans'],
    include_package_data=True,
    install_requires=[],
    python_requires='>=3.4.0',

    download_url='https://github.com/Gorialis/ttf-opensans/archive/v{}.tar.gz'.format(VERSION),

    keywords='font fonts ttf',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Text Processing :: Fonts',
    ]
)
