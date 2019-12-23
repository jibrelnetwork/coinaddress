from binascii import hexlify
from sha3 import keccak_256

from .base import BaseNetwork
from .registry import registry


def to_checksum_address(value):
    norm_address = value.lower()
    address_hash = '0x' + hexlify(
        keccak_256(norm_address[2:].encode()).digest()
    ).decode('ascii')

    checksum_address = "".join(
        (
            norm_address[i].upper()
            if int(address_hash[i], 16) > 7
            else norm_address[i]
        )
        for i in range(2, 42)
    )
    return '0x%s' % checksum_address


@registry.register('ethereum', 'ETH')
class Ethereum(BaseNetwork):
    def public_key_to_address(self, node):
        pk_bytes = bytes(node)
        keccak = keccak_256(pk_bytes[1:]).digest()
        eth_address = '0x%s' % hexlify(keccak[12:]).decode('ascii')
        return to_checksum_address(eth_address)
