---
title: Getting started

tags:
  - information
---

# `ufpy` package

## Introduction

Ufpy (Useful Python) - is a package for simplifying Python programs using many useful features.

Now Ufpy has these features:

- [`UDict`](useful_classes/udict.md "Useful dict.").
- [`UStack`](useful_classes/ustack.md "Useful stack.").
- Generators of classes methods:
    - [`cmp_generator`](generators.md "Compare generator. In latest python version were deleted __cmp__ method. With this generator you can use __cmp__ in your class")
    - [`r_generator`](generators.md "Reverse generator. Generating __r...__ methods for math operations")
    - [`i_generator`](generators.md "I methods generator. Generating __i...__ method for math operations")
- [many protocols for type hinting.](type_checking/protocols.md)
- [many type alias for type hinting.](type_checking/type_alias.md)

## Installing

To install `ufpy`, you need `python 3.12+` and `pip`.
After installing, use this command in your `cmd`/`bash` terminal:

=== "You have one python version"
    ```shell
    pip install ufpy
    # or
    python -m pip install ufpy
    # or
    py -m pip install ufpy
    ```

=== "Several versions"
    ```shell
    python -3.12 -m pip install ufpy
    # or
    py -3.12 -m pip install ufpy
    ```

## Importing and writing some code

After installing, you can use `ufpy` package in all your projects with `3.12+` python version.
Just import `ufpy` or import certain classes, functions and variables.

```python
import ufpy
from ufpy import UDict
```

Enjoy!

## About the site

Site was made using `mkdocs` with `mkdocs material` theme. You can use search: just click `Search`
text input at the top of the page or use the ++s++ or ++f++ hotkeys. You can switch themes using the
button on the left and access the `ufpy` repository using the button on the right.

## Contribute

You can also contribute to `ufpy` package or `ufpy` docs site. Just go to `ufpy` repository using
button in right-top of page. For contributing to site you can use `Edit this page` button
(pencil icon in top of every page).
