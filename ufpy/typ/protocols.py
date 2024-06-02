__all__ = (
    'SupportsGetItem',
    'SupportsGet',
    'SupportsSetItem',
    'SupportsDelItem',
    'LikeDict',
)

from typing import Protocol, Generic, TypeVar

KT = TypeVar('KT')
VT = TypeVar('VT')
DV = TypeVar('DV')


class SupportsGetItem(Protocol, Generic[KT, VT]):
    def __getitem__(self, key: KT) -> VT: ...


class SupportsGet(Protocol, Generic[KT, VT]):
    def get(self, key: KT, default: DV) -> VT | DV: ...


class SupportsSetItem(Protocol, Generic[KT, VT]):
    def __setitem__(self, key: KT, value: VT) -> None: ...


class SupportsDelItem(Protocol, Generic[KT, VT]):
    def __delitem__(self, key: KT) -> None: ...


class LikeDict(
    SupportsGet[KT, VT],
    SupportsGetItem[KT, VT],
    SupportsSetItem[KT, VT],
    SupportsDelItem[KT, VT],
    Generic[KT, VT]
):
    ...
