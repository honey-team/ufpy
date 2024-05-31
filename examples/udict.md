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

You can also use index of key or slice of indexes of keys:

> [!CAUTION]
> In this class first index is 1

```python
d[1] # 2
d[:] # u{'id': 2, 'content': 'hello, world'} (UDict object)
```

You can also use `get()` method.
You can get item by its key using `key` kwarg,
and you can get item by its index using `index` kwarg.
Example:
```python
d = UDict({2: 3, 1: 4})
d[2] # 3
d.get(index=2) # 4
d.get(key=1) # also 4
```

## Set items

For setting items you should use the way you use in lists and dicts:
use `UDict[key] = value` syntax:
```python
d['id'] = 3
```

Also you can use indexes and slices when you are setting items:
```python
d[1] = 2
d[2:6:2] = 8
d[:3] = 1, 2, 3
```
