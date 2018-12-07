"""
Implements bottom-up dynamic programming approach to making change for a given
amount.

Args:
    bag: Bag (represents an initialized bag of currency to start the problem.)
    amount: int (amount for which we want to make change)

Methods:
    run: runs the coin change app and returns the optimal bag of change (with
    fewest coins used
"""

from coin_change.bag import Bag

class MakeChange(object):
    """Implements bottom-up dynamic programming approach to coin-change
    problem."""

    def __init__(self, bag, amount):
        self.bag = bag
        self.amount = amount
        self.amounts = range(1, amount+1)
        self.cache = {}

    def run(self):
        """
        If amount is 0 or negative, return trivial bag

        If amount is > 0, populate each value from 1 to amount (inclusive) with
        the optimal bag of change for that amount.

        The critical step here is to query prior subproblems for optimal bags of
        change, once for each value of a coin in the currency, and choose the
        bag with the fewest coins used.

        This choice is delegated to the `min`
        operator, which uses our implementation of `__lt__` to find a bag with
        the smallest coin count.

        Then, the optimal bag for the current problem
        is produced by augmenting the chosen bag with exactly one coin of the
        appropriate denomination. E.g.: if the optimal subproblem bag came from
        dropping a nickel from the current amount, we would take that optimal
        bag and add a nickel to it for the solution to the current problem. This
        combination operation is implemented by the __add__ override in Bag, and
        essentially adds together the configs as dictionaries.
        """
        if self.amount < 1:
            return Bag(self.bag.currency)
        for amount in self.amounts:
            if amount in self.bag.currency.coin_values:
                self.cache[amount] = Bag(self.bag.currency, amount)
            else:
                tmp = {c:self.cache[amount-c] for c in self.bag.currency.coin_values if c <= amount}
                if tmp:
                    lightest_bag = min(tmp.values())
                    self.cache[amount] = min(
                        tmp.values()) + Bag(
                            self.bag.currency,
                            amount - lightest_bag.bag_value)

        result = self.cache.get(self.amount, {})
        return result
