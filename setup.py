#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages


setup(
    name='django-intellectmoney',
    version='0.0.4',
    author='Ivan Petukhov',
    author_email='satels@gmail.com',
    packages=find_packages(exclude=['docs', 'tests']),
    platforms=['Any'],
    python_requires='>=3.6, <4',
    url='https://github.com/satels/django-intellectmoney',
    keywords=['django', 'intellectmoney'],
    download_url='https://github.com/satels/django-intellectmoney/zipball/master',
    license='MIT license',
    description=u'Приложение для работы с intellectmoney.ru.',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
    install_requires=[],
    include_package_data=True,
)
