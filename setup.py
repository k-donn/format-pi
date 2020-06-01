"""Install the module."""
import pathlib
from setuptools import setup

# The dir containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="matplot-fmt-pi",
    version="1.5.0",
    description="Format numbers as multiples of Pi",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/k-donn/format-pi",
    author="k-donn",
    author_email="k-donn@github.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    keywords=[
        "matplotlib",
        "formatter",
        "locator",
        "axes ticks",
        "numbers",
        "radians"
        "multiples",
        "of",
        "pi",
    ],
    packages=["matplot_fmt_pi"],
    install_requires=["numpy", "matplotlib"]
)
