from .base import BaseNetwork
from .registry import registry


@registry.register('bitcoin', 'BTC')
class Bitcoin(BaseNetwork):
    pass
