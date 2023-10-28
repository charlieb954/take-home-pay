#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

test_requirements = [
    "pytest>=3",
]

setup(
    author="Charlie B",
    author_email="",
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9",
    ],
    description="A Python package to work out tax, pension and national insurance contributions in the UK by year.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="takehomepay",
    name="takehomepay",
    packages=find_packages(include=["takehomepay", "takehomepay.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/charlieb954/takehomepay",
    version="0.1.0",
    zip_safe=False,
)
