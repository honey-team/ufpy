from typing import Never, Iterable

from ufpy.typ.protocols import LikeDict, SupportsTrueDiv

__all__ = (
    'AnyCollection',
    'AnyDict',
    'NumberLiteral',
    'Empty',
    'SupportsAvg',
)

type AnyCollection[T] = tuple[T, ...] | list[T]
type AnyDict[KT, VT] = dict[KT, VT] | LikeDict[KT, VT]

type NumberLiteral = int | float

type Empty[T] = T[Never]

type SupportsAvg = SupportsTrueDiv[int] | Iterable[SupportsTrueDiv[int]]
