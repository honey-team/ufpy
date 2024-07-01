from setuptools import setup, find_packages

from ufpy import __version__

with open('README.md', 'r', encoding='utf-8') as mdf:
    long_description = mdf.read()

install_requires = [
    'requests>=2.31.0',
]

author = 'bleudev'
author_email = 'aitiiigg1@gmail.com'
organization_name = 'honey-team'
project_name = 'ufpy'
github_url = f'https://github.com/{organization_name}/{project_name}'


setup(
    name=project_name,
    version=__version__,
    author=author,
    author_email=author_email,
    description='Ufpy (Useful Python) - package for Python with some useful features.',
    download_url=f'{github_url}/releases/tag/{__version__}',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=github_url,
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
    ],
    zip_safe=False,
    python_requires=">=3.12",
    install_requires=install_requires
)
