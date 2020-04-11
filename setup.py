import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="matplot-fmt-pi",
    version="1.2.1",
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
    packages=["matplot_fmt_pi"],
    install_requires=["numpy", "matplotlib"]
)
