try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config ={
    'description': 'WorkTRacker',
    'author': 'Yojimbo',
    'url' : 'WorkTracker',
    'download_url' : 'WorkTracker',
    'author_email' : 'johnson.david3411@yahoo.com',
    'version' : '0.1',
    'install_requiers' : ['nose', 'PyQt4', 'sip', 'datetime', 'sys'],
    'packages' : ['WorkTracker'],
    'scripts' : [],
    'name' : 'WorkTracker'
}

setup(**config)
