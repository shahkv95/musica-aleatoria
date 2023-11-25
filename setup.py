# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='lcg-music-generator',
    version='0.1.0',
    description='Code generates random music using a linear congruential generator (LCG) to select pitches and chords from predefined lists.',
    long_description=readme,
    author='Kush Shah',
    url='https://github.com/shahkv95/lcg-music-gen',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
