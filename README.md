<p align=center>
    <picture>
        <source
            srcset="/readme_assets/logo_d.svg"
            media="(prefers-color-scheme: dark), (min-width: 200px)"
        />
        <source
            srcset="/readme_assets/logo_l.svg"
            media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference), (min-width: 200px)"
        />
        <img src="readme_assets/logo.svg" width="200" alt="Logo" style="text-align: center" />
    </picture>
</p>

<p align=center>
    <a href="https://pypi.org/project/ufpy">
        <img src="https://img.shields.io/pypi/v/ufpy?style=flat&amp;logo=pypi&amp;logoColor=white&amp;label&amp;color=blue" alt="Pypi">
    </a>
    <a href="https://python.org">
        <img src="https://img.shields.io/badge/3.12%2B-blue?logo=python&amp;logoColor=white" alt="Python version">
    </a>
    <a href="https://honey-team.ru/ufpy-website">
        <img src="https://img.shields.io/badge/docs-blue?logo=material%20for%20mkdocs&amp;logoColor=white" alt="Docs">
    </a>
    <a href="https://pypi.org/project/pylint">
        <img src="https://img.shields.io/badge/pylint-blue" alt="Pylint">
    </a>
    <a href="https://pypi.org/project/black">
        <img src="https://img.shields.io/badge/black-blue" alt="Black">
    </a>
</p>

Ufpy (Useful Python) - package for Python with some useful features

# Key features

- Useful dict (UDict) for simplification working with dictionaries. [See more...](examples/udict.md)
- Download GitHub's public repositories, its folders and files. [See more...](examples/github/download.md)
- Some type alias and protocols
- And more!

# Installation

## Install latest version

To install `ufpy` with `pip` use this command in your shell
```sh
pip install ufpy
```

## Install specific version

To install specific version of `ufpy` with `pip` use this command in your shell
```sh
# Replace version with your specific version
pip install ufpy==version
```

## Install dev version

To install dev version with `pip`:

1. Clone this repository (you need to have installed `git`)
2. Install library as cloned code

```sh
git clone https://github.com/honey-team/ufpy
cd ufpy
pip install .
```

After this you can remove `ufpy` directory

