# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='humiocore',
    version='0.1.9',
    description='A python library for for interacting with the Humio API',
    python_requires='==3.*,>=3.6.0',
    project_urls={'repository': 'https://github.com/gwtwod/py3humiocore'},
    author='Jostein Haukeli',
    packages=['humiocore'],
    package_data={},
    install_requires=[
        'aiohttp==3.*,>=3.5.0', 'chardet==3.*,>=3.0.0', 'colorama==0.*,>=0.4.1',
        'pandas==0.*,>=0.24.1', 'python-dotenv==0.*,>=0.10.2',
        'pytz==2018.*,>=2018.9.0', 'requests==2.*,>=2.21.0',
        'snaptime==0.*,>=0.2.4', 'structlog==19.*,>=19.1.0',
        'structlog-pretty==0.*,>=0.1.1', 'tzlocal==1.*,>=1.5.0'
    ],
    extras_require={'dev': ['black', 'pylint==2.*,>=2.3.0']},
)
