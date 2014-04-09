"""
azure tools
===

Tools for working with Azure python API
"""
from setuptools import setup, find_packages

setup(
    name='azuretools',
    version='0.1-dev',
    url='http://github.com/bklappauf/azuretools',
    author='Bruce Klappauf',
    author_email='bklappauf@enthought.com',
    description='Tools for working with Azure python API',
    long_description=__doc__,
    platforms='any',
    license='BSD',
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages()
)
