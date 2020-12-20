"""Install the module."""
import pathlib
from setuptools import setup

# The dir containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="matplot-fmt-pi",
    version="2.0.4",
    description="Format numbers as multiples of Pi",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/k-donn/format-pi",
    author="k-donn",
    author_email="k-donn@github.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Framework :: Matplotlib",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    keywords=[
        "matplotlib",
        "formatter",
        "locator",
        "axes ticks",
        "numbers",
        "radians",
        "multiples",
        "of",
        "pi",
    ],
    zip_safe=False,
    package_data={
        "matplot_fmt_pi": [
            "py.typed",
            "ticker.pyi",
            "__init__.pyi"]},
    packages=["matplot_fmt_pi"],
    install_requires=["numpy", "matplotlib"]
)
