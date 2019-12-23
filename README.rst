===========
coinaddress
===========


.. image:: https://img.shields.io/pypi/v/coinaddress.svg
        :target: https://pypi.python.org/pypi/coinaddress

.. image:: https://img.shields.io/travis/jibrelnetwork/coinaddress.svg
        :target: https://travis-ci.org/jibrelnetwork/coinaddress

.. image:: https://readthedocs.org/projects/coinaddress/badge/?version=latest
        :target: https://coinaddress.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/jibrelnetwork/coinaddress/shield.svg
     :target: https://pyup.io/repos/github/jibrelnetwork/coinaddress/
     :alt: Updates



Crypto address generator from xpub


* Free software: MIT license
* Documentation: https://coinaddress.readthedocs.io.


Features
--------

* generate addresses for multiple blockchains from extended public key (xpub)
* minimum dependency (it means security)
* CLI interface

Getting started
---------------

Install package using pip (prefer virtualenv):

    pip install coinaddress

And you can start use provided CLI. Read help first:

    coinaddress --help

To generate 1000 addresses for bitcoin xpub from file (xpub should be a single line in this file):

    cat xpub.txt | coinaddress bitcoin 0 -n 1000

To generate another bunch of addresses:

    cat xpub.txt | coinaddress bitcoin 1000 -n 1000

xpub can be passed with `--xpub` option but you should avoid this and prefer read from file for security reasons.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
