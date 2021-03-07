"""Package configuration"""
from setuptools import find_packages, setup

setup(
    name='djmag_top100_scraper',
    packages=find_packages(),
    package_dir={'': 'src'},
    install_requires=[
        'requests==2.5.1',
        'beautifulsoup4==4.9.3',
        'coverage==5.5',
        'pytest==6.2.2'
    ]
)
