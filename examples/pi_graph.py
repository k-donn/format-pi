"""Show a simple example of using MultiplePi."""
import matplotlib.pyplot as plt
import numpy as np

from matplot_fmt_pi import MultiplePi

fig = plt.figure(figsize=(4*np.pi, 2.4))
axes = fig.add_subplot(111)
x = np.linspace(-2*np.pi, 2*np.pi, 512)
axes.plot(x, np.sin(x))

axes.grid(True)
axes.axhline(0, color='black', lw=2)
axes.axvline(0, color='black', lw=2)
axes.set_title("MultiplePi formatting")

pi_manager = MultiplePi(2)
axes.xaxis.set_major_locator(pi_manager.locator())
axes.xaxis.set_major_formatter(pi_manager.formatter())

plt.tight_layout()
plt.savefig("./pi_graph.png", dpi=120)