from __future__ import annotations

from typing import TypeVar, Generic

from ufpy.typ import AnyCollection

T = TypeVar('T')

class UList(Generic[T]):
    def __init__(self, __list: list[T] | UList[T]) -> None:
        if isinstance(__list, UList):
            __list = __list.listing
        self.__list = __list

    @property
    def listing(self) -> list[T]:
        return self.__list

    @listing.setter
    def listing(self, value: AnyCollection[T] | set[T] | UList[T]):
        if isinstance(value, UList):
            value = value.listing
        self.__list = list(value)
