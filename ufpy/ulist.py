from __future__ import annotations

import sys
from collections import Counter
from typing import TypeVar, Generic, Callable, overload, Iterator

from ufpy.cmp import cmp_generator
from ufpy.math_op import generate_all_math_operations_magic_methods
from ufpy.typ.protocols import Listable, Reversed, Sorted, SupportsNeg, SupportsIter, SupportsLT, SupportsGT
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
        return self

    def reversed(self) -> Reversed[UList[T]]:
        """
        Returns reversed UList, but doesn't change it.
        """
        return UList(iterable=reversed(self.listing))

    def __invert__(self) -> Reversed[UList[T]]:
        return self.reversed()

    def __reversed__(self) -> Reversed[UList[T]]:
        return self.reversed()

    # sort
    def sort(self, *, key: Callable[[T], SupportsLT | SupportsGT] = None, reverse: bool = False) -> Sorted[UList[T]]:
        """
        Sorts UList and returns it.

        Args:
            key: Function which takes each element of the UList and returns element to sort by (optional)
            reverse: Need to reverse the order of the UList after sorting? (optional)

        Returns: Sorted UList
        """
        self.__list.sort(key=key, reverse=reverse)
        return self

    def sorted(self, *, key: Callable[[T], SupportsLT | SupportsGT] = None, reverse: bool = False) -> Sorted[UList[T]]:
        """
        Returns sorted UList, but doesn't change it.

        Args:
            key: Function which takes each element of the UList and returns element to sort by (optional)
            reverse: Need to reverse the order of the UList after sorting? (optional)

        Returns: Sorted UList
        """
        return UList(iterable=sorted(self.__list, key=key, reverse=reverse))

    def index(self, value: T, start: int = 1, stop: int = sys.maxsize) -> int | None:
        """
        Returns index of value.

        Args:
            value: Value to obtain index
            start: The index after which need to start searching for the index of the value (including itself) (optional)
            stop: The index before which to complete the search for the index of the value (including itself) (optional)

        Returns: Index of value or `None` if index didn't find

        """
        try:
            return self.__list.index(value, start - 1, stop - 1) + 1
        except ValueError:
            return None

    @overload
    def count(self) -> dict[T, int]:
        ...

    @overload
    def count(self, value: T) -> int:
        ...

    @overload
    def count(self, *values: T) -> dict[T, int]:
        ...

    def count(self, *values: T) -> int | dict[T, int]:
        """
        Count number of values

        Args:
            *values: Values to count.

        Returns: Counts of provided values provided in dict[value, count]. If len(values) == 1 -> return integer which
        is count of value. If len(values) == 0 -> return counts of every item in UList

        """
        counter = Counter(self.__list)
        if len(values) == 1:
            return counter[values[0]]
        elif len(values) == 0:
            counter_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
            return dict(counter_items)

        res = {}
        for v in values:
            res[v] = counter[v]
        return res

    def insert(self, index: int, *values: NT) -> UList[T | NT]:
        for i, v in enumerate(values):
            self.__list.insert(index + i - 1, v)
        return self

    def replace(self, old: T, new: NT) -> UList[T | NT]:
        self.__list[self.__list.index(old)] = new
        return self

    def append(self, *values: NT, to_start: bool = False) -> UList[T | NT]:
        if to_start:
            self.__list = list(values) + self.__list
        else:
            self.__list.extend(values)
        return self

    def remove(self, *values: T, from_end: bool = False) -> UList[T]:
        if from_end:
            self.__list.reverse()

        for i in values:
            self.__list.remove(i)

        if from_end:
            self.reverse()
        return self

    def extend(self, iterable: AnyList[NT], to_start: bool = False) -> UList[T | NT]:
        return self.append(*iterable, to_start=to_start)

    def reduce(self, iterable: AnyList[T], from_end: bool = False) -> UList[T]:
        return self.remove(*iterable, from_end=from_end)

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
