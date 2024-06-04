# 📖 Contributing rules in `ufpy` repository

If you want to contribute the project, you must read this rules and follow they.

## 💻 Code style

- Formatter: `black`
- Optimizer of imports: `isort`
- Linter: `Pylint`
- `Generic`

Use `typing.Generic`s in your useful classes.

For example,
```python
from typing import Generic, TypeVar

T = TypeVar('T')

class A(Generic[T]): 
    def __init__(self, a: T): ...
```

- `@overload`s

Use decorator `@typing.overload` in public methods if your method
has two and more variants to define arguments
For example,
```python
@overload
def a(x: int): ...
@overload
def a(x: list): ...
@overload
def a(x: dict): ...
def a(x: int | list | dict): ...
```

- `__all__`

`__all__` variable is variable with names of every class,
function and variable in module which needs to import.
When you use `from x import *` syntax, you import all names from `x.__all__` variable.
Example:
```python
__all__ = (
    'abc',
    'Abc',
)

def abc(): ...
class Abc: ...
```

- `__future__.annotations`

If you use your class in annotations in method's signatures of this, you should import
`__future__.annotations`. Don't use string annotations!

```python
# don't this
class A:
    def a(self, b: 'A') -> 'A': ...

# do this
from __future__ import annotations

class A:
    def a(self, b: A) -> A: ...
```

## ✅ Tests rules

When you create new class for library you should add tests. All tests must be Unittests and
contains all public features of class.
[How to write unittest?](https://realpython.com/python-testing/#how-to-structure-a-simple-test)

Example of test for UDict class:
```python
import unittest

from ufpy import UDict


class UDictTestCase(unittest.TestCase):
    def test_init(self):
        d = UDict(hello=1, hi=2, default=10)
        d2 = UDict({'hello': 1, 'hi': 2})
        self.assertEqual(d.default, 10)
        self.assertDictEqual(d.dictionary, d2.dictionary)
        self.assertEqual(d, d2)
```

## 📺 Examples rules

...
