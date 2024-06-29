---
title: UDict

tags:
  - useful class
---

# `UDict` class

!!! note
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

## Magic methods

Currently, UDict supports all these magic methods:

### magic   _\_call__(func: Callable[[KT, VT], VT]) -> UDict[KT, VT, CDV]

Returns new UDict, but all values generated with `func` function. First argument: key, second: value.

!!! example
    ```python
    def f(k, v):
        return v * 2
    d = d(f) # multiply all values by 2
    ```

*[KT]: Key type
*[VT]: Value type
*[CDV]: Class default value
