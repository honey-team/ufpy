---
title: UDict

tags:
  - useful class
---

# `UDict` class

!!! note "UDict as generic"
    You can use `UDict` as `Generic`, because of it, there are 3 `TypeVar`s: KT, VT, CDV.

    KT and VT is key type and value type. In inbuilt `dict` there are KT and VT type vars.
    CDV is class defaul value.

    In this documentation KT, VT and CDV will be using in methods.

## class UDict[KT, VT, CDV]

```python
class UDict(dictionary: AnyDict[KT, VT]) # (1)!
class UDict(dictionary: AnyDict[KT, VT], *, default: CDV)
class UDict(**kwargs: VT)
class UDict(*, default: CDV, **kwargs: VT)
```

1.  `AnyDict[KT, VT] = LikeDict[KT, VT] | dict[KT, VT]`. In UDict 

    !!! note
        `LikeDict[KT, VT]` is type which has `__getitem__`,
        `__setitem__`, `__delitem__` and `get()` methods. `UDict` is `LikeDict`.
    
    Read about [AnyDict](../type_checking/type_alias.md) and [LikeDict](../type_checking/protocols.md)

---

Create UDict object. If `default`, when not existent keys is given in
getting item, method will return `default`.

!!! example
    ```py
    d = UDict(hello=world, hi=python, default=10)
    ```

## (property, settable) dictionary: dict[KT, VT]

UDict's dictionary.

!!! example
    ```py
    print(d.dictionary)
    d.dictionary = {4: 'world'}
    ```

!!! tip
    You can use UDict to set dictionary

    !!! example
        ```python
        d.dictionary = UDict({1: 7})
        ```

## (property, settable) keys: list[KT]

UDict's keys

!!! example
    ```python
    print(d.keys)
    d.keys = [1, 2]
    ```

!!! tip
    You can use tuples to set keys
    
    !!! example
        ```python
        d.keys = 1, 2
        ```

## (property, settable) values: list[VT]

UDict's values

!!! example
    ```python
    print(d.values)
    d.values = [7, 2]
    ```

!!! tip
    You can use tuples to set values
    
    !!! example
        ```python
        d.values = 7, 2
        ```

## (property, settable) items: list[tuple[KT, VT]]

UDict's items.

!!! example
    ```python
    print(d.items)
    d.items = [(1, 7), (2, 2)]
    ```

!!! tip
    You can use tuples to set items or you can use tuples or lists with lists
    
    !!! example
        ```python
        d.items = (1, 7), (2, 2)
        d.items = [1, 7], [2, 2]
        ```

## (property, settable) default: CDV

UDict's default value

!!! example
    ```python
    print(d.default)
    d.default = 'null'
    ```

## reverse() -> UDict[KT, VT, CDV]

Reverses UDict and returns it. (1)
{ .annotate }

1.  !!! question "How UDict is being reversing?"

        Just is being reversing items  
        `#!python u{'hello': 1, 'hi': 2}` -> `#!python u{'hi': 2, 'hello': 1}` (reversed)

!!! warning
    `#!python reverse()` edits UDict. If you don't want to reverse UDict use [`#!python reversed()`](#reversed-udictkt-vt-cdv) method instead.

!!! example
    ```python
    d.reverse()
    print(d) # prints reversed UDict
    ```

## reversed() -> UDict[KT, VT, CDV]

Returns reversed UDict

!!! example
    ```python
    print(d.reversed())
    ```

!!! tip "Get reversed UDict with inbuilt `#!python reversed()` and `#!python ~` operator"
    You can get reversed UDict with inbuilt `#!python reversed()` and with invert operator (`~`).
    !!! example
        ```
        print(~d)
        print(reversed(d))
        print(d.reversed() == reversed(d)) # True
        ```
    [Read more about `#!python reversed()` and `#!python ~` support in UDict](#magic-methods)

## sort() -> UDict[KT, VT, CDV]

Sorts UDict and returns it. (1)
{ .annotate }

1.  !!! question "How UDict is being sorting?"

        Just are being sorting items by keys.  
        `#!python u{'b': 1, 'a': 2}` -> `#!python u{'a': 2, 'b': 1}` (sorted)

!!! warning
    `#!python sort()` edits UDict. If you don't want to sort UDict use [`#!python sorted()`](#sorted-udictkt-vt-cdv) method instead.

!!! example
    ```python
    print(d.sort())
    ```

## sorted() -> UDict[KT, VT, CDV]

Returns sorted UDict

!!! example
    ```python
    print(d.sorted())
    ```

##  get()

```python
def get(*, key: KT) -> VT | CDV
def get(*, key: KT, default: DV) -> VT | DV
def get(*, index: int) -> VT | CDV
def get(*, index: int, default: DV) -> VT | DV
def get(*, value: VT) -> KT | CDV
def get(*, value: VT, default: DV) -> KT | DV
```

!!! failure "Using more than 1 argument"
    If you use 0 or 2 or 3 of this arguments (`key`, `index`, `value`), method will raise `ValueError`

Arguments:
#### `key: KT`

UDict value's key to find.

!!! example
    ```python
    print(d.get(key='key')) # same that d['key']
    ```

#### `index: int`

UDict value's index to find

!!! warning
    Indexes are starting from 1. Index of first element of UDict is 1.

!!! failure "`index` argument more than UDict length"
    If you use `index` argument make sure that `index` are less than UDict length. Otherwise `#!python get()`
    will raise `IndexError`

!!! example
    ```python
    print(d.get(index=2)) # second value of UDict
    ```

#### `value: VT`

UDict key's value to find

!!! example
    ```python
    print(d.get(value=1)) # if d = UDict{'hello': 1}, this will be 'hello'
    ```

## Magic methods

Currently, UDict supports all these magic methods:

### _\_call__(func: Callable[[KT, VT], VT]) -> UDict[KT, VT, CDV]

Returns new UDict, but all values generated with `func` function. First argument: key, second: value.

Arguments:
#### `func: (KT, VT) -> VT`

First argument of function is key, second is value. Returns new value
    

!!! example
    ```python
    def f(k, v):
        return v * 2
    d = d(f) # multiply all values by 2
    ```

*[KT]: Key type
*[VT]: Value type
*[CDV]: Class default value
