#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

from setuptools import find_packages, setup

setup(
    name="locust-timecsale",
    description="Timescale extension for locust",
    long_description="""https://github.com/shyim/locust-timecsale""",
    classifiers=[
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
    ],
    python_requires=">=3.7, <4",
    keywords="",
    author="Shyim",
    url="https://github.com/shyim/locust-timecsale",
    license="Apache-2.0",
    packages=find_packages(exclude=["examples"]),
    include_package_data=True,
    package_data={"locust_timescale": ["py.typed"]},
    zip_safe=False,
    install_requires=[
        "locust>=2.14.0",
        "psycogreen",
        "psycopg2"
    ],
    use_scm_version={
        "write_to": "locust_timescale/_version.py",
        "local_scheme": "no-local-version",
    }
)
