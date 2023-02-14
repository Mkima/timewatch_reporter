from os.path import exists
from distutils.core import setup
import timewatch

setup(
  name = 'timewatch',
  packages = ['timewatch'],
  version = timewatch.__version__,
  description = 'A library that automates worktime task reports for timewatch.co.il',
  long_description=(open('README.md').read() if exists('README.md') else ''),
  author = 'Maor Kima',
  author_email = 'maorkima@gmail.com',
install_requires=[
            'tqdm',
    'BeautifulSoup4',
    'requests',
    'pandas',
    'lxml',
    'tabulate',
        ],

  keywords = ['timewatch', 'timewatch.co.il'], # arbitrary keywords
  classifiers = [],
)
