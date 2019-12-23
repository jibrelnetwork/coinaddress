"""Top-level package for coinaddress."""

__author__ = """Roman Tolkachyov"""
__email__ = 'roman@tolkachyov.name'
__version__ = '0.1.1'

from .coinaddress import address_from_xpub

__all__ = [
    'address_from_xpub'
]
