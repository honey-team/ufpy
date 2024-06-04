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

When you create new class for library you should add tests. All tests must be Unittests,
be in `tests` directory and contains all public features of class.
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

When you create new class for library you also should add examples. All examples must be
`markdown` files, be in `examples` directory and contains all general public features of class.

Example of example:
```markdown
    # UDict
    
    ## Introduction
    
    UDict is class which is simplifying working with Python dicts.
    It has many methods, properties, magic methods.
    
    Firstly, import `UDict` from `ufpy`
    ```python
    from ufpy import UDict
    ```
    
    ## Create UDict
    
    For creating UDict you should use this code:
    ```python
    d = UDict({'id': 2, 'content': 'hello, world'})
    # for string keys you can use this way:
    d = UDict(id=2, content='hello, world')
    ```
    
    You can also define `default` value for items when you use item's getter:
    ```python
    d = UDict(id=2, content='hello, world', default=0)
    ```
    
    ## Get items
    
    For getting items you should use the way you use in lists and dicts:
    use `UDict[key]` syntax:
    ```python
    d['id'] # 2
    ```
```

### Cautions and notes

Also, you can use cautions and notes in your examples.

#### Caution

Code:
```markdown
> [!CAUTION]
> This is caution!
```

How it's looking:
> [!CAUTION]
> This is caution!

#### Note

Code:
```markdown
> [!NOTE]
> This is caution!
```

How it's looking:
> [!NOTE]
> This is caution!
