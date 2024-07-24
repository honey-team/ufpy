from typing import Never, Literal

from ufpy.typ.protocols import LikeDict, LikeList

__all__ = (
    'AnyCollection',
    'AnyBinaryCollection',
    'AnyDict',
    'AnyList',
    'NumberLiteral',
    'Empty',
    'MathOperations',
)

type AnyCollection[T] = tuple[T, ...] | list[T] | LikeList[T]
type AnyBinaryCollection[T1, T2] = tuple[T1, T2] | list[T1 | T2] | LikeList[T1 | T2]
type AnyDict[KT, VT] = dict[KT, VT] | LikeDict[KT, VT]
type AnyList[T] = list[T] | reversed[list[T]] | LikeList[T] | reversed[LikeList[T]]

type NumberLiteral = int | float

type Empty[T] = T[Never]

type MathOperations = Literal['+', '-', '*', '/', '//', '%', '**', '<<', '>>', '&', '|', '^']
