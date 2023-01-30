from os.path import exists
from distutils.core import setup
import timewatch

setup(
  name = 'timewatch',
  packages = ['timewatch'],
  version = timewatch.__version__,
  description = 'A library automating worktime reports for timewatch.co.il',
  long_description=(open('README.md').read() if exists('README.md') else ''),
  author = 'Maor Kima',
  author_email = 'maorkima@gmail.com',
  download_url = 'https://github.com/nirizr/timewatch/tarball/{}'.format(timewatch.__version__),
  keywords = ['timewatch', 'timewatch.co.il'], # arbitrary keywords
  classifiers = [],
)
