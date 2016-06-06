import versioneer
from setuptools import setup


setup(name='synthetic_data',
      packages=['synthetic_data'],
      author='Brookhaven National Laboratory',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass())
