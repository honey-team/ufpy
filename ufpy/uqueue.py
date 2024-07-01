from __future__ import annotations
from typing import Generic, TypeVar, Any

__all__ = (
    "UQueue",
)

VT = TypeVar("VT")

class UQueue(Generic[VT]):
    def __init__(self, *__list):
        self.__list: list[VT] = list(__list)
        self.__index = 0

    def pop(self) -> VT:
        return self.__list.pop(0)

    def push(self, value: VT) -> VT:
        self.__list.append(value)
        return value
    
    @property
    def head(self) -> None:
        return self.__list[-1] if self else None
    
    def copy(self) -> UQueue:
        return UQueue(self.__list.copy())

    def set_head(self, value: VT) -> VT:
        if self:
            self.__list[-1] = value
            return value
        else:
            raise IndexError("Index out of range")

    def is_empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return len(self.__list)

    def __nonzero__(self) -> bool:
        return not self.is_empty()

    def __str__(self) -> str:
        return str(self.__list)

    def __iter__(self) -> UQueue:
        return self
    
    def __next__(self) -> VT:
        if self.is_empty():
            raise StopIteration
        else:
            return self.__list.pop(0)