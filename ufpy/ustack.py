from __future__ import annotations

from typing import Generic, TypeVar, Iterable, Callable

from .cmp import cmp_generator
from .math_op import r_generator, i_generator
from .typ import AnyCollection, NumberLiteral, SupportsMul, SupportsTrueDiv, Empty

__all__ = (
    "UStack",
)

T = TypeVar("T")
T2 = TypeVar("T2")

def convert_to_stack(other: UStack[T] | AnyCollection[T] | T) -> UStack[T]:
    if isinstance(other, UStack):
        return other
    if isinstance(other, (list, tuple)):
        return UStack(iterable=other)
    return UStack(other)

def convert_to_list_for_mul_and_div(other: UStack[T] | AnyCollection[T] | T, __len: int = None) -> list[T]:
    if isinstance(other, UStack):
        return other.elements
    if isinstance(other, (list, tuple)):
        return list(other)
    return [other for _ in range(__len)]

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

    def push(self, *items: T) -> UStack[T]:
        """Append items to stack"""
        self.__elements.extend(items)
        return UStack(iterable=self.__elements)

    def remove(self, *items: T) -> UStack[T]:
        for i in items:
            self.__elements.remove(i)
        return UStack(iterable=self.__elements)

    def clear(self) -> Empty[UStack]:
        del self.elements
        return self

    # copying
    def copy(self) -> UStack[T]:
        return UStack(iterable=self.__elements.copy())

    def __copy__(self):
        return self.copy()

    # call
    def __call__(self, func: Callable[[int, T], T2]) -> UStack[T2]:
        elements = self.__elements.copy()
        for i, v in enumerate(elements):
            elements[i] = func(i, v)
        return UStack(iterable=elements)

    # math operations
    def __add__(self, other: UStack[T2] | AnyCollection[T2] | T2) -> UStack[T | T2]:
        other = convert_to_stack(other)
        result = self.copy()
        return result.push(*other.elements)

    def __sub__(self, other: UStack[T] | AnyCollection[T] | T) -> UStack[T]:
        other = convert_to_stack(other)
        result = self.copy()
        return result.remove(*other.elements)

    def __mul__(
        self: UStack[SupportsMul], other: UStack[NumberLiteral] | AnyCollection[NumberLiteral] | NumberLiteral
    ) -> UStack[SupportsMul]:
        other = convert_to_list_for_mul_and_div(other, len(self))

        def mul(i: int, v: SupportsMul) -> SupportsMul:
            return v * other[i]

        return self(mul)

    def __truediv__(
        self: UStack[SupportsTrueDiv], other: UStack[NumberLiteral] | AnyCollection[NumberLiteral] | NumberLiteral
    ) -> UStack[SupportsTrueDiv]:
        other = convert_to_list_for_mul_and_div(other, len(self))

        def div(i: int, v: SupportsTrueDiv) -> SupportsTrueDiv:
            return v / other[i]

        return self(div)

    # Booleans
    def __len__(self) -> int:
        return len(self.__elements)

    def is_empty(self) -> bool:
        return len(self) == 0
    
    def __nonzero__(self) -> bool:
        return not self.is_empty()

    # Transform to other types
    def __repr__(self) -> str:
        return f's{self.__elements}'
