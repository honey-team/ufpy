__all__ = (
    'Geometric',
)

from typing import TypeVar

from ufpy.algebra.func_sequence import FunctionSequence

VT = TypeVar('VT', int, float, int | float)
QT = TypeVar('QT', int, float, int | float)

class Geometric(FunctionSequence[VT, QT], name_of_elements='b'):
    def k_func(self, a_m: VT, a_n: VT, m: int, n: int) -> QT:
        return (a_n / a_m) ** (1 / (n - m))

    @property
    def q(self) -> QT:
        return self.k

    def __init__(self, *, q: QT = None, **kwargs):
        def f(n, k, am, m):
            return am * (k**(n-m))

        super().__init__(f, q, **kwargs)
