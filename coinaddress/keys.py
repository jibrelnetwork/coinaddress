import hashlib
import hmac
from binascii import hexlify, unhexlify

from ecdsa.curves import SECP256k1
from ecdsa.ecdsa import Public_key as ECDSAPublicKey

from .utils import int_to_hex, create_verifying_key


class PublicKey:

    def __init__(self, chain_code, verifying_key):
        self.verifying_key = verifying_key
        self.chain_code = chain_code

    def get_child_from_path(self, path: str):
        parts = path.split('/')
        node = self
        for p in parts:
            if 'm' in p or "'" in p:
                raise RuntimeError("Can't be used to generate private keys")
            part_index = int(p)
            if part_index < 0:
                raise ValueError("Index can't be less than 0")
            node = node.get_child(part_index)
        return node

    def get_child(self, child_number):
        """Derive a child key.

        :param child_number: The number of the child key to compute
        :type child_number: int

        This derivation is fully described at
        https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki#child-key-derivation-functions  # noqa
        """

        child_number_hex = int_to_hex(child_number, 8)

        data = self.hex()

        data += child_number_hex

        # Compute a 64 Byte `i_full` that is the HMAC-SHA512, using
        # self.chain_code as the seed, and data as the message.
        i_full = hmac.new(
            unhexlify(self.chain_code),
            msg=unhexlify(data),
            digestmod=hashlib.sha512
        ).digest()
        # split `i_full` into its 32 Byte components.
        i_left, i_right = i_full[:32], i_full[32:]

        c_i = hexlify(i_right)

        # only use public information for this derivation
        g = SECP256k1.generator
        i_left_int = int(hexlify(i_left), 16)
        point = (
            ECDSAPublicKey(g, g * i_left_int).point +
            self.verifying_key.pubkey.point
        )
        # `i_right` is the child's chain code

        child = self.__class__(
            chain_code=c_i,
            verifying_key=create_verifying_key(point.x(), point.y())
        )

        return child

    @property
    def point(self):
        return self.verifying_key.pubkey.point

    def hex(self) -> bytes:
        x, y = self.point.x(), self.point.y()
        parity = 2 + (y & 1)  # 0x02 even, 0x03 odd
        return int_to_hex(parity, 2) + int_to_hex(x, 64)

    def __bytes__(self) -> bytes:
        nbytes = self.verifying_key.curve.baselen
        x = self.point.x().to_bytes(nbytes, 'big')
        y = self.point.y().to_bytes(nbytes, 'big')
        return bytes([0x04]) + x + y
