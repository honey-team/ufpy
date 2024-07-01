@echo off
py -3.12 -m pip install --upgrade pip
py -3.12 -m pip install setuptools twine
py -3.12 setup.py sdist

py -3.12 -m twine upload dist\*

rd /s /q ufpy.egg-info
rd /s /q dist
rd /s /q build
