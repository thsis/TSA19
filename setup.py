"""
Setup for package
"""

import os
from setuptools import setup, find_packages


def read(fname):
    """Return contents of a file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name="TSA19",
      author="Christian Gary Mena Lecona, Thomas Siskos",
      author_email="gary.mena@bdpems.de, thomas.siskos91@gmail.com",
      description="Models and algorithms for the course Time Series Analysis",
      license="MIT",
      keywords="Python time-series-analysis",
      url="https://github.com/thsis/TSA19",
      packages=find_packages(),
      long_description=read("README.md"))
