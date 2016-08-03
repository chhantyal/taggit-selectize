#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import taggit_selectize

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = taggit_selectize.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py bdist_wheel')
    os.system('python setup.py sdist')
    os.system('twine upload dist/*')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='taggit-selectize',
    version=version,
    description="""django-taggit + selectize.js""",
    long_description="""Auto-complete/auto-suggestion for django-taggit.""",
    author='Nar Chhantyal',
    author_email='nkchhantyal@gmail.com',
    url='https://github.com/chhantyal/taggit-selectize',
    packages=[
        'taggit_selectize',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='taggit-selectize',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
