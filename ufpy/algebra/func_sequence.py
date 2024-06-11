__all__ = (
    'FunctionSequence',
)

from typing import Callable, TypeVar, Generic, Literal, overload

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
    def __call__(self, n: int): ...
    @overload
    def __call__(self, start: int, end: int): ...
    def __call__(self, start_or_end: int, end: int = None) -> VT | list[VT]:
        start = start_or_end
        if not end:
            end = start_or_end

        r = []

        for i in range(start, end+1):
            r.append(self.__process_float(self.f(i)))

        return r if len(r) > 1 else r[0]

    def __getitem__(self, n: int | slice):
        if isinstance(n, slice):
            start, end = n.start, n.stop
            print(start, end)
            return self(start, end)
        return self(n)

    def s(self, n: int) -> VT:
        r = self.first

        for i in range(2, n+1):
            r += self(i)

        return self.__process_float(r)

    def p(self, n: int) -> VT:
        r = self.first

        for i in range(2, n + 1):
            r *= self(i)

        return self.__process_float(r)

