"""setup.py"""
from setuptools import setup, find_packages
from __init__ import __version__, __author__, __name__, __doc__


setup(author=__author__,
      author_email='wc810267705@163.com',
      maintainer=__author__,
      name=__name__,
      packages=find_packages(exclude=('test', 'test.*')),
      long_description=open('README.md').read(),
      version=__version__,
      keywords='mongodb',
      description=__doc__,
      url="https://github.com/evi0s/pyqudie",
      install_requires=['pymongo'],
      classifiers=[
          'Environment :: Console',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ])