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
from typing import TypeVar, Iterable, overload, TYPE_CHECKING

from ufpy.typ.protocols import SupportsSorted

if TYPE_CHECKING:
    from ufpy import SupportsTrueDiv, SupportsCompare
    from ufpy.typ import SupportsGet, SupportsSetItem, SupportsDelItem, AnyCollection, SupportsAvg

KT = TypeVar('KT')
VT = TypeVar('VT')
DV = TypeVar('DV')
T = TypeVar('T')


def get_items_for_several_keys(o: SupportsGet[KT, VT], keys: AnyCollection[KT], default: DV = None) -> list[VT | DV]:
    return [o.get(k, default) for k in keys]


def set_items_for_several_keys(
        o: SupportsSetItem[KT, VT], keys: AnyCollection[KT], values: AnyCollection[VT]
) -> SupportsSetItem[KT, VT]:
    for i, k in enumerate(keys):
        o[k] = values[i]
    return o


def del_items_for_several_keys(o: SupportsDelItem[KT, VT], keys: AnyCollection[KT]) -> SupportsDelItem[KT, VT]:
    for k in keys:
        del o[k]
    return o


def is_iterable(o: object) -> bool:
    return isinstance(o, Iterable)


@overload
def avg(*items: SupportsTrueDiv[int]) -> SupportsTrueDiv[int | float] | T: ...
@overload
def avg(*iterables: Iterable[SupportsTrueDiv[int]]) -> SupportsTrueDiv[int | float] | T: ...
@overload
def avg(*items_and_iterables: SupportsTrueDiv[int] | Iterable[SupportsTrueDiv[int]])\
        -> SupportsTrueDiv[int | float] | T: ...
def avg(*items_or_iterables: SupportsAvg) -> SupportsTrueDiv[int | float]:
    """
    Get average value of iterable's or args's values
    """
    l = []
    for i in items_or_iterables:
        if is_iterable(i): l += i
        else: l += [i]

    return sum(l) / len(l)


@overload
def mdn(*items: SupportsCompare[SupportsTrueDiv[int]] | SupportsTrueDiv[int]) -> SupportsTrueDiv[int | float] | T: ...
@overload
def mdn(*iterables: Iterable[SupportsTrueDiv[int]] | SupportsSorted[T]) -> T | SupportsTrueDiv[int | float] | T: ...
@overload
def mdn(*items_and_iterables: SupportsSorted[T] | SupportsAvg) -> T | SupportsTrueDiv[int | float] | T: ...
def mdn(*items_or_iterables: SupportsSorted[T] | SupportsAvg) -> T | SupportsTrueDiv[int | float] | T:
    """
    Get median of iterable or args
    """
    l = []
    for i in items_or_iterables:
        if is_iterable(i):
            l += i
        else:
            l += [i]
    l = sorted(l)

    if len(l) % 2 == 1: # Odd lenght - middle element
        return l[len(l) // 2]
    return avg(l[len(l) // 2], l[len(l) // 2 - 1]) # Even lenght - avg(middle elements)

@overload
def mod(*items: T) -> T | Iterable[T]: ...
@overload
def mod(*iterables: Iterable[T]) -> T | Iterable[T]: ...
@overload
def mod(*items_and_iterables: T | Iterable[T]) -> T | Iterable[T]: ...
def mod(*items_or_iterables: T | Iterable[T]) -> T | Iterable[T]:
    """
    Get mode of iterable or args
    """
    l = []
    for i in items_or_iterables:
        if is_iterable(i):
            l += i
        else:
            l += [i]

    counter = Counter(l)
    ans = []
    for k, v in counter.items():
        if v == max(counter.values()):
            ans.append(k)
    return ans[0] if len(ans) == 1 else ans

