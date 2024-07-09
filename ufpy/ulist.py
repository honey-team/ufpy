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

    def __repr__(self) -> str:
        return f'u{self.listing}'

    def __add__(self, other: dict[T] | UList[T] | int[T] | str[T]) -> UList[T]:
        if isinstance(other, int):
            new_list = []
            for i in self.listing:
                new_list.append(int(i) + other)
        elif isinstance(other, str):
            new_list = []
            for i in self.listing:
                new_list.append(str(i) + other) 
        elif isinstance(other, list):
            new_list = self.listing.copy()
            for i in other:
                new_list.append(i)
        elif isinstance(other, UList):
            new_list = self.listing.copy()
            for i in other.listing:
                new_list.append(i)

        return UList(new_list)
    
    def __sub__(self, other) -> UList[T]:
        new_list = self.listing.copy()
        new_list.remove(other)

        return UList(new_list)