#!/usr/bin/python3
# vim: fileencoding=utf-8

import os
import pathlib
import setuptools

from qubesmirror import __version__
assert __version__ == pathlib.Path('version').read_text().strip()

if __name__ == '__main__':
    setuptools.setup(
        name='qubesmirror',
        version=__version__,
        author='Wojtek Porczyk',
        author_email='woju@invisiblethingslab.com',
        maintainer='Invisible Things Lab',
        description='Simple mirror manager for yum repos, as used in Qubes OS infra.',
        license='GPL2+',
        url='https://github.com/QubesOS/qubes-infrastructure-mirrors',
        packages=setuptools.find_packages(),
        requires=['aiohttp'],
        entry_points={
            'console_scripts': [
                'mkmetalink = qubesmirror.metalink:main'
            ],
        },
    )
