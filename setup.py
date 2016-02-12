"""
    WrenchSQL Query Window Component
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
from pip.req import parse_requirements

GIT_ROOT = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(GIT_ROOT, 'README.rst'), encoding='utf-8') as file_handle:
    LONG_DESCRIPTION = file_handle.read()

INSTALL_REQUIRES = [
    str(requirement.req) for requirement
    in parse_requirements(path.join(GIT_ROOT, 'requirements.txt'))
]

setup(
    name='WrenchSQL',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.0a1',

    description='Python and GTK based SQL browser.',
    long_description=LONG_DESCRIPTION,

    # The project's main homepage.
    url='https://github.com/WrenchSQL/WrenchSQL',

    # Author details
    author='Dylan Grafmyre',
    author_email='thorsummoner@live.com',

    # Choose your license
    license='GPL V3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Code Generators',

        'Environment :: X11 Applications :: GTK',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='sql mysql browser',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=INSTALL_REQUIRES,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'nose'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'sample': ['package_data.dat'],
    },

    entry_points={
        'gui_scripts': [
            'wrenchsql-demo-querywindow = wrenchsql.querywindow:demo',
        ],
    },
)
