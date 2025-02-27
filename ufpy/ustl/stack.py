from __future__ import annotations

from typing import Generic, TypeVar, Iterable, Callable

from ufpy.cmp import cmp_generator
from ufpy.math_op import r_generator, i_generator
from ufpy.typ import AnyCollection, NumberLiteral, SupportsMul, SupportsTrueDiv, Empty

# Marked for deletion in 0.5
# pylint: disable=all

__all__ = (
    "Stack",
)

T = TypeVar("T")
T2 = TypeVar("T2") # pylint: disable=invalid-name

def _convert_to_stack(other: Stack[T] | AnyCollection[T] | T) -> Stack[T]:
    if isinstance(other, Stack):
        return other
    if isinstance(other, (list, tuple)):
        return Stack(iterable=other)
    return Stack(other)

def _convert_to_list_for_mul_and_div(other: Stack[T] | AnyCollection[T] | T, __len: int = None) -> list[T]:
    if isinstance(other, Stack):
        return other.elements
    if isinstance(other, (list, tuple)):
        return list(other)
    return [other for _ in range(__len)]

@cmp_generator
@i_generator
@r_generator
class Stack(Generic[T]):
    """
    Class for simplifying working with stacks in Python.
    """
    def __init__(self, *elements: T, iterable: Iterable[T] = None):
        if iterable:
            elements = iterable
        self.__elements = list(elements) if elements else []

    # elements
    @property
    def elements(self) -> list[T]:
        return self.__elements

    @elements.setter
    def elements(self, value: Iterable[T]):
        self.__elements = list(value)

    @elements.deleter
    def elements(self):
        self.__elements.clear()

    # top
    @property
    def top(self) -> T | None:
        """
        Top element of stack.

        :return: Top element
        """
        return self.__elements[-1] if self else None

    @top.setter
    def top(self, value: T):
        self.__elements[-1] = value

    @top.deleter
    def top(self):
        del self.__elements[-1]

    # public methods
    def pop(self) -> T:
        """
        Remove and return top element.

        :return: Removed element
        """
        return self.__elements.pop()

    def push(self, *items: T) -> Stack[T]:
        """Append items to stack"""
        self.__elements.extend(items)
        return Stack(iterable=self.__elements)

    def remove(self, *items: T) -> Stack[T]:
        """
        Remove elements from stack
        """
        for i in items:
            self.__elements.remove(i)
        return Stack(iterable=self.__elements)

    def clear(self) -> Empty[Stack]:
        del self.elements
        return self

    # copying
    def copy(self) -> Stack[T]:
        return Stack(iterable=self.__elements.copy())

    def __copy__(self):
        return self.copy()

    # call
    def __call__(self, func: Callable[[int, T], T2]) -> Stack[T2]:
        elements = self.__elements.copy()
        for i, v in enumerate(elements):
            elements[i] = func(i, v)
        return Stack(iterable=elements)

    # math operations
    def __add__(self, other: Stack[T2] | AnyCollection[T2] | T2) -> Stack[T | T2]:
        other = _convert_to_stack(other)
        result = self.copy()
        return result.push(*other.elements)

    def __sub__(self, other: Stack[T] | AnyCollection[T] | T) -> Stack[T]:
        other = _convert_to_stack(other)
        result = self.copy()
        return result.remove(*other.elements)

    def __mul__(
        self: Stack[SupportsMul], other: Stack[NumberLiteral] | AnyCollection[NumberLiteral] | NumberLiteral
    ) -> Stack[SupportsMul]:
        other = _convert_to_list_for_mul_and_div(other, len(self))

        def mul(i: int, v: SupportsMul) -> SupportsMul:
            return v * other[i]

        return self(mul)

    def __truediv__(
        self: Stack[SupportsTrueDiv], other: Stack[NumberLiteral] | AnyCollection[NumberLiteral] | NumberLiteral
    ) -> Stack[SupportsTrueDiv]:
        other = _convert_to_list_for_mul_and_div(other, len(self))

        def div(i: int, v: SupportsTrueDiv) -> SupportsTrueDiv:
            return v / other[i]

        return self(div)

    # Booleans
    def __len__(self) -> int:
        return len(self.__elements)

    def is_empty(self) -> bool:
        return len(self) == 0

    def __bool__(self) -> bool:
        return not self.is_empty()

    def __eq__(self, other: Stack[T2]) -> bool:
        return self.elements == other.elements

    # Transform to other types
    def __repr__(self) -> str:
        return f's{self.__elements}'
