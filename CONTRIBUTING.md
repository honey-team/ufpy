# 📖 Contributing rules in `ufpy` repository

If you want to contribute, you have to read this rules and follow they.

## 💻 Code style

- Formatter: `black`
- Optimizer of imports: `isort`
- Linter: `Pylint`
- Generic style: `True`

Generic style is style where are using `typing.Generic` class in all `useful classes`

For example,
```python
from typing import Generic, TypeVar

T = TypeVar('T')

class A(Generic[T]): 
    def __init__(self, a: T): ...
```

- `@overload`s: `True`

You must define `@typing.overload`s in public methods when your method has two and more ways to define arguments
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

- `__all__` variable: `True`

`__all__` variable is variable with names of every class,
function and variable in module which needs to import.
When you use `from x import *` syntax, you import all names from `x.__all__` variable.
