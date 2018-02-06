from setuptools import setup

setup(name='linkedin',
      version='0.1.0',
      description='Download user data from LinkedIn',
      url='https://github.com/mfrodl/linkedin-scraper',
      author='Martin Frodl',
      author_email='maarilainen@gmail.com',
      license='GPLv2',
      packages=['linkedin'],
      install_requires=[
          'scrapy',
          'six',
          'unicodecsv',
      ],
      entry_points={
          'console_scripts': [
              'linkedin-scraper = linkedin.__main__:main',
          ],
      },
  )
