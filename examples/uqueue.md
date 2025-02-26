# UQueue
## Introduction

UQueue is class which is simplifying working with queue.
It has many methods, properties, magic methods.

Firstly, import `UQueue` from `ufpy`
```python
from ufpy import UQueue
```

## Create UQueue

For creating UQueue you should use this code:
```python
q = UQueue(1, 2, 3, 4, 5)
```

## Get head

To get head of the queue use:
```python
q.head # 5
```

## Add value

To add value you can use
```python
q.push(6) # [1, 2, 3, 4, 5, 6]
```

## Set head

To set end you can use
```python
q.set_head(7) # [1, 2, 3, 4, 5, 7]
```

## Delete value

For deleting the first element use
```python
q.pop() # [2, 3, 4, 5, 7]
```

> [!NOTE]
> To delete end or begin you also can use `del <UQueue>[-1]`:
> ```python
> del q[-1] # [2, 3, 4, 5]
> ```
> But it is undesirable to use

## Get length of queue

You can get the length of the queue using the built-in len() function.

```python
q2 = UQueue(1, 2, 3, 4, 5)
len(q2) # 5
```

## Reserve
To reserve the queue's end and beginning, use the built-in `reserved()` function
```python
reserved(q2) # [5, 4, 3, 2, 1]
```

## Iteration
`UQueue()` suppots iteration:
```python
for var in q2:
    print(var)
# 1
# 2
# 3
# 4
# 5
```

> [!WARNING]
> After using `for` your queue will be empty:
> ```python
> print(q2) # []
> ```