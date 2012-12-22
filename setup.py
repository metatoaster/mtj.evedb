from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='mtj.evedb',
      version=version,
      description="EVE DB access helper",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Tommy Yu',
      author_email='y@metatoaster.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['mtj'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'sqlalchemy',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
