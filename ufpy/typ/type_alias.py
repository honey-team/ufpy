from .protocols import LikeDict

__all__ = (
    'AnyCollection',
    'AnyDict'
)

type AnyCollection[T] = tuple[T, ...] | list[T]
type AnyDict[KT, VT] = dict[KT, VT] | LikeDict[KT, VT]
