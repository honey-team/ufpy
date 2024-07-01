# Stack

## Introduction

A Stack is a list that allows access only to the top element and includes several useful features. [Wiki](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))

Firstly, import `Stack` from `ufpy`

```python
from ufpy import Stack
```

## Create Stack

To create a Stack, use the following code:
```python
s = Stack() # blank stack
s = Stack(1, 9, 2) # You can also provide elements as arguments
s = Stack(iterable=[9, 2, 8]) # Or with `iterable` kwarg
```

## Get / edit / delete top element

For getting top element you can use `top` property:
```python
s.top
```

For editing, you can just set value to this property:
```python
s.top = 2
```

For deleting:
```python
del s.top
```

Also, you can use `pop()` method for deleting. On this way you also will get top element
after its deleting. It's working how `list.pop()`:
```python
popped_element = s.pop()
```

If you want to delete several elements, use `remove()` method:
```python
s.remove(2, 9, 1) # delete first elements with values 2 or 9 or 1
# (how list.remove(), but with several elements)
```

## Get / set / delete all elements

You can get all elements with `elements` property:
```python
s.elements
```

Also with property you can edit elements:
```python
s.elements = [1, 2, 3]
```

And delete them:
```python
del s.elements
```

## Push elements

To add elements to the stack, use `push()` method

```python
s.push(1, 2, 3, 4, 5)
```

## Math operations

You can use 4 math operations with stacks: `+`, `-`, `*`, `/`. `+`, `-` append or
remove items to stack. `*`, `/` multiply or divide these items. [See UDict example for
more information.](udict.md#math-operations)

```python
s = s + [1, 2]
# or
s += 1, 2

s = s - 1
# or
s -= 1

s *= 2 # multiply by 2
s /= 2 # divide by 2
```

## Get length of stack

You can get length of stack using `len()` function:
```python
len(s)
```

## Check that stack is empty or not empty

You can check that stack is empty using `is_empty()` method:
```python
s = Stack()
s.is_empty() # True
```

You can also use the `if Stack` syntax to check whether the stack is not empty
```python
s = Stack()
if s:
    print("Stack isn't empty!")
else:
    print("Stack is empty!")
# out: Stack is empty!
```

## Use `repr()` function with stack

You can use `repr()` with stacks. Because of it, you can print stacks:
```python
s = Stack(1, 9, 2)
print(s) # s[1, 9, 2]
```

## Copying of Stack

You can use `copy()` method for copying `Stack`s:
```python
s.copy()
```

You can use the `copy.copy()` function to copy `Stack`s:
```python
from copy import copy

copy(s)
```
