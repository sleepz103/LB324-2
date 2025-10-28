from setuptools import setup, find_packages

setup(
    name="arithmetic",
    version="0.1",
    packages=find_packages(where="."),
    package_dir={"": "."},
)
