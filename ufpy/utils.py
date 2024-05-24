__all__ = (
    'SupportsGetItem',
    'SupportsGet',
    'get_items_for_several_keys',
    'set_items_for_several_keys',
)

from typing import Protocol, TypeVar, Generic, Type

type AnyCollection[T] = tuple[T, ...] | list[T]

KT = TypeVar('KT')
VT = TypeVar('VT')
DV = TypeVar('DV')


class SupportsGetItem(Protocol, Generic[KT, VT]):
    def __getitem__(self, key: KT) -> VT: ...


class SupportsGet(Protocol, Generic[KT, VT]):
    def get(self, key: KT, default: DV) -> VT | DV: ...


class SupportsSetItem(Protocol, Generic[KT, VT]):
    def __setitem__(self, key: KT, value: VT) -> None: ...


def get_items_for_several_keys(o: SupportsGet[KT, VT], keys: AnyCollection[KT], default: DV = None) -> list[VT | DV]:
    return [o.get(k, default) for k in keys]


def set_items_for_several_keys(
        o: SupportsSetItem[KT, VT], keys: AnyCollection[KT], values: AnyCollection[VT]
) -> Type[SupportsSetItem[KT, VT]]:
    res = o
    for i, k in enumerate(keys):
        res[k] = values[i]
    return res
