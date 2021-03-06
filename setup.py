"""Package configuration"""
from setuptools import find_packages, setup

setup(
    packages=find_packages(),
    install_requires=[
        'requests',
        'bs4',
        'coverage',
        'pytest'
    ]
)
