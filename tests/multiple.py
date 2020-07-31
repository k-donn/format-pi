"""Test functionality of matplot_fmt_pi on numbers."""

import math
import unittest

from matplot_fmt_pi import multiple


class TestRawValue(unittest.TestCase):
    """Test the returned function."""

    def test_create_class(self):
        """Test instantiation of MultiplePi objects."""
        denom = 1
        manager = multiple.MultiplePi(denominator=denom)

        self.assertIsInstance(manager, multiple.MultiplePi)
        self.assertEqual(manager.denominator, denom)
        self.assertEqual(manager.base, math.pi)
        self.assertEqual(manager.symbol, r"\pi")

        tau = math.pi * 2
        denom2 = 60
        base = tau
        symbol = r"\tau"
        manager2 = multiple.MultiplePi(
            denominator=denom2, base=base, symbol=symbol)

        self.assertEqual(manager2.denominator, denom2)
        self.assertEqual(manager2.base, tau)
        self.assertEqual(manager2.symbol, symbol)

        with self.assertRaises(ValueError):
            multiple.MultiplePi(denominator=-1)

        with self.assertRaises(ValueError):
            multiple.MultiplePi(denominator=0)

        with self.assertRaises(TypeError):
            multiple.MultiplePi(denominator=1.5)

    def test_create_function(self):
        """Test creation of format function."""
        manager = multiple.MultiplePi(denominator=1)

        fmt = manager._make_formatter()

        self.assertIsInstance(fmt, type(lambda a: a))

    def test_one_denom(self):
        """Test values where the denominator of pi is one."""
        manager = multiple.MultiplePi(denominator=1)

        fmt = manager._make_formatter()

        # correct behaviour
        self.assertEqual(fmt(math.pi), r"$\pi$")
        self.assertEqual(fmt(-math.pi), r"$-\pi$")

        self.assertEqual(fmt(math.pi * 3), r"$3\pi$")
        self.assertEqual(fmt(-math.pi * 3), r"$-3\pi$")

        self.assertEqual(fmt(math.pi * 24), r"$24\pi$")
        self.assertEqual(fmt(-math.pi * 24), r"$-24\pi$")

        # correct behaviour when improperly used
        with self.assertRaises(ValueError):
            # Should be multiples of one
            fmt(math.pi * 1.5)
            fmt(-math.pi * 1.5)

    def test_whole_denom(self):
        """Test values where the denominator is a whole number."""
        # pi/2, pi, 3pi/2, ...
        manager2 = multiple.MultiplePi(denominator=2)

        fmt2 = manager2._make_formatter()

        # correct behaviour
        self.assertEqual(fmt2(0.5 * math.pi), r"$\frac{\pi}{2}$")
        self.assertEqual(fmt2(-0.5 * math.pi), r"$\frac{-\pi}{2}$")

        self.assertEqual(fmt2(2.5 * math.pi), r"$\frac{5\pi}{2}$")
        self.assertEqual(fmt2(-2.5 * math.pi), r"$\frac{-5\pi}{2}$")

        manager3 = multiple.MultiplePi(denominator=3)

        fmt3 = manager3._make_formatter()

        # correct behaviour
        self.assertEqual(
            fmt3(
                0.3333333333333333 *
                math.pi),
            r"$\frac{\pi}{3}$")
        self.assertEqual(fmt3(-0.3333333333333333 * math.pi),
                         r"$\frac{-\pi}{3}$")

        self.assertEqual(fmt3(4 * math.pi / 3), r"$\frac{4\pi}{3}$")
        self.assertEqual(fmt3(-4 * math.pi / 3), r"$\frac{-4\pi}{3}$")

        # correct behaviour when improperly used
        with self.assertRaises(ValueError):
            fmt3(math.pi / 4)
            fmt3(-math.pi / 4)

    def test_tau(self):
        """Test using MultiplePi for multiples of fractions of tau."""
        tau = math.pi * 2
        base = tau
        symbol = r"\tau"
        manager = multiple.MultiplePi(
            denominator=60, base=base, symbol=symbol)

        fmt = manager._make_formatter()

        self.assertEqual(fmt(tau / 60), r"$\frac{\tau}{60}$")
        self.assertEqual(fmt(-tau / 60), r"$\frac{-\tau}{60}$")

        self.assertEqual(fmt(2 * tau / 15), r"$\frac{2\tau}{15}$")
        self.assertEqual(fmt(-2 * tau / 15), r"$\frac{-2\tau}{15}$")

        self.assertEqual(fmt(4 * tau / 30), r"$\frac{2\tau}{15}$")
        self.assertEqual(fmt(-4 * tau / 30), r"$\frac{-2\tau}{15}$")

        # correct behaviour when improperly used
        with self.assertRaises(ValueError):
            fmt(tau / 45)
            fmt(-tau / 45)


if __name__ == "__main__":
    unittest.main()
