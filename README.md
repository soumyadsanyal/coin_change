*Coin change application supporting multiple currencies*

To install:

1. `git clone https://github.com/soumyadsanyal/coin_change`
2. `cd coin_change`
3. `pip install .`.

To run test suites:

1. `pytests tests/tests.py`

To use provided classes:

```
from coin_change.usd import USD
from coin_change.bag import Bag
from coin_change.make_change import MakeChange

>>> usd = USD()
>>> bag = Bag(usd)

>>> problem = MakeChange(bag, amount=167)

>>> problem.run()
```

Returns:

```
{'nickel': 1, 'quarter': 6, 'penny': 2, 'dime': 1} (representation of `Bag`
type)
```
