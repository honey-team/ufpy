from __future__ import annotations

from typing import TypeVar, Generic, Callable, SupportsIndex

from ufpy.typ import AnyCollection

T = TypeVar('T')

class UList(Generic[T]):
    def __init__(self, __list: list[T] | UList[T]) -> None:
        if isinstance(__list, UList):
            __list = __list.listing
        self.__list = __list

    @property
    def listing(self) -> list[T]:
        return self.__list.copy()

    @listing.setter
    def listing(self, value: AnyCollection[T] | set[T] | UList[T]):
        if isinstance(value, UList):
            value = value.listing
        self.__list = list(value)

    def reversed(self):
        new_list = self.listing
        new_list.reverse()
        return UList(new_list)

    def count(self, value: T) -> int:
        return self.__list.count(value)
    
    def insert(self, index: SupportsIndex, object: T) -> None:
        self.__list.insert(index, object)

    def replace(self, old, new):
        new_list = self.listing
        for i, v in enumerate(new_list):
            if v == old:
                new_list[i] = new
        self.__list = new_list

    def __call__(self, func: Callable[[T], T]) -> UList[T]:
        new_dict = self.list
        for k, v in self:
            new_dict[k] = func(k, v)
        return UList(new_dict)

    def __getitem__(self, key: int) -> T:
        return self.__list[key]
    
    def __repr__(self) -> str:
        return f'u{self.__list}'

    def __add__(self, other) -> UList[T]:
        new_list = self.listing.copy()
        new_list.append(other)

        return UList(new_list)
    
    def __radd__(self, other) -> UList[T]:
        return self + other

    def __sub__(self, other) -> UList[T]:
        new_list = self.listing.copy()
        new_list.remove(other)

        return UList(new_list)