"""Instance of Currency, initialized with hash specifying values of
half-loonies, quarters, dimes, nickels and pennies.
"""

from coin_change.currency import Currency

class CAD(Currency):
    """Instance of Currency, initialized with hash specifying values of
    half-loonies, quarters, dimes, nickels and pennies.
    """


    def __init__(self):
        super(CAD, self).__init__()
        self.denominations = {"half_loonie":50, "quarter":25, "dime":10, "nickel":5, "penny":1}
        self._set_attributes()
