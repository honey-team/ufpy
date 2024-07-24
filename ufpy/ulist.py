from __future__ import annotations

import sys
from collections import Counter
from typing import TypeVar, Generic, Callable, overload, Iterator

from ufpy.cmp import cmp_generator
from ufpy.math_op import generate_all_math_operations_magic_methods
from ufpy.typ.protocols import Listable, Reversed, Sorted, SupportsNeg, SupportsIter
from ufpy.typ.type_alias import AnyList, MathOperations
from ufpy.utils import is_iterable

__all__ = (
    'UList',
)

T = TypeVar('T')
NT = TypeVar('NT')


@cmp_generator
@generate_all_math_operations_magic_methods
class UList(Generic[T]):
    @overload
    def __init__(self, *, iterable: AnyList[T] | Listable[T] | UList[T]) -> None:
        ...

    @overload
    def __init__(self, *args: T) -> None:
        ...

    def __init__(self, *args: T, iterable: AnyList[T] | Listable[T] | UList[T] = None) -> None:
        if iterable:
            self.__list = list(iterable)
        else:
            self.__list = list(args)

    @property
    def listing(self) -> list[T]:
        return self.__list.copy()

    @listing.setter
    def listing(self, value: Listable[T]):
        self.__list = list(value)

    # call
    def __call__(self, func: Callable[[int, T], NT]) -> UList[NT]:
        new_list = self.__list
        for i, v in enumerate(self):
            new_list[i] = func(i, v)
        return UList(iterable=new_list)

    # make negative numbers
    def __neg__(self: UList[SupportsNeg]) -> UList[NT]:
        return self(lambda i, v: -v)

    # reverse
    def reverse(self) -> Reversed[UList[T]]:
        """
        Reverses UList and returns it.
        """
        self.__list.reverse()
        return UList(iterable=self.listing)

    def reversed(self) -> Reversed[UList[T]]:
        """
        Returns reversed UList, but doesn't change it
        """
        return UList(iterable=reversed(self.listing))

    def __invert__(self) -> Reversed[UList[T]]:
        return self.reversed()

    def __reversed__(self) -> Reversed[UList[T]]:
        return self.reversed()

    # sort
    def sort(self) -> Sorted[UList[T]]:
        self.__list.sort()
        return UList(iterable=self.listing)

    def sorted(self) -> Sorted[UList[T]]:
        return UList(iterable=sorted(self.__list))

    def index(self, value: T, start: int = 1, stop: int = sys.maxsize) -> int:
        return self.__list.index(value, start - 1, stop - 1) + 1

    @overload
    def count(self, value: T) -> int:
        ...

    @overload
    def count(self, value: AnyList[T]) -> dict[T, int]:
        ...

    def count(self, value: T | AnyList[T]) -> int | dict[T, int]:
        counter = Counter(self.__list)
        if is_iterable(value):
            res = {}
            for v in value:
                res[v] = counter[v]
            return res
        return counter[value]

    def insert(self, index: int, value: T) -> T:
        self.__list.insert(index, value)
        return value

    def replace(self, old: T, new: NT) -> UList[T | NT]:
        self.__list[self.__list.index(old)] = new
        return self

    def extend(self, iterable: AnyList[NT]) -> UList[T | NT]:
        self.__list.extend(iterable)
        return self

    def remove(self, value_or_iterable: T | AnyList[T]) -> UList[T]:
        if is_iterable(value_or_iterable):
            iterable = value_or_iterable
        else:
            iterable = [value_or_iterable]

        for i in iterable:
            self.__list.remove(i)
        return self

    def __get_indexes_from_slice_or_int(self, index: int | slice) -> list[int]:
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self) + 1)
            res = list(range(start, stop + 1, step))
            return res
        if index == 0:
            raise IndexError("You can't use 0 as index in UList. Use 1 index instead.")
        return [index]

    def __getitem__(self, index: int | slice) -> T:
        indexes = self.__get_indexes_from_slice_or_int(index)

        res = [self.__list[i - 1] for i in indexes]
        return res if len(res) > 1 else res[0]

    def __setitem__(self, index: int | slice, value: NT | SupportsIter[NT]) -> None:
        indexes = self.__get_indexes_from_slice_or_int(index)
        values = value if is_iterable(value) else [value for _ in range(len(indexes))]

        if len(indexes) > len(values):
            values.extend([values[-1] for _ in range(len(indexes) - len(values) + 1)])

        for i, ind in enumerate(indexes):
            self.__list[i - 1] = values[i]

    def __delitem__(self, index: int | slice) -> None:
        indexes = self.__get_indexes_from_slice_or_int(index)

        for i in indexes:
            del self.__list[i - 1]

    def get(self, index: int) -> T:
        return self[index]

    def __len__(self) -> int:
        """
        Returns `len(self)`
        """
        return len(self.__list)

    def __iter__(self) -> Iterator[T]:
        """
        Implements `iter(self)`.
        """
        return iter(self.__list)

    # Booleans
    def is_empty(self) -> bool:
        """
        Returns `True` if `len(self)` equals `0`
        """
        return len(self) == 0

    def __bool__(self) -> bool:
        """
        Returns `False` if `len(self)` equals `0`
        """
        return not self.is_empty()

    def __contains__(self, item: T) -> bool:
        """
        Returns `True` if `item` is in `UDict`
        """
        return item in self.__list

    # Transform to other types
    def __repr__(self) -> str:
        return f'u{self.__list}'

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def __math__(
            self,
            other: NT | Listable[NT] | int,
            math_op: MathOperations
    ) -> UList[T] | UList[T | NT]:
        if is_iterable(other):
            other = list(other)
        elif math_op in ['+', '-']:
            other = [other]
        match math_op:
            case '+':
                l = self.listing
                l.extend(other)
                return UList(iterable=l)
            case '-':
                l = self.listing
                for i in other:
                    l.remove(i)
                return UList(iterable=l)
