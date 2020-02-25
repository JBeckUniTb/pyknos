# coding: utf-8

from setuptools import find_packages, setup

exec(open("pyknos/version.py").read())

setup(
    name="pyknos",
    version=__version__,
    description="don't regress",
    url="https://github.com/mackelab/pyknos",
    author="Álvaro Tejero Cantero",
    packages=find_packages(exclude=["tests"]),
    license="GPLv3",
    install_requires=[
        "matplotlib",
        "nflows@git+https://github.com/mackelab/nflows.git",
        "numpy",
        "tensorboard",
        "torch",
        "tqdm",
    ],
    extras_requires={
        "dev": [
            "autoflake",
            "black",
            "flake8",
            "isort",
            "pytest",
            "pyyaml",
            "torchtestcase",
        ],
    },
    dependency_links=[],
)
