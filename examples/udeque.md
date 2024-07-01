# UDeque
## Introduction

UDeque is class which is simplifying working with deque.
It has many methods, properties, magic methods.

Firstly, import `UDeque` from `ufpy`
```python
from ufpy import UDeque
```

## Create UDeque

For creating UDeque you should use this code:
```python
d = UDeque(1, 2, 3, 4, 5)
```

## Get end/begin

To get end you can use:
```python
d[0] # 1
d.end() # 1
```

To get begin you can use:
```python
d[1] # 5
d.begin() # 5
```

> [!NOTE]
> 0 - first element
> 1 - last element

## Add end/begin

To add end you can use
```python
d.addend(6) # [1, 2, 3, 4, 5, 6]
```

To add begin you can use
```python
d.addbegin(0) # [0, 1, 2, 3, 4, 5, 6]
```

## Set end/begin

To set end you can use
```python
d.setend(7) # [0, 1, 2, 3, 4, 5, 7]
```

To set begin you can use
```python
d.setbegin(7) # [7, 1, 2, 3, 4, 5, 7]
```
> [!NOTE]
> Also you can use indexes:
> ```python
> d[0] = 1 # [1, 1, 2, 3, 4, 5, 7]
> d[1] = 1 # [1, 1, 2, 3, 4, 5, 1]
> ```
> But it is undesirable to use

## Delete end/begin

For deleting end use
```python
d.popend() # [7, 1, 2, 3, 4, 5]
```

For deleting begin use
```python
d.popbegin(7) # [1, 2, 3, 4, 5]
```

> [!NOTE]
> To delete end or begin you also can use `del`:
> ```python
> del d[0] # [2, 3, 4, 5]
> del d[1] # [2, 3, 4]
> ```
> But it is undesirable to use

## Get length of deque

You can get the length of the deque using the built-in len() function.

```python
d2 = UDeque(1, 2, 3, 4, 5)
len(d2) # 5
```

## Reserve
To reserve the deque's end and beginning, use the built-in `reserved()` function
```python
reserved(d2) # [5, 1]
```

> [!NOTE]
> `reserved()` returns `[end, begin]`
