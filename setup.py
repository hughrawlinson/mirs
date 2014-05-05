try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A small similarity based lookup system for short, percussive samples',
    'author': 'Hugh Rawlinson',
    'url': 'http://www.github.com/hughrawlinson/mirs',
    'download_url': 'http://www.github.com/hughrawlinson/mirs',
    'author_email': 'hugh@codeoclock.net',
    'version': '0.1',
    'install_requires': ['unittest'],
    'packages': ['mirs'],
    'scripts': [],
    'name': 'MIRS'
}

setup(**config)