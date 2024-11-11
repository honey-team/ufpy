from __future__ import annotations

from ufpy.math_op import i_generator, r_generator
from ufpy.utils import is_iterable

__all__ = (
    'USet',
)

from typing import Iterable, Iterator, Optional, TypeVar, overload

T = TypeVar('T')
OT = TypeVar('OT')

@i_generator
@r_generator
class USet[T]:
    U: USet = None
    
    @overload
    def __init__(self, *values: T) -> None: ...
    @overload
    def __init__(self, *values: T, auto_update_U: bool) -> None: ...
    @overload
    def __init__(self, *, iterable: Iterable[T]) -> None: ...
    @overload
    def __init__(self, *, iterable: Iterable[T], auto_update_U: bool) -> None: ...

    def __init__(self, *values: T, iterable: Optional[Iterable[T]] = None, auto_update_U: bool = True) -> None:
        if USet.U == None and auto_update_U:
            USet.U = _U()
        
        self.__set = list(sorted(set(iterable))) if iterable else list(sorted(set(values)))
        self.__auto_update_U = auto_update_U
        self.__update__()
        
    @property
    def set(self) -> set[T]:
        return set(self.__set)
    
    @set.setter
    def set(self, value: Iterable[T]):
        self.__set = list(value)
        self.__update__()
        
    # When USet updates (not required, that new USet must be not same that old one)
    def __update__(self):
        if self.__auto_update_U:
            USet.U |= self
    
    # Convert to other types
    def __repr__(self) -> str:
        return 'u{' + ', '.join([str(i) for i in self.__set]) + '}'

    # Iteration
    def __iter__(self) -> Iterator[T]:
        return iter(self.__set)
    
    # Or
    def _or(self, other: Iterable[OT] | OT) -> USet[T | OT]:
        if not is_iterable(other):
            other = [other]
        return USet(iterable=set(self) | set(other), auto_update_U=self.__auto_update_U)
    
    def __or__(self, other: Iterable[OT] | OT) -> USet[T | OT]:
        return self._or(other)

    def __add__(self, other: Iterable[OT] | OT) -> USet[T | OT]:
        return self._or(other)

    # Substract
    def sub(self, other: Iterable[OT] | OT) -> USet[T]:
        if not is_iterable(other):
            other = [other]
        return USet(iterable=set(self) - set(other), auto_update_U=self.__auto_update_U)
    
    def __sub__(self, other: Iterable[OT] | OT) -> USet[T]:
        return self.sub(other)
    
    def __rsub__(self, other: Iterable[OT] | OT) -> USet[T]:
        return USet(iterable=other if is_iterable(other) else [other]).sub(self)
    
    def __truediv__(self, other: Iterable[OT] | OT) -> USet[T]:
        return self.sub(other)
    
    # And
    def _and(self, other: Iterable[OT] | OT) -> USet:
        if not is_iterable(other):
            other = [other]
        return USet(iterable=set(self) & set(other), auto_update_U=self.__auto_update_U)
    
    def __and__(self, other: Iterable[OT] | OT) -> USet:
        return self._and(other)
    
    def __mul__(self, other: Iterable[OT] | OT) -> USet:
        return self._and(other)
    
    # Not
    def _not(self, s: Optional[USet[OT]] = None) -> USet[OT]:
        return (s or USet.U) - self

    def __neg__(self) -> USet:
        return self._not()
    
    # Implication
    def implicate(self, other: Iterable[OT] | OT) -> USet:
        if not is_iterable(other):
            other = [other]
        return USet(iterable=(-self + other), auto_update_U=self.__auto_update_U)
    
    def __gt__(self, other: Iterable[OT] | OT) -> USet:
        return self.implicate(other)
    
    def __ge__(self, other: Iterable[OT] | OT) -> USet:
        return self > other
    
    def __lt__(self, other: Iterable[OT] | OT) -> USet:
        other2 = USet(*(other if is_iterable(other) else [other]))
        return other2.implicate(self)
    
    def __le__(self, other: Iterable[OT] | OT) -> USet:
        return self < other


class _U(USet[T]):
    def __init__(self, *values: T) -> None:
        super().__init__(*values, auto_update_U=False)
