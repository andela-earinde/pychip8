# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


setup(
    name='pychip8',
    version='0.0.1',
    description='Implementing the chip8 interpreter in python',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    long_description=readme,
    author='Arinde Eniola',
    author_email='eniola.arinde@andela.com',
    url='https://github.com/andela-earinde/pychip8',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'pyglet',
    ],
)
