"""Package configuration"""
from setuptools import find_packages, setup

setup(
    name='djmag_top100_scraper',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'bs4'
    ]
)
