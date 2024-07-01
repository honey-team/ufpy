from __future__ import annotations
from typing import TypeVar, Generic, Iterable, Any

__all__ = (
    "UDeque"
)

VT = TypeVar("VT")

class UDeque(Generic[VT]):
    def __init__(self, __list: Iterable[VT] = []):
        self.__list = list(__list)

    def addend(self, value: VT):
        self.__list.append(value)

    def addbegin(self, value: VT):
        self.__list.insert(0, value)

    def popend(self):
        return self.__list.pop()

    def popbegin(self):
        return self.__list.pop(0)
    
    def setend(self, value: VT):
        self[1] = value

    def setbegin(self, value: VT):
        self[0] = value

    def end(self) -> VT:
        if self:
            return self.__list[-1]
        else:
            return None

    def begin(self) -> VT:
        if self:
            return self.__list[0]
        else:
            return None
    
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
        if isinstance(index, int):
            if index in (0, 1):
                return self.__list[index]
            else:
                raise IndexError(f"{index} out of range (0, 1)")
            
    def __setitem__(self, index: int, value: VT):
        if isinstance(index, int):
            if index == 0:
                self.__list[index] = value
            elif index == 1:
                self.__list[-index] = value
            else:
                raise IndexError(f"{index} out of range (0, 1)")
            
    def __delitem__(self, index: int):
        if isinstance(index, int):
            if index == 0:
                del self.__list[index]
            elif index == 1:
                del self.__list[-index]
            else:
                raise IndexError(f"{index} out of range (0, 1)")

    def __reversed__(self) -> UDeque:
        return UDeque((self.end(), self.begin()))
    
    def __str__(self) -> str:
        return str(self.__list)