"""Package configuration"""
from setuptools import find_packages, setup

setup(
    packages=['src', 'tests'],
    install_requires=[
        'requests',
        'bs4',
        'coverage',
        'pytest'
    ]
)
