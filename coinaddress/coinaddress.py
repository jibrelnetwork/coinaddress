"""Main module."""
from .networks import registry
from .networks.base import BaseNetwork


def get_network(name: str) -> BaseNetwork:
    return registry.get(name)


def address_from_xpub(network: str, xpub: str, path: str = '0') -> str:
    """Get address derived from xpub.
    """
    net = get_network(network)
    return net.get_address(xpub=xpub, path=path)
