# -*- encodibg: utf-8 -*-
from __future__ import annotations
from typing import Any

class UStack():
    def __init__(self, __list: list | tuple = list()) -> UStack:
        """
        UStack's methods:
            append(**items) - to add item to begin.
            empty() - true if stack is empty.
            pop() - delete the last element in stack.
        """
        self.__list = __list
        
    def pop(self) -> Any:
        return self.__list.pop()

    @property
    def top(self) -> Any | bool:
        if self:
            return self.__list[-1]
        else:
            return False

    @property
    def empty(self) -> bool:
        return len(self.__list) == 0

    def __add__(self, stack: UStack) -> UStack:
        return UStack(self.__list + stack.__list)

    def __radd__(self, stack: UStack) -> UStack:
        return UStack(stack.__list + self.__list)
    
    def __len__(self) -> int:
        return len(self.__list)
    
    def __nonzero__(self) -> bool:
        return len(self.__list) == 0