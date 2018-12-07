"""Module provides class implementing a bag of coins to make change for a given amount of money.

Args:
    currency: Currency
    amount: int

Methods:
    bag_value: int
    coin_count: int

Overrides:
    __lt__: compare two bags by the value of coin_count; permits a total order
    on bags
    __eq__: equality on number of coins of each denomination (used in test
    assertions)
    __add__: combines two bags of a certain currency by adding the coins of each
    denomination in each
    __repr__: represents the bag by a dictionary of denomination:count pairs
"""

from copy import deepcopy

class Bag(object):
    """Bag of coins, parametrized by denomination."""

    def __init__(self, currency, amount=0):
        """config records how many coins of each denomination is in the bag"""
        self.currency = currency
        self.config = {coin:0 for coin in self.currency.denominations}
        self.amount = amount

        #allow for instantating primitive bags with exactly one coin of some
        #denomination
        if self.amount > 0:
            for coin in self.config.keys():
                if self.currency.coin_value(coin) == self.amount:
                    self.config[coin] += 1
            if self.coin_count <= 0:
                raise ValueError(
                    """could not correctly
                     instantiate bag using amount {}""".format(self.amount))

    @property
    def coin_count(self):
        """number of coins in bag"""
        return sum(self.config.values())

    @property
    def bag_value(self):
        """total value of bag in currency units"""
        return sum(
            map(
                lambda p: reduce(lambda r, x: r*x, p, 1),
                zip(self.config.values(), map(
                    self.currency.coin_value, self.config.keys()))
            )
        )

    def __lt__(self, other):
        """implement a total ordering on bags by number of coins used"""
        return self.coin_count < other.coin_count

    def __add__(self, other):
        """returns new instance and does not modify self"""
        _self = deepcopy(self)
        for coin in _self.config:
            _self.config[coin] += other.config[coin]
        return _self

    def __eq__(self, other):
        """equality on configs"""
        return self.config == other.config

    def __repr__(self):
        """string representation of config"""
        return """{}""".format(self.config)
