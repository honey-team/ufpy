# -*- encodibg: utf-8 -*-
from __future__ import annotations
from typing import Any

class UStackElement():
    def __init__(self, value: Any) -> UStackElement:
        """
        UStackElement is using like an element in UStack.
        """
        self.__value: Any = value
        
    def __len__(self):
        return len(self.__value)
        
    def __str__(self):
        return str(self.__value)
        
    def __int__(self):
        return int(self.__value)
        
    def __bool__(self):
        return bool(self.__value)

    def __dict__(self):
        return dict(self.__value)
        
    def __bytes__(self, encoding: str = 'utf-8'):
        return bytes(self.__value, encoding)

class UStack():
    def __init__(self, _list: list | tuple = list()) -> UStack:
        """
        UStack's methods:
            append(**items) - to add item to begin.
            empty() - true if stack is empty.
            pop() - delete the last element in stack.
        """
        if len(_list) != 0:
            self.__list = [UStackElement(item) for item in _list]
        else:
            self.__list = _list
        
    def append(self, *items) -> UStackElement:
        for item in items:
            item = UStackElement(item)
            self.__list.append(item)
        return items
        
    def empty(self) -> bool:
        return len(self.__list) == 0
        
    def pop(self) -> UStackElement | None:
        if not self.empty():
            item: UStackElement = self.__list[-1]
            del self.__list[-1]
            return item
        else:
            return None
        
    def top(self) -> UStackElement | None:
        if not self.empty():
            return self.__list[-1]
        else:
            return None

    def __add__(self, stack: UStack) -> UStack:
        return UStack(self.__list + stack.__list)

    def __radd__(self, stack: UStack) -> UStack:
        return UStack(stack.__list + self.__list)
    
    def __len__(self) -> int:
        return len(self.__list)

s = UStack()
s.append(1, 2, 3, 4, 6)
s2 = UStack()
s2.append(1, 2, 3, 4, 5)
s3 = s + s2
print(s3.top())