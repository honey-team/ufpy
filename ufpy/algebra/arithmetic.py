__all__ = (
    'Arithmetic',
)

from typing import TypeVar

from ufpy.algebra.func_sequence import FunctionSequence

VT = TypeVar('VT', int, float, int | float)
DT = TypeVar('DT', int, float, int | float)

class Arithmetic(FunctionSequence[VT, DT], name_of_elements='a'):
    def k_func(self, a_m: VT, a_n: VT, m: int, n: int) -> VT:
        return (a_n - a_m) / (n - m)

    @property
    def d(self) -> DT:
        return self.k

    def __init__(self, d: VT = None, **kwargs):
        def f(n, k, am, m):
            return am + k * (n - m)

        super().__init__(f, d, **kwargs)
