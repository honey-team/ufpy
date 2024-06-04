from __future__ import annotations

from typing import Generic, TypeVar, Iterable

from .cmp import cmp_generator
from .math_op import r_generator, i_generator

T = TypeVar("T")
T2 = TypeVar("T2")

__all__ = (
    "UStack",
)

@cmp_generator
@i_generator
@r_generator
class UStack(Generic[T]):
    """
    Class for simplifying working with stacks in Python.
    """
    def __init__(self, *elements: T, iterable: Iterable[T] = None):
        if iterable:
            elements = iterable
        self.__list = list(elements) if elements else []

    @property
    def list(self) -> list[T]:
        return self.__list

    @list.setter
    def list(self, value: list[T]):
        self.__list = value

    def pop(self) -> T:
        """
        Remove and return top element.

        :return: Removed element
        """
        return self.__list.pop()

    @property
    def top(self) -> T | None:
        """
        Top element of stack.

        :return: Top element
        """
        if self:
            return self.__list[-1]
        return None

    def append(self, *items: T) -> UStack[T]:
        """Append items to stack"""
        self.__list.extend(items)
        return UStack(self.__list)

    def __add__(self, stack: UStack[T2] | T2) -> UStack[T | T2]:
        if not isinstance(stack, UStack):
            stack = UStack(stack)
        return UStack(self.__list + stack.__list)

    # Booleans
    def __len__(self) -> int:
        return len(self.__list)

    def is_empty(self) -> bool:
        return len(self) == 0
    
    def __nonzero__(self) -> bool:
        return not self.is_empty()

    # Transform to other types
    def __repr__(self) -> str:
        return f's{self.__list}'
