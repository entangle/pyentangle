#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


packages = [
    'entangle',
]

requires = [
    'enum34',
    'python-snappy',
    'msgpack-python',
    'six',
]

tests_require = [
    'nose',
    'rednose',
    'flake8',
]

setup(
    name='entangle',
    version='1.0.0',
    description='Entangle runtime library for Python',
    author='Nick Bruun',
    author_email='nick@bruun.co',
    url='http://bruun.co/',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'entangle': 'entangle'},
    include_package_data=True,
    tests_require=tests_require,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=True,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
