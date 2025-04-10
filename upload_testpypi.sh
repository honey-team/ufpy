#!/usr/bin/zsh

# Create venv
python3.12 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install setuptools wheel twine
python setup.py sdist

twine upload --repository testpypi dist/*

rm -r ufpy.egg-info
rm -r dist