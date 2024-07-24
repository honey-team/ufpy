from __future__ import annotations

__all__ = (
    # Dicts/collections
    'SupportsGetItem',
    'SupportsGet',
    'SupportsSetItem',
    'SupportsDelItem',
    'SupportsIter',
    # Comparing
    'SupportsLT',
    'SupportsGT',
    'SupportsLE',
    'SupportsGE',
    'SupportsEQ',
    'SupportsNE',
    # Math operations
    'SupportsAdd',
    'SupportsSub',
    'SupportsMul',
    'SupportsTrueDiv',
    'SupportsFloorDiv',
    'SupportsMod',
    'SupportsPow',
    'SupportsLshift',
    'SupportsRshift',
    'SupportsAnd',
    'SupportsOr',
    'SupportsXor',
    'SupportsMathOperations',
    # Other magic methods
    'SupportsNeg',
    # Converting
    'Listable',
    # "Like"s
    'LikeDict',
    'LikeList',
    # Other
    'Reversed',
    'Sorted',
)

from typing import Protocol, Generic, TypeVar, Iterator, TYPE_CHECKING, runtime_checkable, Iterable

if TYPE_CHECKING:
    pass

# TypeVars

# Dicts
KT = TypeVar('KT')  # Type of key in like-dict object
VT = TypeVar('VT')  # Type of value in like-dict object
DV = TypeVar('DV')  # Class default value in like-dict object

# Dicts/collections
IT = TypeVar('IT')  # Type of thing, which iterates

# Math operations
OT = TypeVar('OT')  # Type of object (used in math operation's magic method)
MRT = TypeVar('MRT')  # Math result type (used in math operation's magic method)

# All
T = TypeVar('T')  # Anything


# Dicts and collections
@runtime_checkable
class SupportsGetItem(Protocol[KT, VT]):
    def __getitem__(self, key: KT) -> VT: ...


@runtime_checkable
class SupportsGet(Protocol[KT, VT]):
    def get(self, key: KT, default: DV) -> VT | DV: ...


@runtime_checkable
class SupportsSetItem(Protocol[KT, VT]):
    def __setitem__(self, key: KT, value: VT) -> None: ...


@runtime_checkable
class SupportsDelItem(Protocol[KT, VT]):
    def __delitem__(self, key: KT) -> None: ...


@runtime_checkable
class SupportsIter(Protocol[IT]):
    def __iter__(self) -> Iterator[IT]: ...


# Comparing
@runtime_checkable
class SupportsLT(Protocol[OT]):
    def __lt__(self, other: OT) -> bool: ...


@runtime_checkable
class SupportsGT(Protocol[OT]):
    def __gt__(self, other: OT) -> bool: ...


@runtime_checkable
class SupportsLE(Protocol[OT]):
    def __le__(self, other: OT) -> bool: ...


@runtime_checkable
class SupportsGE(Protocol[OT]):
    def __ge__(self, other: OT) -> bool: ...


@runtime_checkable
class SupportsEQ(Protocol[OT]):
    def __eq__(self, other: OT) -> bool: ...


@runtime_checkable
class SupportsNE(Protocol[OT]):
    def __ne__(self, other: OT) -> bool: ...


class SupportsComparing(
    SupportsLT[OT],
    SupportsGT[OT],
    SupportsLE[OT],
    SupportsGE[OT],
    SupportsEQ[OT],
    SupportsNE[OT]
):
    ...


# Math operations
@runtime_checkable
class SupportsAdd(Protocol[OT]):
    def __add__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsSub(Protocol[OT]):
    def __sub__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsMul(Protocol[OT]):
    def __mul__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsTrueDiv(Protocol[OT]):
    def __truediv__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsFloorDiv(Protocol[OT]):
    def __floordiv__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsMod(Protocol[OT]):
    def __mod__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsFloorDiv(Protocol[OT]):
    def __floordiv__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsPow(Protocol[OT]):
    def __pow__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsLshift(Protocol[OT]):
    def __lshift__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsRshift(Protocol[OT]):
    def __rshift__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsAnd(Protocol[OT]):
    def __and__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsOr(Protocol[OT]):
    def __or__(self, other: OT) -> MRT: ...


@runtime_checkable
class SupportsXor(Protocol[OT]):
    def __xor__(self, other: OT) -> MRT: ...


class SupportsBinaryOperations(
    SupportsLshift[OT],
    SupportsRshift[OT],
    SupportsAnd[OT],
    SupportsOr[OT],
    SupportsXor[OT]
):
    ...


class SupportsMathOperations(
    SupportsAdd[OT],
    SupportsSub[OT],
    SupportsMul[OT],
    SupportsTrueDiv[OT],
    SupportsFloorDiv[OT],
    SupportsMod[OT],
    SupportsPow[OT],
    SupportsBinaryOperations[OT]
):
    ...


# Other magic methods
@runtime_checkable
class SupportsNeg(Protocol):
    def __neg__(self) -> SupportsNeg: ...


# Converting

# TODO: More protocols for converting

class Listable(
    SupportsIter[T],
    Iterable[T],
    Generic[T]
):
    ...


# "Like"s
class LikeDict(
    SupportsGet[KT, VT],
    SupportsGetItem[KT, VT],
    SupportsSetItem[KT, VT],
    SupportsDelItem[KT, VT],
    Listable["KT | AnyBinaryCollection[KT, VT]"],
    Generic[KT, VT]
):
    ...


class LikeList(
    SupportsGetItem[int, T],
    SupportsSetItem[int, T],
    SupportsDelItem[int, T],
    Listable[T],
    Generic[T]
):
    ...


# Other
class Reversed(
    Protocol[T]
):
    def __reversed__(self) -> T: ...


class Sorted(
    Protocol[T]
):
    def sorted(self) -> T: ...
