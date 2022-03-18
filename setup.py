#!/usr/bin/env python3
# coding: utf-8

from setuptools import setup

setup(
    name="workshop",
    version="0.1",
    license="Infor",
    python_requires="==3.7.5",
    zip_safe=False,
    include_package_data=True,
    packages=["staging", "features_processing"],
    package_dir={
        "staging": "./src/staging",
        "features_processing": "./src/features_processing",
    }
)
