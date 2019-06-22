# -*- coding: utf-8 -*-

import re
from setuptools import setup


VERSION = re.search(
    '^__version__\s*=\s*"(.*)"', open("mdtable/mdtable.py").read(), re.M
).group(1)


with open("README.md", "rb") as f:
    LONG_DESCR = f.read().decode("utf-8")


setup(
    name="mdtable",
    packages=["mdtable"],
    entry_points={"console_scripts": ["mdtable = mdtable.cli:main"]},
    version=VERSION,
    description="mdtable converts csv files to markdown formatted tables",
    long_description=LONG_DESCR,
    long_description_content_type="text/markdown",
    author="Zain Patel",
    author_email="zain.patel06@gmail.com",
    url="https://github.com/mzjp2/mdtable",
    classifiers=[
        # Pick your license as you wish
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="markdown cli convert",
    python_requires=">=3.5",
    install_requires=["click"],
)
