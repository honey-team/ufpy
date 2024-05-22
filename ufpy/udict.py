from typing import Generic, Literal, overload, TypeVar

KT = TypeVar('KT')
VT = TypeVar('VT')

class UDict(Generic[KT, VT]):
    @overload
    def __init__(self, dict: dict[KT, VT]): ...
    @overload
    def __init__(self, **kwargs: VT): ...
    def __init__(self, dictionary = None, **kwargs):
        self.__dict = dictionary if dictionary else kwargs
    
    @property
    def dictionary(self) -> dict[KT, VT]:
        return self.__dict
    
    @dictionary.setter
    def dictionary(self, value: dict[KT, VT] | "UDict"):
        if isinstance(value, UDict):
            value = value.dictionary
        self.__dict = value
    
    def __len__(self) -> int:
        return len(self.__dict.keys())
    
    def __compare(self, other: dict[KT, VT] | "UDict") -> int | Literal['eq']:
        if isinstance(other, UDict):
            other = other.dictionary

        if self.__dict == other:
            return 'eq'
        return len(self) - len(other.keys())
    
    def __eq__(self, other: dict[KT, VT] | "UDict") -> bool:
        return self.__compare(other) == 'eq'
    
    def __ne__(self, other: dict[KT, VT] | "UDict") -> bool:
        return self.__compare(other) != 'eq'
