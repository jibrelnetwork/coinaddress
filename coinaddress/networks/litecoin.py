from .base import BaseNetwork
from .registry import registry


@registry.register('litecoin', 'LTC')
class Litecoin(BaseNetwork):
    pubkey_address_prefix = 0x30
