from __future__ import annotations
from typing import TypeVar, Generic, Any

__all__ = (
    "UDeque",
)

VT = TypeVar("VT")

class UDeque(Generic[VT]):
    def __init__(self, *__list):
        self.__list: list[VT] = list(__list)

    def addend(self, value: VT) -> VT:
        self.__list.append(value)
        return value

    def addbegin(self, value: VT) -> VT:
        self.__list.insert(0, value)
        return value

    def popend(self) -> VT:
        if self:
            return self.__list.pop()
        else:
            raise IndexError("list index out of range")

    def popbegin(self) -> VT:
        if self:
            return self.__list.pop(0)
        else:
            raise IndexError("list index out of range")
    
    def setend(self, value: VT) -> VT:
        if self:
            self[-1] = value
            return value
        else:
            raise IndexError("list index out of range")

    def setbegin(self, value: VT) -> VT:
        if self:
            self[0] = value
            return value
        else:
            raise IndexError("list index out of range")

    def end(self) -> Any:
        return self.__list[-1] if self else None

    def begin(self) -> Any:
        return self.__list[0] if self else None
    
    def copy(self) -> UDeque:
        return UDeque(self.__list.copy())
    
    def is_empty(self) -> bool:
        return len(self) == 0

    def reversed(self) -> UDeque:
        return self.__reversed__()
    
    def __len__(self) -> int:
        return len(self.__list)
    
    def __nonzero__(self) -> bool:
        return not self.is_empty()
    
    def __getitem__(self, index: Any) -> VT:
        if index in (0, -1):
            return self.__list[index]
        else:
            raise IndexError(f"{index} out of range")
            
    def __setitem__(self, index: int, value: VT):
        if index in (0, -1):
            self.__list[index] = value
        else:
            raise IndexError(f"{index} out of range")
            
    def __delitem__(self, index: int):
        if index in (0, -1):
            del self.__list[index]
        else:
            raise IndexError(f"{index} out of range")

    def __reversed__(self) -> UDeque:
        return UDeque((self.end(), self.begin()))
    
    def __str__(self) -> str:
        return str(self.__list)

    def __iter__(self) -> UDeque:
        return self

    def __next__(self) -> VT:
        if self.is_empty():
            raise StopIteration
        else:
            return self.popbegin()