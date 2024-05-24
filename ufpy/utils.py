__all__ = (
    'get_items_for_several_keys',
    'set_items_for_several_keys',
)

from typing import TypeVar

from .protocols import SupportsGet, SupportsSetItem, SupportsDelItem

type AnyCollection[T] = tuple[T, ...] | list[T]

KT = TypeVar('KT')
VT = TypeVar('VT')
DV = TypeVar('DV')


def get_items_for_several_keys(o: SupportsGet[KT, VT], keys: AnyCollection[KT], default: DV = None) -> list[VT | DV]:
    return [o.get(k, default) for k in keys]


def set_items_for_several_keys(
        o: SupportsSetItem[KT, VT], keys: AnyCollection[KT], values: AnyCollection[VT]
) -> SupportsSetItem[KT, VT]:
    res = o
    for i, k in enumerate(keys):
        res[k] = values[i]
    return res


def del_items_for_several_keys(o: SupportsDelItem[KT, VT], keys: AnyCollection[KT]) -> SupportsDelItem[KT, VT]:
    res = o
    for k in keys:
        del res[k]
    return res
