from setuptools import setup, find_packages

setup(name='coin_change',
      version='0.0.1',
      description='Coin change implementation with support for multiple currencies',
      url='http://github.com/soumyadsanyal/change',
      author='Soumya D. Sanyal',
      author_email='soumya@soumyadsanyal.com',
      license='MIT',
      install_requires=['pytest'],
      packages=find_packages(),
      zip_safe=False)
