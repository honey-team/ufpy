from __future__ import annotations
from typing import Generic, TypeVar, Any

__all__ = (
    "UPair"
)

VT = TypeVar("VT")

class UPair(Generic[VT]):
    def __init__(self, __first: VT = None, __second: VT = None):
        self.first = __first
        self.second = __second

    def is_empty(self) -> bool:
        return len(self) == 0
    
    def reversed(self) -> UPair:
        return self.__reversed__()

    def __setattr__(self, __name: str, __value: Any):
        if __name in ("first", "second"):
            self.__dict__[__name] = __value
        else:
            raise KeyError(f"Key not found: {__name}")
    
    def __getitem__(self, index: int):
        if isinstance(index, int):
            if index in (0, 1):
                return [self.first, self.second][index]
            else:
                raise IndexError(f"{index} out of range (0, 1)")

    def __setitem__(self, index: int, value: VT):
        if isinstance(index, int):
            if index == 0:
                self.first = value
            elif index == 1:
                self.second = value
            else:
                raise IndexError(f"{index} out of range (0, 1)")

    def __len__(self) -> int:
        return sum(map(lambda var: 1 if var else 0, (self.first, self.second)))

    def __nonzero__(self) -> bool:
        return not self.is_empty()
    
    def __str__(self) -> str:
        return str([self.first, self.second])
    
    def __reversed__(self) -> UPair:
        return UPair(self.first, self.second)