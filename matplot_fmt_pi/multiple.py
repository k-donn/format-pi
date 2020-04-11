"""The multiple module defines the MultiplePi class."""
import math
from typing import Any, Callable

import numpy as np
from matplotlib.ticker import FuncFormatter, MultipleLocator


class MultiplePi:
    r"""
    Handle formatting of numbers as multiples of pi.

    An instance can be constructed, then, the methods can be called and passed to
    the matplotlib formatting and locating methods.

    Attributes
    ----------
    denominator : `int`
        The denominator of the multiples desired.

    base : `float`, optional
        Number to find multiples of, by default math.pi

    symbol : `str`, optional
        Symbol to place in string of multiple, by default r"\pi"

    Methods
    -------
    locator()
        Return the locator instance

    formatter()
        Return the formatter instance


    Example
    -------
    >>> pi_controller = MultiplePi(3) # For pi/3 and multiples of
    >>> axes_instance.set_major_formatter(pi_controller.formatter()) # Turn values into the fraction
    >>> axes_instance.set_major_locator(pi_controller.locator()) # Will put ticks at multiples of pi/3

    Notes
    -----
    The symbol is rendered inside a latex equation by matplotlib. Non-latex characters
    can also be used.

    Set symbol to a different value when base is a different value. (tau possibly)


    """

    def __init__(self, denominator: int, base: float = math.pi,
                 symbol: str = r"\pi"):
        """Initialize self."""
        self.denominator = denominator
        self.base = base
        self.symbol = symbol

    def locator(self) -> MultipleLocator:
        """Return the locator with ticks at multiples of base via denominator.

        Returns
        -------
        `MultipleLocator`
            The object used to space the ticks
        """
        return MultipleLocator(self.base / self.denominator)

    def formatter(self) -> FuncFormatter:
        """Return the formatter for multiple ticks.

        Returns
        -------
        `FuncFormatter`
            Used to insert the symbol into the multiples
        """
        return FuncFormatter(self._make_formatter())

    def _make_formatter(self) -> Callable[[float, Any], str]:
        """Return the function used by the FuncFormatter instance.

        Returns
        -------
        `Callable[[float, Any], str]`
            Accpes a value and a position parameter and transforms them
        """
        def _fmt(theta, _pos=1) -> str:
            """Transform the passed value into the proper representation of the multiple.

            Parameters
            ----------
            theta : `float`
                The angle in radians to be transformed
            _pos : `int`, optional
                Index of the tick on the axis, by default 1

            Returns
            -------
            `str`
                The final label to be shown on the axis
            """
            denom = self.denominator
            # Find raw numerator by finding how many (denom)s are in (theta)
            # eg. How many pi/4 are in 1.5pi? (6)
            numer = np.int(np.rint(denom * theta / self.base))

            # Simplify the raw (numer) to lowest eg. 6/4 to 3/2
            com = self._gcd(numer, denom)

            # Simplify by dividing raw (numer) and (denom) by GCD
            (numer, denom) = (int(numer / com), int(denom / com))

            # If an integer of base
            if denom == 1:
                if numer == 0:
                    return r"$0$"

                # When numer simplifies to be +/- 1
                if numer in (-1, 1):
                    return r"${0}{1}$".format(
                        "-" if numer == -1 else "", self.symbol)

                # Just (multiple) * (base)
                return r"${0}{1}$".format(numer, self.symbol)

            # between inetegers of base
            # When numer simplifies to be +/- 1
            if numer in (-1, 1):
                return r"$\frac{{{0}{2}}}{{{1}}}$".format(
                    "-" if numer == -1 else "", denom, self.symbol)

            # Simplified ((numer) * (base))/(denom)
            return r"$\frac{{{0}{2}}}{{{1}}}$".format(
                numer, denom, self.symbol)

        return _fmt

    @staticmethod
    def _gcd(int_1: float, int_2: float) -> float:
        """Return the Greatest Common Divisor of int_1 and int_2.

        AKA, greatest common factor or greatest common measure.

        Parameters
        ----------
        int_1 : `float`
            First integer

        int_2 : `float`
            Second integer

        Returns
        -------
        `float`
            The largest positive integer that divides each of the integers
        """
        while int_2:
            int_1, int_2 = int_2, int_1 % int_2
        return int_1
