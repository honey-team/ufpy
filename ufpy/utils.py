__all__ = (
    'get_items_for_several_keys',
    'set_items_for_several_keys',
    'del_items_for_several_keys',
)

from typing import TypeVar

from ufpy.typ import SupportsGet, SupportsSetItem, SupportsDelItem, AnyCollection

KT = TypeVar('KT')
VT = TypeVar('VT')
DV = TypeVar('DV')


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
