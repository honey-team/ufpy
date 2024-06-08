---
title: UDict

tags:
  - useful class
---

# `UDict` class

!!! note
    You can use `UDict` as `Generic`, because of it, there are 3 `TypeVar`s: KT, VT, CDV.

    KT and VT is key type and value type. In inbuilt `dict` there are KT and VT type vars.
    CDV is class defaul value. See `__init__` for more information.

    In this documentation KT, VT and CDV will be using in methods.

## class UDict(dictionary=None, *, default=None, **kwargs)[KT, VT, CDV]

```python
class UDict(dictionary: AnyDict[KT, VT]) # (1)
class UDict(dictionary: AnyDict[KT, VT], *, default: CDV)
class UDict(**kwargs: VT)
class UDict(*, default: CDV, **kwargs: VT)
```

1.  `AnyDict[KT, VT] = LikeDict[KT, VT] | dict[KT, VT]`. In UDict 

    !!! note
        `LikeDict[KT, VT]` is type which has `__getitem__`,
        `__setitem__`, `__delitem__` and `get()` methods. `UDict` is `LikeDict`.

---

Create UDict object. If `default`, when not existent keys is given in
getting item, method will return `default`.

!!! example
    ```py
    d = UDict(hello=world, hi=python, default=10)
    ```

## (property, settable) dictionary: dict[KT, VT]

UDict's dictionary.

!!! tip
    You can use UDict to set dictionary

    !!! example
        ```python
        d.dictionary = UDict({1: 7})
        ```

!!! example
    ```py
    print(d.dictionary)
    d.dictionary = {4: 'world'}
    ```

## (property, settable) keys: list[KT]

UDict's keys

!!! tip
    You can use tuples to set keys
    
    !!! example
        ```python
        d.keys = 1, 9
        ```

!!! example
    ```python
    d.keys = [1, 2]
    ```

*[KT]: Key type
*[VT]: Value type
*[CDV]: Class default value
