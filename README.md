# Matplotlib Format Pi

## [DOCS](https://k-donn.github.io/format-pi)

## Branches

### Master

| Version                                                                                                               | Upload Status                                                                                                                                                                                                                                              | Downloads                                                                                                                      |
| :-------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| [![PyPI](https://img.shields.io/pypi/v/matplot-fmt-pi?label=PyPi%20package)](https://badge.fury.io/py/matplot-fmt-pi) | [![Upload Python Package](https://img.shields.io/github/workflow/status/k-donn/format-pi/Upload%20Python%20Package?label=Upload%20Python%20Package&logo=github)](https://github.com/k-donn/format-pi/actions?query=workflow%3A%22Upload+Python+Package%22) | [![PyPI - Downloads](https://img.shields.io/pypi/dm/matplot-fmt-pi?logo=pypi)](https://pepy.tech/project/matplot-fmt-pi/month) |

### Release

| Version                                                                                                                                                | Upload Status                                                                                                                                                                                                                                                                 | Size                                                                                             |
| :----------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| [![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/k-donn/format-pi?label=Release)](https://github.com/k-donn/format-pi/tree/release) | [![Upload Python Package](https://img.shields.io/github/workflow/status/k-donn/format-pi/Test%20Upload%20Python%20Package?label=Test%20Upload%20Python%20Package&logo=github)](https://github.com/k-donn/format-pi/actions?query=workflow%3A%22Test+Upload+Python+Package%22) | ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/k-donn/format-pi) |

Format multiples of pi as strings on Matplotlib axes.

The `MultiplePi` class creates a [Locator](https://matplotlib.org/api/ticker_api.html?highlight=locator#matplotlib.ticker.MultipleLocator) to place ticks at desired multiples and a [Formatter](https://matplotlib.org/api/ticker_api.html?highlight=locator#matplotlib.ticker.FuncFormatter) to format all tick labels.

The base (π or τ) can be divided by any Natural Number.

Multiples of one-π or one-τ can be placed/formatted too. (2π, 3π, 2τ, 3τ, etc.)

## Installing

```bash
pip install matplot-fmt-pi
```

## Examples

```python
from matplot_fmt_pi.ticker import MultiplePi
```

Simply, the instance can be asssigned a denominator of pi then passed to matplotlib.

![Graph Example](https://raw.githubusercontent.com/k-donn/format-pi/master/examples/pi_graph.png)

The parameters can also be modified to adjust the output to something more sophisticated.

![Tau Graph Example](https://raw.githubusercontent.com/k-donn/format-pi/master/examples/tau_graph.png)

![Y-Axis Example](https://raw.githubusercontent.com/k-donn/format-pi/master/examples/pi_y_axis.png)

## Running Examples

Clone, then from the repo,

```bash
cd examples/
python *.py
```

Put the repo's directory in the python path to import the `matplot_fmt_pi` folder not the installed package.

```bash
PYTHONPATH=/home/user/py-pros/format-pi python examples/pi_graph.py
```

## Todo

-   [ ] Add testing option once installed (Like `numpy.test()`)
-   [ ] Windows `make.bat`?

## Meta

![PyPI - License](https://img.shields.io/pypi/l/matplot-fmt-pi)

Inspired by [this](https://stackoverflow.com/questions/40642061/how-to-set-axis-ticks-in-multiples-of-pi-python-matplotlib) post on StackOverflow.
