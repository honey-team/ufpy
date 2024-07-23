from __future__ import annotations

__all__ = (
    'SupportsGetItem',
    'SupportsGet',
    'SupportsSetItem',
    'SupportsDelItem',
    'SupportsIter',
    'SupportsAdd',
    'SupportsSub',
    'SupportsMul',
    'SupportsTrueDiv',
    'SupportsMathOperations',
    'Listable',
    'LikeDict',
    'LikeList',
)

from typing import Protocol, Generic, TypeVar, Iterator, TYPE_CHECKING

if TYPE_CHECKING:
    from ufpy.typ.type_alias import AnyBinaryCollection

# TypeVars

# Dicts
KT = TypeVar('KT')  # Type of key in like-dict object
VT = TypeVar('VT')  # Type of value in like-dict object
DV = TypeVar('DV')  # Class default value in like-dict object

# Collections
T = TypeVar('T')  # Type of value in collection

# Dicts/collections
IT = TypeVar('IT')  # Type of thing, which iterates

# Math operations
OT = TypeVar('OT')  # Type of object (used in math operation's magic method)


class SupportsGetItem(Protocol[KT, VT]):
    def __getitem__(self, key: KT) -> VT: ...


class SupportsGet(Protocol[KT, VT]):
    def get(self, key: KT, default: DV) -> VT | DV: ...


class SupportsSetItem(Protocol[KT, VT]):
    def __setitem__(self, key: KT, value: VT) -> None: ...


class SupportsDelItem(Protocol[KT, VT]):
    def __delitem__(self, key: KT) -> None: ...


class SupportsIter(Protocol[IT]):
    def __iter__(self) -> Iterator[IT]: ...


# Math operations

# TODO: More math operations

class SupportsAdd(Protocol[OT]):
    def __add__(self, other: OT): ...


class SupportsSub(Protocol[OT]):
    def __sub__(self, other: OT): ...


class SupportsMul(Protocol[OT]):
    def __mul__(self, other: OT): ...


class SupportsTrueDiv(Protocol[OT]):
    def __truediv__(self, other: OT): ...


class SupportsMathOperations(
    SupportsAdd[OT],
    SupportsSub[OT],
    SupportsMul[OT],
    SupportsTrueDiv[OT]
):
    ...


# Converting

# TODO: More protocols for converting

class Listable(
    SupportsIter[T],
    Generic[T]
):
    ...


# "Like"s
class LikeDict(
    SupportsGet[KT, VT],
    SupportsGetItem[KT, VT],
    SupportsSetItem[KT, VT],
    SupportsDelItem[KT, VT],
    Listable[KT | AnyBinaryCollection[KT, VT]],
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
