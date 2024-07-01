# UPair

## Introduction

UDeque is class which is simplifying working with deque.
It has many methods, properties, magic methods.

Firstly, import `UPair` from `ufpy`
```python
from ufpy import UPair
```

## Create UPair

For creating UPair you should use this code:
```python
p = UPair(first="first", second="second")
```

## Get first/second

To get the first value you can use:
```python
p[0] # first
p.first # first
```

To get the second value you can use:
```python
p[1] # second
p.second # second
```

> [!NOTE]
> 0 - the first value
> 1 - the second value

## Set first/second

To set the first value you can use
```python
p.first = "FIRST" # FIRST
```

Use the same way to set the second value

> [!NOTE]
> Also you can use indexes:
> ```python
> p[0] = "FIRST"
> p[1] = "SECOND"
> ```
> But it is undesirable to use

## Get length of pair

You can get the length of the pair using the built-in len() function.

```python
p2 = UPair(1, 2)
len(p2) # 2
```

> [!NOTE]
> If `first == None` and `second == "second"` `len()` returns 1
> If `first == None` and `second == None` `len()` returns 0

## Reserve
To reserve the pair's the first and the second value, use the built-in `reserved()` function
```python
reserved(p2) # ["second", "first"]
```