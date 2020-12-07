"""Show a simple example of using MultiplePi."""
import math

import matplotlib.pyplot as plt
import numpy as np
from matplot_fmt_pi.ticker import MultiplePi
from matplotlib.ticker import MultipleLocator

fig = plt.figure(figsize=(4 * np.pi, 2.4))
axes = fig.add_subplot(111)
x = np.linspace(-2 * np.pi, 2 * np.pi, 512)
axes.plot(x, np.sin(x))

axes.grid(True)
axes.axhline(0, color='black', lw=2)
axes.axvline(0, color='black', lw=2)
axes.set_title("MultiplePi Wrong formatting (duplicates)")

# Expect pi/2
pi_manager = MultiplePi(denominator=2)

# Proper usage:
# loc = pi_manager.locator()


# Improper: give pi/3
loc = MultipleLocator(math.pi / 3)
axes.xaxis.set_major_locator(loc)
axes.xaxis.set_major_formatter(pi_manager.formatter())

plt.tight_layout()

plt.savefig("./wrong_graph.png", dpi=120)
