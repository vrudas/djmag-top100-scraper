"""Package configuration"""
from setuptools import find_packages, setup

setup(
    name='djmag_top100_scraper',
    packages=find_packages(),
    install_requires=[
        'requests',
        'bs4',
        'coverage',
        'pytest'
    ]
)
