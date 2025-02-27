"""
Some useful utils
"""

from __future__ import annotations

__all__ = (
    'get_items_for_several_keys',
    'set_items_for_several_keys',
    'del_items_for_several_keys',
    'is_iterable',
    'avg',
    'mdn',
    'mod',
)

from collections import Counter
from typing import TypeVar, Iterable, TYPE_CHECKING


if TYPE_CHECKING:
    from ufpy import SupportsTrueDiv, SupportsCompare
    from ufpy.typ import SupportsGet, SupportsSetItem, SupportsDelItem, AnyCollection, SupportsAvg

KT = TypeVar('KT')
VT = TypeVar('VT')
DV = TypeVar('DV')
T = TypeVar('T')


def get_items_for_several_keys(o: SupportsGet[KT, VT], keys: AnyCollection[KT], default: DV = None) -> list[VT | DV]:
    """
    Get items for several keys. You can also specify default value if key is missing
    """
    return [o.get(k, default) for k in keys]


def set_items_for_several_keys(
        o: SupportsSetItem[KT, VT], keys: AnyCollection[KT], values: AnyCollection[VT]
) -> SupportsSetItem[KT, VT]:
    """
    Set items for several keys
    """
    for k, v in zip(keys, values):
        o[k] = v
    return o


def del_items_for_several_keys(o: SupportsDelItem[KT, VT], keys: AnyCollection[KT]) -> SupportsDelItem[KT, VT]:
    """
    Delete items for several keys
    """
    for k in keys:
        del o[k]
    return o


def is_iterable(o: object) -> bool:
    """
    Check that object is iterable
    """
    return isinstance(o, Iterable)


def _flatten(*items_or_iterables: T | Iterable[T]) -> list[T]:
    result = []
    for item in items_or_iterables:
        result += item if is_iterable(item) else [item]
    return result


def avg(*items_or_iterables: SupportsAvg) -> SupportsTrueDiv[int | float]:
    """
    Get average value of iterable's or args's values
    """
    l = _flatten(*items_or_iterables)

    if len(l) == 0:
        raise ValueError("Please, give at least one argument. avg() can't find average value of empty iterable")

    return sum(l) / len(l)


def mdn(*items_or_iterables: SupportsCompare[T] | SupportsAvg) -> T | SupportsTrueDiv[int | float]:
    """
    Get median of iterable or args
    """
    l = sorted(_flatten(*items_or_iterables))

    if len(l) == 0:
        raise ValueError("Please, give at least one argument. mdn() can't find median of empty iterable")

    if len(l) % 2 == 1: # Odd length - middle element
        return l[len(l) // 2]
    return avg(l[len(l) // 2], l[len(l) // 2 - 1]) # Even length - avg(middle elements)


def mod(*items_or_iterables: T | Iterable[T]) -> T | Iterable[T]:
    """
    Get mode of iterable or args
    """
    counter = Counter(_flatten(*items_or_iterables))
    ans = [k for k, v in counter.items() if v == max(counter.values())]
    return ans[0] if len(ans) == 1 else ans
