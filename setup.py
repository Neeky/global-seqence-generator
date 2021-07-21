import os
import re
from setuptools import setup


setup(name='global-seqence-generator',
      version='0.0.1',
      description='global-seqence-generator',
      author="Neeky",
      author_email="neeky@live.com",
      maintainer='Neeky',
      maintainer_email='neeky@live.com',
      scripts=['bin/global-seqence-client-pb', 'bin/global-seqence-server-pb'],
      packages=['gs','gs/pb'],
      #package_data={'dbma': ['static/cnfs/*', 'static/sql-scripts/*']},
      url='https://github.com/Neeky/global-seqence-generator',
      install_requires=['grpcio>=1.38.1', 'grpcio-tools>=1.38.1'],
      python_requires='>=3.6.*',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8']
      )