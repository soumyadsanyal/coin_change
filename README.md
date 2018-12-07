*Coin change application supporting multiple currencies*

To install:

1. In this directory, run `pip install .`.

Example usage:

```
from coin_change.usd import USD
from coin_change.bag import Bag
from coin_change.make_change import MakeChange

usd = USD()
bag = Bag(usd)

problem = MakeChange(bag, amount=167)

problem.run()
```

Returns:

```
{'nickel': 1, 'quarter': 6, 'penny': 2, 'dime': 1}
```
