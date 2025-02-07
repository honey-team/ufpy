__all__ = (
    'SupportsGetItem',
    'SupportsGet',
    'SupportsSetItem',
    'SupportsDelItem',
    'LikeDict',
    'SupportsAdd',
    'SupportsSub',
    'SupportsMul',
    'SupportsTrueDiv',
    'SupportsMathOperations',
    'SupportsRead',
    'SupportsWrite',
    'ReadWriteIO'
)

from typing import Protocol, Generic, TypeVar

# Dicts/collections
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

# math operations
OT = TypeVar("OT")

class SupportsAdd(Protocol[OT]):
    def __add__(self, other: OT): ...

class SupportsSub(Protocol[OT]):
    def __sub__(self, other: OT): ...

class SupportsMul(Protocol[OT]):
    def __mul__(self, other: OT): ...

class SupportsTrueDiv(Protocol[OT]):
    def __truediv__(self, other: OT): ...

# TODO: More math operations

class SupportsMathOperations(
    SupportsAdd[OT],
    SupportsSub[OT],
    SupportsMul[OT],
    SupportsTrueDiv[OT],
    Generic[OT]
):
    ...

# IO

T = TypeVar('RT')

class SupportsRead(Protocol[T]):
    def read(self) -> T: ...

class SupportsWrite(Protocol[T]):
    def write(self, __data: T): ...

class ReadWriteIO(SupportsRead[T], SupportsWrite[T]):
    ...
