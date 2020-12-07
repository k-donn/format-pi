"""Test functionality of matplot_fmt_pi on numbers."""

import math
import unittest

from matplot_fmt_pi import ticker
from matplotlib.ticker import FuncFormatter, MultipleLocator


class TestRawValue(unittest.TestCase):
    """Test the returned function."""

    def test_create_class(self):
        """Test instantiation of MultiplePi objects."""
        denom = 1
        manager = ticker.MultiplePi(denominator=denom)

        self.assertIsInstance(manager, ticker.MultiplePi)
        self.assertEqual(manager.denominator, denom)
        self.assertEqual(manager.base, math.pi)
        self.assertEqual(manager.symbol, r"\pi")

        tau = math.pi * 2
        denom2 = 60
        base = tau
        symbol = r"\tau"
        manager2 = ticker.MultiplePi(
            denominator=denom2, base=base, symbol=symbol)

        self.assertEqual(manager2.denominator, denom2)
        self.assertEqual(manager2.base, tau)
        self.assertEqual(manager2.symbol, symbol)

        with self.assertRaises(ValueError):
            ticker.MultiplePi(denominator=-1)

        with self.assertRaises(ValueError):
            ticker.MultiplePi(denominator=0)

        with self.assertRaises(TypeError):
            ticker.MultiplePi(denominator=1.5)

    def test_create_function(self):
        """Test creation of format function."""
        manager = ticker.MultiplePi(denominator=1)

        fmt = manager._make_formatter()

        self.assertIsInstance(fmt, type(lambda a: a))

    def test_create_locator(self):
        """Test returned locator from .locator()."""
        manager = ticker.MultiplePi(denominator=1)

        self.assertIsInstance(manager.locator(), MultipleLocator)

    def test_create_formatter(self):
        """Test returned formatter from .formatter()."""
        manager = ticker.MultiplePi(denominator=1)

        self.assertIsInstance(manager.formatter(), FuncFormatter)

    def test_fmt_one_denom(self):
        """Test values where the denominator of pi is one."""
        manager = ticker.MultiplePi(denominator=1)

        fmt = manager.formatter()

        # correct behaviour
        self.assertEqual(fmt(0), r"$0$")

        self.assertEqual(fmt(math.pi), r"$\pi$")
        self.assertEqual(fmt(-math.pi), r"$-\pi$")

        self.assertEqual(fmt(math.pi * 3), r"$3\pi$")
        self.assertEqual(fmt(-math.pi * 3), r"$-3\pi$")

        self.assertEqual(fmt(math.pi * 24), r"$24\pi$")
        self.assertEqual(fmt(-math.pi * 24), r"$-24\pi$")

    def test_fmt_whole_denom(self):
        """Test values where the denominator is a whole number."""
        # pi/2, pi, 3pi/2, ...
        manager2 = ticker.MultiplePi(denominator=2)

        fmt2 = manager2.formatter()

        # correct behaviour
        self.assertEqual(fmt2(0.5 * math.pi), r"$\frac{\pi}{2}$")
        self.assertEqual(fmt2(-0.5 * math.pi), r"$\frac{-\pi}{2}$")

        self.assertEqual(fmt2(2.5 * math.pi), r"$\frac{5\pi}{2}$")
        self.assertEqual(fmt2(-2.5 * math.pi),
                         r"$\frac{-5\pi}{2}$")

        manager3 = ticker.MultiplePi(denominator=3)

        fmt3 = manager3.formatter()

        # correct behaviour
        self.assertEqual(
            fmt3(0.3333333333333333 * math.pi),
            r"$\frac{\pi}{3}$")
        self.assertEqual(fmt3(-0.3333333333333333 * math.pi),
                         r"$\frac{-\pi}{3}$")

        self.assertEqual(
            fmt3(
                4 * math.pi / 3),
            r"$\frac{4\pi}{3}$")
        self.assertEqual(fmt3(-4 * math.pi / 3),
                         r"$\frac{-4\pi}{3}$")

    def test_fmt_tau(self):
        """Test using MultiplePi for multiples of fractions of tau."""
        tau = math.pi * 2
        base = tau
        symbol = r"\tau"
        manager = ticker.MultiplePi(
            denominator=60, base=base, symbol=symbol)

        fmt = manager.formatter()

        self.assertEqual(fmt(tau / 60), r"$\frac{\tau}{60}$")
        self.assertEqual(fmt(-tau / 60), r"$\frac{-\tau}{60}$")

        self.assertEqual(fmt(2 * tau / 15), r"$\frac{2\tau}{15}$")
        self.assertEqual(fmt(-2 * tau / 15), r"$\frac{-2\tau}{15}$")

        self.assertEqual(fmt(4 * tau / 30), r"$\frac{2\tau}{15}$")
        self.assertEqual(fmt(-4 * tau / 30), r"$\frac{-2\tau}{15}$")


if __name__ == "__main__":
    unittest.main()
