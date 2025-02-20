from __future__ import annotations

__all__ = (
    'get_items_for_several_keys',
    'set_items_for_several_keys',
    'del_items_for_several_keys',
    'is_iterable',
    'avg',
)

from typing import TypeVar, Iterable, overload, TYPE_CHECKING

if TYPE_CHECKING:
    from ufpy import SupportsTrueDiv
    from ufpy.typ import SupportsGet, SupportsSetItem, SupportsDelItem, AnyCollection

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
def avg(*items: SupportsTrueDiv[int]): ...
@overload
def avg(*iterables: Iterable[SupportsTrueDiv[int]]): ...
@overload
def avg(items_and_iterables: SupportsTrueDiv[int] | Iterable[SupportsTrueDiv[int]]): ...
def avg(*items_or_iterables: SupportsTrueDiv[int] | Iterable[SupportsTrueDiv[int]]) -> SupportsTrueDiv[int | float]:
    """
    Get average value of iterable's or args's values
    """
    l = []
    for i in items_or_iterables:
        if is_iterable(i): l += i
        else: l += [i]

    return sum(l) / len(l)
