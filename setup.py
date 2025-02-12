from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'deoldify',
    version          = '0.1',
    description      = 'An app to convert old images to color images',
    long_description = readme,
    author           = 'Rigin Oommen',
    author_email     = 'riginoommen@gmail.com',
    url              = 'http://wiki',
    packages         = ['deoldify'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'deoldify = deoldify.__main__:main'
            ]
        }
)
