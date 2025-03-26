from __future__ import annotations

__all__ = (
    'FunctionSequence',
    'ArithmeticProgression',
    'GeometricProgression'
)

from typing import Callable, TypeVar, Generic, overload, Any
from abc import ABC, abstractmethod

from ufpy.utils import mul
from ufpy.cmp import cmp_generator

VT = TypeVar('VT', int, float, int | float)
KT = TypeVar('KT', int, float, int | float)

VT2 = TypeVar('VT2', int, float, int | float)
KT2 = TypeVar('KT2', int, float, int | float)


@cmp_generator
class FunctionSequence(Generic[VT, KT]):
    def __resolve_item(self, kwarg: tuple[str, VT]) -> tuple[int, VT] | None:
        name, value = kwarg
        name = name.lower()

        if name.startswith(self.__name_of_elements) and (x := name.replace(self.__name_of_elements, '')).isdigit():
            if int(x) <= 0:
                raise Exception("'n' must be bigger that 0!")
            return int(x), value
        return None

    def __process_float(self, x: float):
        return int(x) if x.is_integer() else x

    def __init_subclass__(cls, name_of_elements: str, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__name_of_elements = name_of_elements

    def __init__(self, f: Callable[[int, KT, VT, int], VT], k_func: Callable[[VT, VT, int, int], KT], k: KT = None, **kwargs: VT):
        self.ref_func = f
        self.__k_func = k_func
        self.f = lambda n: self.ref_func(n, self.k, self.first, 1)

        el = [x for i in kwargs.items() if (x := self.__resolve_item(i))]

        if k:
            self.k = self.__process_float(k)
            if len(el) >= 1:
                i1, v1 = el[0]
                self.first = self.__process_float(self.ref_func(1, self.k, v1, i1))
            return
        if len(el) >= 2:
            (i1, v1), (i2, v2) = el[0], el[1]
            self.k = self.__process_float(self.__k_func(v1, v2, i1, i2))
            self.first = self.__process_float(self.ref_func(1, self.k, v1, i1))
            return
        raise Exception("__init__ can't get k")

    @overload
    def __call__(self, n: int) -> VT:
        ...

    @overload
    def __call__(self, start: int, end: int) -> list[VT]:
        ...

    def __call__(self, start: int, end: int | None = None):
        start1 = start
        if not end:
            end = start

        r = []

        for i in range(start1, end + 1):
            r.append(self.__process_float(self.f(i)))

        return r if len(r) > 1 else r[0]

    def __getitem__(self, n: int | slice):
        if isinstance(n, slice):
            start, end = x if (x := n.start) else 1, n.stop
            return self(start, end)
        return self(n)

    def __eq__(self, other: FunctionSequence[[VT2, KT2]]) -> bool:
        return self.k == other.k and self[1] == other[1]

    def __cmp__(self, other: FunctionSequence[VT2, KT2]) -> int:
        return self.k - other.k

    def __check_for_list(self, l_or_v: list | Any):
        if isinstance(l_or_v, list):
            return l_or_v
        return [l_or_v]

    @overload
    def s(self, n: int) -> VT:
        """
        Get sum of elements from `1` to `n`
        """
        ...

    @overload
    def s(self, start: int, end: int) -> VT:
        """
        Get sum of elements from `start` to `end`
        """
        ...

    def s(self, start: int, end: int | None = None) -> VT:
        """
        Get sum of elements
        """
        if end is None:
            start, end = 1, start
        return sum(self.__check_for_list(self(start, end)))

    @overload
    def p(self, n: int) -> VT:
        """
        Get product of elements from `1` to `n`
        """
        ...

    @overload
    def p(self, start: int, end: int) -> VT:
        """
        Get product of elements from `start` to `end`
        """
        ...

    def p(self, start: int, end: int | None = None) -> VT:
        """
        Get product of elements
        """
        if end is None:
            start, end = 1, start
        return mul(self.__check_for_list(self(start, end)))


class ArithmeticProgression(FunctionSequence[VT, KT], name_of_elements='a'):
    @property
    def d(self) -> KT:
        return self.k

    def __init__(self, *, d: KT = None, **kwargs):
        def f(n, k, am, m):
            return am + k * (n - m)
        def k_func(a_m: VT, a_n: VT, m: int, n: int) -> KT:
            return (a_n - a_m) / (n - m)
        super().__init__(f, k_func, d, **kwargs)

class GeometricProgression(FunctionSequence[VT, KT], name_of_elements='b'):
    @property
    def q(self) -> KT:
        return self.k

    def __init__(self, *, q: KT = None, **kwargs):
        def f(n, k, am, m):
            return am * (k**(n-m))
        def k_func(a_m: VT, a_n: VT, m: int, n: int) -> KT:
            return (a_n / a_m) ** (1 / (n - m))
        super().__init__(f, k_func, q, **kwargs)
