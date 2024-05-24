__all__ = (
    'SupportsGetItem',
    'SupportsGet',
    'get_items_for_several_keys',
)

from typing import Protocol, TypeVar, Generic

KT = TypeVar('KT')
VT = TypeVar('VT')
DV = TypeVar('DV')

class SupportsGetItem(Protocol, Generic[KT, VT]):
    def __getitem__(self, key: KT) -> VT: ...

class SupportsGet(Protocol, Generic[KT, VT]):
    def get(self, key: KT, default: DV) -> VT | DV: ...

def get_items_for_several_keys(o: SupportsGet[KT, VT], keys: tuple[KT, ...], default: DV = None) -> tuple[VT | DV, ...]:
    return [o.get(k, default) for k in keys]
