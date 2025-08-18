"""
Setup script for MorphScore package.
"""

from setuptools import setup

setup(
    name="morphscore",
    version="0.1.0",
    py_modules=["morphscore"],
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.20.0",
    ],
)