from typing import Generic, Iterator, Literal, overload, TypeVar

from .cmp import cmp_generator
from .i import i_generator

__all__ = (
    'UDict',
)

KT = TypeVar('KT')
VT = TypeVar('VT')

@cmp_generator
@i_generator
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

    # Get items
    def __getitem__(self, key: KT | int | slice): ...
    def __setitem__(self, key: KT | int | slice, value: VT): ...
    def __delitem__(self, key: KT | int | slice): ...
    
    
    def __getattr__(self, name: str): ...
    def __setattr__(self, name: str, value: VT): ...
    def __delattr__(self, name: str): ...

        
    # Len, iterator and reversed version
    def __len__(self) -> int:
        return len(self.__dict.keys())
    
    def __iter__(self) -> Iterator[tuple[KT, VT]]:
        res = []
        
        for k, v in self.__dict.items():
            res.append((k, v))
        
        return iter(res)
    
    def __reversed__(self) -> 'UDict': ...
    
    # Booleans
    def __contains__(self, item: tuple[KT, VT] | KT) -> bool: ...
    
    # Comparing
    def __cmp__(self, other: "dict[KT, VT] | UDict") -> int:
        return len(self) - len(other)
    
    def __eq__(self, other: "dict[KT, VT] | UDict") -> bool:
        if isinstance(other, UDict):
            other = other.dictionary
        return self.__dict == other
    
    # Math operations
    def __add__(self, other: "dict[KT, VT] | UDict") -> "UDict":
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other = other.dictionary
        
        for k, v in other.items():
            new_dict[k] = v
        return UDict(new_dict)
    
    def __sub__(self, other: "dict[KT, VT] | UDict") -> "UDict":
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other = other.dictionary
        
        for k, v in other.items():
            if new_dict.get(k) == v:
                del new_dict[k]
        return UDict(new_dict)
    
    def __mul__(self, other: "dict[KT, float | int] | UDict[KT, float | int] | float | int") -> "UDict":
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other = other.dictionary
        if isinstance(other, (int, float)):
            other = dict([(k, other) for k in new_dict.keys()])
        
        for k, v in other.items():
            new_dict[k] *= v
        
        return UDict(new_dict)

    def __truediv__(self, other: "dict[KT, float | int] | UDict[KT, float | int] | float | int") -> "UDict":
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other = other.dictionary
        if isinstance(other, (int, float)):
            other = dict([(k, other) for k in new_dict.keys()])
        
        for k, v in other.items():
            new_dict[k] /= v
        
        return UDict(new_dict)
