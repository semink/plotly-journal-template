from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='plotly_journal',
    version='0.0.1',
    description='plotly themes for journals',
    author='Semin Kwak',
    author_email='semin.kwak@gmail.com',
    packages=['plotly_journal'],
    install_requires=['plotly'],
    long_description=read('README.md')
)
