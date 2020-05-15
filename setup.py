from distutils.core import setup
from setuptools import setup, find_packages

with open('README.md') as file:
    readme = file.read()

with open('requirements.txt') as file:
    install_requires = file.readlines()

setup(
    name='datalib',
    version='0.2',
    packages=find_packages(),
    install_requires=install_requires,
    url='',
    license='LICENSE.txt',
    description='',
    long_description=readme,
    author='Perry',
    author_email='perryism@gmail.com'
)
