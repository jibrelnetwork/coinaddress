#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'ecdsa>=0.14.1',
    'base58>=1.0.3',
    'crypto>=1.4.1',
    'pysha3>=1.0.2',
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Roman Tolkachyov",
    author_email='roman@tolkachyov.name',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Crypto address generator from xpub",
    entry_points={
        'console_scripts': [
            'coinaddress=coinaddress.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='coinaddress',
    name='coinaddress',
    packages=find_packages(include=['coinaddress', 'coinaddress.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jibrelnetwork/coinaddress',
    version='0.1.1',
    zip_safe=False,
)
