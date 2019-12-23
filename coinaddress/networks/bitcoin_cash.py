from base58 import b58decode_check

from .base import BaseNetwork
from .registry import registry

CHARSET = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l'


def b32encode(inputs):
    out = ''
    for char_code in inputs:
        out += CHARSET[char_code]
    return out


def polymod(values):
    chk = 1
    generator = [
        (0x01, 0x98f2bc8e61),
        (0x02, 0x79b76d99e2),
        (0x04, 0xf33e5fb3c4),
        (0x08, 0xae2eabe2a8),
        (0x10, 0x1e4f43e470)]
    for value in values:
        top = chk >> 35
        chk = ((chk & 0x07ffffffff) << 5) ^ value
        for i in generator:
            if top & i[0] != 0:
                chk ^= i[1]
    return chk ^ 1


def prefix_expand(prefix):
    return [ord(x) & 0x1f for x in prefix] + [0]


def calculate_checksum(prefix, payload):
    poly = polymod(prefix_expand(prefix) + payload + [0, 0, 0, 0, 0, 0, 0, 0])
    out = list()
    for i in range(8):
        out.append((poly >> 5 * (7 - i)) & 0x1f)
    return out


def convertbits(data, frombits, tobits, pad=True):
    acc = 0
    bits = 0
    ret = []
    maxv = (1 << tobits) - 1
    max_acc = (1 << (frombits + tobits - 1)) - 1
    for value in data:
        if value < 0 or (value >> frombits):
            return None
        acc = ((acc << frombits) | value) & max_acc
        bits += frombits
        while bits >= tobits:
            bits -= tobits
            ret.append((acc >> bits) & maxv)
    if pad:
        if bits:
            ret.append((acc << (tobits - bits)) & maxv)
    elif bits >= frombits or ((acc << (tobits - bits)) & maxv):
        return None
    return ret


@registry.register('bitcoin_cash', 'BCH')
class BitcoinCash(BaseNetwork):
    pubkey_address_prefix = 0x1C

    def public_key_to_address(self, public_key):
        version_int = 0
        prefix = 'bitcoincash'

        pub_key = super().public_key_to_address(public_key)
        payload = list(b58decode_check(pub_key)[1:])

        payload = [version_int] + payload
        payload = convertbits(payload, 8, 5)
        checksum = calculate_checksum(prefix, payload)
        return prefix + ':' + b32encode(payload + checksum)
