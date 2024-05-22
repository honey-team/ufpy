from typing import Generic, Literal, overload, TypeVar

from .cmp import cmp_generator

__all__ = (
    'UDict',
)

KT = TypeVar('KT')
VT = TypeVar('VT')

@cmp_generator
class UDict(Generic[KT, VT]):
    @overload
    def __init__(self, dictionary: dict[KT, VT]): ...
    @overload
    def __init__(self, **kwargs: VT): ...
    def __init__(self, dictionary = None, **kwargs):
        self.__dict = dictionary if dictionary else kwargs
    
    # dictionary
    @property
    def dictionary(self) -> dict[KT, VT]:
        return self.__dict
    
    @dictionary.setter
    def dictionary(self, value: "dict[KT, VT] | UDict"):
        if isinstance(value, UDict):
            value = value.dictionary
        self.__dict = value
    
    def __len__(self) -> int:
        return len(self.__dict.keys())
    
    def __cmp__(self, other: "dict[KT, VT] | UDict") -> int:
        return len(self) - len(other)
    
    def __eq__(self, other: "dict[KT, VT] | UDict") -> bool:
        if isinstance(other, UDict):
            other = other.dictionary
        return self.__dict == other
