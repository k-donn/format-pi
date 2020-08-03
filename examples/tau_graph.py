"""Show MultiplePi creating ticks for a tau intervaled graph."""
import matplotlib.pyplot as plt
import numpy as np

from matplot_fmt_pi import MultiplePi

fig = plt.figure()
axes = fig.add_subplot(111)
tau = np.pi * 2
x = np.linspace(-tau / 60, tau * 8 / 60, 512)
axes.plot(x, np.exp(-x) * np.cos(60 * x))

axes.grid(True)
axes.axhline(0, color='black', lw=2)
axes.axvline(0, color='black', lw=2)
axes.set_title("MultiplePi tau formatting")

major_pi_manager = MultiplePi(60, base=tau, symbol=r"\tau")
minor_pi_manager = MultiplePi(240, base=tau, symbol=r"\tau")

axes.xaxis.set_major_locator(major_pi_manager.locator())
axes.xaxis.set_major_formatter(major_pi_manager.formatter())
axes.xaxis.set_minor_locator(minor_pi_manager.locator())

plt.tight_layout()
plt.savefig("./tau_graph.png", dpi=120)
