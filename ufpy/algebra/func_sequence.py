__all__ = (
    'FunctionSequence',
)

from typing import Callable, TypeVar, Generic, Literal, overload, Any

from ufpy.utils import mul

VT = TypeVar('VT', int, float, int | float)
KT = TypeVar('KT', int, float, int | float)

class FunctionSequence(Generic[VT, KT]):
    def __resolve_item(self, kwarg: tuple[str, VT]) -> tuple[int, VT] | None:
        name, value = kwarg
        name = name.lower()

        if name.startswith(self.__name_of_elements) and (x := name.replace(self.__name_of_elements, '')).isdigit():
            if int(x) <= 0:
                raise Exception("'n' must be bigger that 0!")
            return int(x), value
        return None

    def __resolve_sum_and_composition(self, kwarg: tuple[str, VT]) -> tuple[Literal['s', 'p'], int, VT] | None:
        name, value = kwarg
        name = name.lower()

        if name.startswith('s') and (x := name.replace('s', '')).isdigit():
            return 's', int(x), value
        if name.startswith('p') and (y := name.replace('p', '')):
            return 'p', int(y), value
        return None

    def __process_float(self, x: float):
        return int(x) if x.is_integer() else x

    def k_func(self, a_m: VT, a_n: VT, m: int, n: int) -> KT:
        ...  # return k

    def __init_subclass__(cls, name_of_elements: str, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__name_of_elements = name_of_elements

    def __init__(self, f: Callable[[int, KT, VT, int], VT], k: KT = None, **kwargs: VT):
        self.ref_func = f
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
            self.k = self.__process_float(self.k_func(v1, v2, i1, i2))
            self.first = self.__process_float(self.ref_func(1, self.k, v1, i1))
            return
        raise Exception("__init__ can't get k")

    @overload
    def __call__(self, n: int) -> VT: ...
    @overload
    def __call__(self, start: int, end: int) -> list[VT]: ...
    def __call__(self, start_or_end: int, end: int = None):
        start = start_or_end
        if not end:
            end = start_or_end

        r = []

        for i in range(start, end+1):
            r.append(self.__process_float(self.f(i)))

        return r if len(r) > 1 else r[0]

    def __getitem__(self, n: int | slice):
        if isinstance(n, slice):
            start, end = x if (x := n.start) else 1, n.stop
            return self(start, end)
        return self(n)

    def __check_for_list(self, l_or_v: list | Any):
        if isinstance(l_or_v, list):
            return l_or_v
        return [l_or_v]

    @overload
    def s(self, n: int) -> VT: ...
    @overload
    def s(self, start: int, end: int) -> VT: ...
    def s(self, start_or_n: int, end: int = None) -> VT:
        if end:
            start = start_or_n
        else:
            start, end = 1, start_or_n
        return sum(self.__check_for_list(self(start, end)))

    @overload
    def p(self, n: int) -> VT: ...
    @overload
    def p(self, start: int, end: int) -> VT: ...
    def p(self, start_or_n: int, end: int = None) -> VT:
        if end:
            start = start_or_n
        else:
            start, end = 1, start_or_n
        return mul(self.__check_for_list(self(start, end)))
