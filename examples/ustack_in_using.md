# Getting started
To start, install ufpy lib by command
### Windows
pip install ufpy
### Linux


## Examples
To create stack, use UStack class.
```python
stack = UStack()
```
To add an element to the stack, use UStack.append([<element1>, <elementN, ...])
```python
stack.append(1, 2, 3, 4, 5)
```
To get the top element, use UStack.top()
```python
print(stack.top())
# 5
```
To get and remove the top element of the stack, use UStack.pop()
```python
print(stack.pop())
# 5
print(stack.top())
# 4
```
## All methods
| Name    | Args    |
| ------- | ------- |
| top     | null    |
| append  | **items |
| pop     | null    |