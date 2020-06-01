"""
Format numbers as multiples of pi for matplotlib plots.

The class MultiplePi contains the math and formatting to accomplish this.
MultiplePi has methods to return a locator and formatter for use on a plot.

Note
----
Matplotlib has a basic_units.py module that can do this, however, it can only do denominators of 2.
In addition, it forces use of its own cos, sin, etc. functions while this is far more extensible.

classes include:
    MultiplePi
        contains everything needed
"""
from .multiple import MultiplePi

__version__ = "1.5.0"
__name__ = "Matplotlib Format Pi"
__pie__ = "Tastes good"
