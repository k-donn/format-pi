# Matplotlib Format Pi

[![Upload Python Package](https://github.com/k-donn/format-pi/workflows/Upload%20Python%20Package/badge.svg?branch=master&event=push)](https://github.com/k-donn/format-pi/actions?query=workflow%3A%22Upload+Python+Package%22)
[![Downloads](https://pepy.tech/badge/matplot-fmt-pi/month)](https://pepy.tech/project/matplot-fmt-pi/month)
[![PyPI version](https://badge.fury.io/py/matplot-fmt-pi.svg)](https://badge.fury.io/py/matplot-fmt-pi)

Create locator and formatter instances to make x/y labels and ticks correspond to multiples of pi.

The `MultiplePi` class provides methods to seamlessly tell matplotlib to create and format tick labels as multiples of pi.

In addition, the `MultiplePi` class allows a user to change the denominator of pi.

Multiples of π/{2, 3, 4, ...} can be represented if needed.

## Examples

Simply, the instance can be asssigned a denominator of pi then passed to matplotlib.

![Graph Example](./examples/graph.png)

The parameters can also be modified to adjust the output to something more sophisticated.

![Tau Graph Example](./examples/tau_graph.png)

## Todo

1.  Raise error for improper usage (plugging in 1/4 for a multiple of 1/3)

## Meta

Inspired by [this](https://stackoverflow.com/questions/40642061/how-to-set-axis-ticks-in-multiples-of-pi-python-matplotlib) post on StackOverflow.
