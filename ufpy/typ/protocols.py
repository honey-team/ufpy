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
    'SupportsLt',
    'SupportsLe',
    'SupportsEq',
    'SupportsNe',
    'SupportsGe',
    'SupportsGt',
    'SupportsCompare',
    'SupportsRead',
    'SupportsWrite',
    'ReadWriteIO',
    'SupportsSorted',
)

from typing import Protocol, TypeVar, Iterable

# Dicts/collections

KT = TypeVar('KT')
VT = TypeVar('VT')
DV = TypeVar('DV')


class SupportsGetItem(Protocol[KT, VT]):
    def __getitem__(self, key: KT) -> VT: ...


class SupportsGet(Protocol[KT, VT]):
    def get(self, key: KT, default: DV) -> VT | DV: ...


class SupportsSetItem(Protocol[KT, VT]):
    def __setitem__(self, key: KT, value: VT) -> None: ...


class SupportsDelItem(Protocol[KT, VT]):
    def __delitem__(self, key: KT) -> None: ...


class LikeDict(
    SupportsGet[KT, VT],
    SupportsGetItem[KT, VT],
    SupportsSetItem[KT, VT],
    SupportsDelItem[KT, VT]
):
    ...

# Math operations

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
    SupportsTrueDiv[OT]
):
    ...

# Compare

class SupportsLt(Protocol[OT]):
    def __lt__(self, other: OT) -> bool: ...

class SupportsLe(Protocol[OT]):
    def __le__(self, other: OT) -> bool: ...

class SupportsEq(Protocol[OT]):
    def __eq__(self, other: OT) -> bool: ...

class SupportsNe(Protocol[OT]):
    def __ne__(self, other: OT) -> bool: ...

class SupportsGe(Protocol[OT]):
    def __ge__(self, other: OT) -> bool: ...

class SupportsGt(Protocol[OT]):
    def __gt__(self, other: OT) -> bool: ...

class SupportsCompare(
    SupportsLt[OT],
    SupportsLe[OT],
    SupportsEq[OT],
    SupportsNe[OT],
    SupportsGe[OT],
    SupportsGt[OT]
):
    ...

# IO

T = TypeVar('T')

class SupportsRead(Protocol[T]):
    def read(self) -> T: ...

class SupportsWrite(Protocol[T]):
    def write(self, __data: T): ...

class ReadWriteIO(SupportsRead[T], SupportsWrite[T]):
    ...

# Other

class SupportsSorted(Protocol[T]):
    def __sorted__(self) -> Iterable[T]: ...
