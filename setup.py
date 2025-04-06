from setuptools import find_packages, setup

setup(
    name="gioco",
    packages=find_packages(include=["gioco"]),
    version="0.0.0",
    description="Python math functions for testing",
    author="Justin Erlick",
    license="MIT",
    install_requires=[],
    test_suite="tests",
)