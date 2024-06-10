from typing import Never

from ufpy.typ.protocols import LikeDict

__all__ = (
    'AnyCollection',
    'AnyDict',
    'NumberLiteral',
    'Empty',
)

type AnyCollection[T] = tuple[T, ...] | list[T]
type AnyDict[KT, VT] = dict[KT, VT] | LikeDict[KT, VT]

type NumberLiteral = int | float

type Empty[T] = T[Never]
