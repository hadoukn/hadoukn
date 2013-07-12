# hadoukn/setup.py
import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    'colander',
    'pyramid',
    'pyramid_tm',
    'sqlalchemy',
    'transaction',
    'waitress',
    'zope.sqlalchemy',
]

entry_points = """
    [paste.app_factory]
    main = hadoukn:main
"""

setup(name='hadoukn',
      version='0.1',
      description='hadoukn',
      long_description=README,
      packages=find_packages(),
      test_suite='hadoukn.tests',
      entry_points=entry_points)
