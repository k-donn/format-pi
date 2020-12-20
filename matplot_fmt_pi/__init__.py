"""
Help with showing multiples of pi on Matplotlib plots.

Classes available format numbers as exact multiples of pi on plots
instead of showing them as decimals.

The class MultiplePi contains the math and formatting to accomplish this.
MultiplePi has methods to return a Locator and FuncFormatter for use on a plot.
Ticks are placed at exact multiples and the exact multiples are shown on the
plot.


Modules include:
    :mod:`matplot_fmt_pi.ticker`
        Contains MultiplePi class

Note
----
Matplotlib has a basic_units.py module that can do this, however,
it can only do format multiples of pi/2.
In addition, it forces use of its own cos, sin, etc.
while this is far more extensible.
"""

__version__ = "2.0.4"
__name__ = "matplot_fmt_pi"
__pie__ = "Tastes good"
