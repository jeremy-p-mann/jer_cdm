from setuptools import find_packages, setup

setup(
    name='jer_cdm',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['pandas', 'pandera', 'typer']
)
