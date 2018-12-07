"""Minimal tests for coin change application"""

from coin_change.usd import USD
from coin_change.cad import CAD
from coin_change.bag import Bag
from coin_change.make_change import MakeChange

class TestMakeChange(object):
    """Tests for MakeChange class go here."""

    def test_usd_167(self):
        usd = USD()
        bag = Bag(usd)
        problem = MakeChange(bag, 167)
        res = problem.run()
        expected = Bag(usd)
        expected.config = {'nickel': 1, 'quarter': 6, 'penny': 2, 'dime': 1}
        assert res == expected

    def test_usd_0(self):
        usd = USD()
        bag = Bag(usd)
        problem = MakeChange(bag, 0)
        res = problem.run()
        expected = Bag(usd)
        expected.config = {'nickel': 0, 'quarter': 0, 'penny': 0, 'dime': 0}
        assert res == expected

    def test_usd_1001(self):
        usd = USD()
        bag = Bag(usd)
        problem = MakeChange(bag, 1001)
        res = problem.run()
        expected = Bag(usd)
        expected.config = {'nickel': 0, 'quarter': 40, 'penny': 1, 'dime': 0}
        assert res == expected

    def test_cad_167(self):
        cad = CAD()
        bag = Bag(cad)
        problem = MakeChange(bag, 167)
        res = problem.run()
        expected = Bag(cad)
        expected.config = {'quarter': 0, 'penny': 2, 'nickel': 1, 'half_loonie': 3, 'dime': 1}
        assert res == expected
