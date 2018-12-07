"""Currency base class, to be extended with denomination:value hash.
"""

class Currency(object):
    """Minimal interface for defining currencies."""

    def __init__(self):
        self.denominations = {}
        self._set_attributes()

    def _set_attributes(self):
        """setting class attributes from initialization hash"""
        for key, val in self.denominations.iteritems():
            setattr(self, key, val)

    def coin_value(self, coin):
        """returns coin value in currency
        e.g.: quarter -> 25
        """
        return getattr(self, coin)

    @property
    def coin_values(self):
        """array of all coin values in currency"""
        return map(self.coin_value, self.denominations)
