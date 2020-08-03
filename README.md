# Matplotlib Format Pi

| Version                                                                                                 | Upload Status                                                                                                                                                                                                                    | Downloads                                                                                                    |
| :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| [![PyPi version](https://badge.fury.io/py/matplot-fmt-pi.svg)](https://badge.fury.io/py/matplot-fmt-pi) | [![Upload Python Package](https://github.com/k-donn/format-pi/workflows/Upload%20Python%20Package/badge.svg?branch=master&event=push)](https://github.com/k-donn/format-pi/actions?query=workflow%3A%22Upload+Python+Package%22) | [![Downloads](https://pepy.tech/badge/matplot-fmt-pi/month)](https://pepy.tech/project/matplot-fmt-pi/month) |

[![Test Upload Python Package](https://github.com/k-donn/format-pi/workflows/Test%20Upload%20Python%20Package/badge.svg?branch=release)](https://github.com/k-donn/format-pi/actions?query=workflow%3A%22Test+Upload+Python+Package%22)

Format multiples of pi as strings on Matplotlib axes.

The `MultiplePi` class creates a [Locator](https://matplotlib.org/api/ticker_api.html?highlight=locator#matplotlib.ticker.MultipleLocator) to place ticks at desired multiples and a [Formatter](https://matplotlib.org/api/ticker_api.html?highlight=locator#matplotlib.ticker.FuncFormatter) to format all tick labels.

The base (π or τ) can be divided by any Natural Number.

Multiples of one-π or one-τ can be placed/formatted too. (2π, 3π, 2τ, 3τ, etc.)

## Installing

```bash
pip install matplot-fmt-pi
```

## Examples

Simply, the instance can be asssigned a denominator of pi then passed to matplotlib.

![Graph Example](https://raw.githubusercontent.com/k-donn/format-pi/master/examples/pi_graph.png)

The parameters can also be modified to adjust the output to something more sophisticated.

![Tau Graph Example](https://raw.githubusercontent.com/k-donn/format-pi/master/examples/tau_graph.png)

![Y-Axis Example](https://raw.githubusercontent.com/k-donn/format-pi/master/examples/pi_y_axis.png)

## Running Examples

[Install](#Installing) then from the repo,

```bash
cd examples/
python *.py
```

Put the repo's directory in the python path to import the `matplot_fmt_pi` folder not the installed package.

```bash
PYTHONPATH=/home/user/py-pros/format-pi python examples/pi_graph.py
```

## Todo

-   [ ] Add type stubs

## Meta

Inspired by [this](https://stackoverflow.com/questions/40642061/how-to-set-axis-ticks-in-multiples-of-pi-python-matplotlib) post on StackOverflow.
