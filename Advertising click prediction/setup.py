from setuptools import find_packages,setup
from pathlib import Path


# package metadata
NAME = 'advertising_ml_project'
DESCRIPTION = 'Ml project to predict advertisement clicks'
URL = 'https://github.com/hansel-dias/Advertising-click-prediction'
AUTHOR = 'Hansel Gavin Dias'
EMAIL = 'hanseldias919@gmail.com'

long_description = DESCRIPTION
HYPHEN_E ="-e ."

# directories
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR


# Obtain List of all packages from requiremnts
def list_reqs():
    with open(REQUIREMENTS_DIR/'requirements.txt') as fd:
        requirements = fd.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)

    return requirements



# Where the magic happens:
setup(
    name=NAME,
    version= '0.0.1',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license="BSD-3",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)