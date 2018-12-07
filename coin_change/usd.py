"""USD as instance of Currency.
"""

from coin_change.currency import Currency

class USD(Currency):
    """Instance of Currency, initialized with hash specifying values of
    quarters, dimes, nickels and pennies.
    """

    def __init__(self):
        super(USD, self).__init__()
        self.denominations = {"quarter":25, "dime":10, "nickel":5, "penny":1}
        self._set_attributes()
