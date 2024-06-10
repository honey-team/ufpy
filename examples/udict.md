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
you can get item by its index using `index` kwarg,
and you get item key by its value using `value` kwarg.

Also you can define `default` only for this calling of `get()` using `default` kwarg.

Example:
```python
d = UDict({2: 3, 1: 4}, default=None)
d[2] # 3
d.get(index=2) # 4
d.get(key=1) # also 4
d.get(value=3) # 2

d.get(key=3) # None
d.get(key=3, default='null') # 'null'
```

## Set items

For setting items you should use the way you use in lists and dicts:
use `UDict[key] = value` syntax:
```python
d['id'] = 3
```

Also, you can use indexes and slices when you are setting items:
```python
d[1] = 2
d[2:6:2] = 8
d[:3] = 1, 2, 3
```

## Delete items

For deleting items you should use the way you use in lists and dicts:
use `del UDict[key]` syntax:
```python
del d['id']
```

Also, you can use indexes and slices:
```python
del d[1]
del d[:] # all UDict will become empty
```

## Get length of dict

You can get length of dict using inbuilt `len()` function

```python
d = UDict(hello=1, hi=2)
len(d) # 2
```

## Iterate dict: `keys`, `values`, `items` properties

You can iterate dict using `for key, value in UDict` syntax.

```python
d = UDict(hello=1, hi=2)
for key, value in d:
    print(key, value)
    
# out:
#
# hello 1
# hi 2
```

Also, you can iterate `items` property for this result

```python
for key, value in d.items:
    ...
```

If you want iterate only all keys or values, use `keys` or `values` properties

```python
for key in d.keys:
    ...

for value in d.values:
    ...
```

## Check that dict is empty or not empty

You can use `is_empty()` method to check that UDict is empty:
```python
d = UDict()
print(d.is_empty()) # True

d['hello'] = 'world'
print(d.is_empty()) # False
```

You also can use `if UDict` or `bool(UDict)` syntax:
```python
d = UDict()
print(bool(d)) # False

d['hello'] = 'world'
print(bool(d)) # True

if d:
    print('True!')

# out: True!
```

## Check that key or item in dict

You can check that key in dict:
```python
d = UDict(hi=1, hello=2)

print('hi' in d) # True
print('hii' in d) # False
```

You can also check that item in dict:
```python
d = UDict(hi=1, hello=2)

print(('hi', 1) in d) # True
print(('hi', 11) in d) # False
```

## Using `repr()` and `print()`

`print()` uses `repr()` therefore you can use `UDict`s in `print()`

```python
d = UDict(hi=1, hello=2)
print(d) # u{'hi': 1, 'hello': 2}
print(repr(d)) # u{'hi': 1, 'hello': 2}
```

## Comparing dicts

You can compare `UDict`s using inbuilt compare operators
(`==`, `!=`, `>`, `>=`, `<`, `<=`):

> [!NOTE]
> When you use equal and not equal compare operator, dicts are comparing by its items and length,
> but in other compare operators dicts are comparing only by its length.
> 
> For example, `d > d2 -> len(d) > len(d2)`, etc.

```python
d = UDict(hi=1, hello=2)
d2 = UDict(hi=1, hello=2)
d3 = UDict(hi=1, hello=2, world=3)

print(d == d2) # True
print(d != d2) # False
print(d < d3) # True
print(d <= d3) # True
print(d3 > d) # True
print(d3 >= d) # True
```

## Math operations

You can use inbuilt math operators (`+`, `-`, `*`, `/`, `+=`, `-=`, `*=`, `/=`)
with `UDict`s:

> [!NOTE]
> When you use sum and sub math operators (`+`, `-`) dicts are summing or subtracting, but
> when you use other math operators dict will be multiplying or dividing by integer or dict.
> 
>When dict it works like this:
> 
> d * {'hello': 2, 'hi': 0.5}
> 
> d['hello'] * 2
> 
> d['hi'] * 0.5

```python
d = UDict(hi=1, hello=2)
print(d + {'world': 3}) # u{'hi': 1, 'hello': 2, 'world': 3}
print(d - {'hello': 2}) # u{'hi': 1}

print(d * 2) # u{'hi': 2, 'hello': 4}
print(d * {'hi': 2}) # u{'hi': 2, 'hello': 2}

print(d / 2) # u{'hi': 0.5, 'hello': 1}
print(d / {'hi': 2}) # u{'hi': 0.5, 'hello': 2}
```

## Negative dict

You can use unary minus with dicts:
```python
d = UDict(hi=1, hello=2)
print(-d) # u{'hi': -1, 'hello': -2}
```

## Reverse dict

You can reverse dict using `reverse()` or `reversed()` method.
> [!CAUTION]
> When you use `reverse()`, dict updates in contrast to `reversed()`. Be careful!
> 
> ```python
> # reverse()
> d = UDict(b=1, a=2)
> print(d.reverse()) # u{'a': 2, 'b': 1}
> print(d) # u{'a': 2, 'b': 1}
> 
> # reversed()
> d = UDict(b=1, a=2)
> print(d.reversed()) # u{'a': 2, 'b': 1}
> print(d) # u{'b': 1, 'a': 2}
> ```

```python
d.reverse()
d.reversed()
```

Also, you can use `~` operator and `reversed()` class. They are equivalents of `UDict.reversed()`:
```python
~d
reversed(d)
```

## Sort dict

You can use `sort()` and `sorted()` methods for sorting UDict.
`sort()` is updating dict, `sorted()` - isn't.

```python
# sort()
d = UDict(b=1, a=2)
print(d.sort()) # u{'a': 2, 'b': 1}
print(d) # u{'a': 2, 'b': 1}

# sorted()
d = UDict(b=1, a=2)
print(d.sorted()) # u{'a': 2, 'b': 1}
print(d) # u{'b': 1, 'a': 2}
```
