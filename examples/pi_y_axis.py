"""Show an example of using MultiplePi on the y-axis."""
import matplotlib.pyplot as plt
import numpy as np

from matplot_fmt_pi import MultiplePi

x = np.arange(-10.0, 10.0, 0.1)
y = np.arctan(x)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title("MultiplePi formatting")
ax.plot(x, y, 'b.')

y_pi = y / np.pi
unit = 0.25
y_tick = np.arange(-0.5, 0.5 + unit, unit)

# New way
manager = MultiplePi(4)
ax.yaxis.set_major_locator(manager.locator())
ax.yaxis.set_major_formatter(manager.formatter())

# Other way
y_label2 = [r"$" + format(r, ".2g") + r"\pi$" for r in y_tick]
ax2 = ax.twinx()
ax2.set_yticks(y_tick * np.pi)
ax2.set_yticklabels(y_label2)

plt.savefig("./pi_y_axis.png", dpi=120)
