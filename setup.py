import io 
import os
from pathlib import Path
from setuptools import setup,find_packages

# Medata of package
NAME = 'prediction_model'
DESCRIPTION = 'Loan Prediction Model'
URL = 'nan'
EMAIL = 'devsiddharthsingh5010@gmail.com'
AUTHOR = 'Siddharth Singh'
REQUIRES_PYTHON = '>=3.7.0'

pwd = os.path.abspath(os.path.dirname(__file__))

# Get the lisf of packages to be installed
def list_reqs(fname='requirements.txt'):
    with open(os.path.join(pwd,fname),encoding='utf-8') as fd:
        return fd.read().splitlines()


try:
    with io.open(os.path.join(pwd, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
print(PACKAGE_DIR)
about = {}
with open(PACKAGE_DIR/'VERSION') as f:
    _version = f.read().strip()
    about['__version__']=_version

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author = AUTHOR,
    author_email=EMAIL,
    python_requires= REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude='tests'),
    package_data={'prediction_model':['VERSION','datasets/train.csv','datasets/test.csv']},
    install_requires=list_reqs(),
    extra_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
