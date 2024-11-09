from __future__ import annotations
from os import environ

from ufpy.math_op import i_generator, r_generator
from ufpy.utils import withrepr

__all__ = (
    'USet',
    'U'
)

from typing import Iterable, Iterator, Optional, TypeVar, overload

T = TypeVar('T')
OT = TypeVar('OT')

@i_generator
@r_generator
class USet[T]:
    @overload
    def __init__(self, *values: T) -> None: ...
    @overload
    def __init__(self, *values: T, auto_update_U: bool) -> None: ...
    @overload
    def __init__(self, *, iterable: Iterable[T]) -> None: ...
    @overload
    def __init__(self, *, iterable: Iterable[T], auto_update_U: bool) -> None: ...

    def __init__(self, *values: T, iterable: Optional[Iterable[T]] = None, auto_update_U: bool = True) -> None:
        self.__set = set(iterable) if iterable else set(values)
        self.__auto_update_U = auto_update_U
        self.__update__()
        
    @property
    def set(self) -> set[T]:
        return self.__set
    
    @set.setter
    def set(self, value: Iterable[T]):
        self.__set = set(value)
        self.__update__()
        
    # When USet updates (not required, that new USet must be not same that old one)
    def __update__(self):
        if self.__auto_update_U:
            U(iterable=_get_U() | self)
    
    # Convert to other types
    def __repr__(self) -> str:
        return f'u{self.set if self.set else '{}'}'
    
    def __str__(self) -> str:
        return repr(self.set) if self.set else '{}'
    
    # Iteration
    def __iter__(self) -> Iterator[T]:
        return iter(self.__set)
    
    # Or
    def __or__(self, other: Iterable[OT]) -> USet[T | OT]:
        return USet(iterable=set(self) | set(other), auto_update_U=self.__auto_update_U)

    def __add__(self, other: Iterable[OT]) -> USet[T | OT]:
        return self | other

    # Substract
    def __sub__(self, other: Iterable[OT]) -> USet[T]:
        return USet(iterable=set(self) - set(other), auto_update_U=self.__auto_update_U)
    
    def __div__(self, other: Iterable[OT]) -> USet[T]:
        return self - other
    
    # And
    def __and__(self, other: Iterable[OT]) -> USet:
        return USet(iterable=set(self) & set(other), auto_update_U=self.__auto_update_U)
    
    def __mul__(self, other: Iterable[OT]) -> USet:
        return self & other
    
    # Not
    def __neg__(self) -> USet:
        return _get_U() - self

environ["ufpy_USet_U"] = "{}"

@overload
def U(*values: T) -> None: ...
@overload
def U(*, iterable: Iterable[T]) -> None: ...

@withrepr(lambda _: repr(_get_U()))
def U(*values: T, iterable: Optional[Iterable[T]] = None) -> None:
    environ["ufpy_USet_U"] = str(_get_U() + (USet(iterable=iterable, auto_update_U=False)
                                             if iterable else
                                             USet(*values, auto_update_U=False)))

def _convert_type(s: str):
    if "'" in s or '"' in s: return s.replace("'", '').replace('"', '')
    elif s.replace('-', '').isdigit(): return int(s)
    else: return s

def _get_U():
    s = environ["ufpy_USet_U"].replace('{', '').replace('}', '').replace('(', '').replace(')', '')
    st = s.split(', ')
    return USet(iterable=[x for i in st if (x := _convert_type(i))], auto_update_U=False)
