__all__ = (
    'math_generator',
    'i_generator',
    'r_generator',
    'generate_all_math_operations_magic_methods',
)

from typing import TypeVar, Callable, Any

from ufpy.typ.type_alias import MathOperations

T = TypeVar('T', bound=type)
OT = TypeVar('OT')
MRT = TypeVar('MRT')


def math_generator(t: type[T]) -> type[T]:
    """
    Generates math operation's magic methods for class with `__math__(self, other, math_operation)` method.
    """
    if '__math__' in t.__dict__:
        math: Callable[[Any, OT, MathOperations], MRT] = t.__math__

        if '__add__' not in t.__dict__:
            def add(self, other: OT) -> MRT:
                return math(self, other, '+')

            t.__add__ = add  # +
        if '__sub__' not in t.__dict__:
            def sub(self, other: OT) -> MRT:
                return math(self, other, '-')

            t.__sub__ = sub  # -
        if '__mul__' not in t.__dict__:
            def mul(self, other: OT) -> MRT:
                return math(self, other, '*')

            t.__mul__ = mul  # *
        if '__floordiv__' not in t.__dict__:
            def floordiv(self, other: OT) -> MRT:
                return math(self, other, '//')

            t.__floordiv__ = floordiv  # //
        if '__truediv__' not in t.__dict__:
            def truediv(self, other: OT) -> MRT:
                return math(self, other, '/')

            t.__truediv__ = truediv  # /
        if '__mod__' not in t.__dict__:
            def mod(self, other: OT) -> MRT:
                return math(self, other, '%')

            t.__mod__ = mod  # %
        if '__pow__' not in t.__dict__:
            def _pow(self, other: OT) -> MRT:
                return math(self, other, '**')

            t.__pow__ = _pow  # **
        if '__lshift__' not in t.__dict__:
            def lshift(self, other: OT) -> MRT:
                return math(self, other, '<<')

            t.__lshift__ = lshift  # <<
        if '__rshift__' not in t.__dict__:
            def rshift(self, other: OT) -> MRT:
                return math(self, other, '>>')

            t.__rshift__ = rshift  # >>
        if '__and__' not in t.__dict__:
            def _and(self, other: OT) -> MRT:
                return math(self, other, '&')

            t.__and__ = _and  # &
        if '__or__' not in t.__dict__:
            def _or(self, other: OT) -> MRT:
                return math(self, other, '|')

            t.__or__ = _or  # |
        if '__xor__' not in t.__dict__:
            def xor(self, other: OT) -> MRT:
                return math(self, other, '^')

            t.__xor__ = xor  # ^

    return t


def i_generator(t: type[T]) -> type[T]:
    if '__add__' in t.__dict__ and '__iadd__' not in t.__dict__:
        t.__iadd__ = t.__add__
    if '__sub__' in t.__dict__ and '__isub__' not in t.__dict__:
        t.__isub__ = t.__sub__
    if '__mul__' in t.__dict__ and '__imul__' not in t.__dict__:
        t.__imul__ = t.__mul__
    if '__floordiv__' in t.__dict__ and '__ifloordiv__' not in t.__dict__:
        t.__ifloordiv__ = t.__floordiv__
    if '__div__' in t.__dict__ and '__idiv__' not in t.__dict__:
        t.__idiv__ = t.__div__
    if '__truediv__' in t.__dict__ and '__itruediv__' not in t.__dict__:
        t.__itruediv__ = t.__truediv__
    if '__mod__' in t.__dict__ and '__imod__' not in t.__dict__:
        t.__imod__ = t.__mod__
    if '__pow__' in t.__dict__ and '__ipow__' not in t.__dict__:
        t.__ipow__ = t.__pow__
    if '__lshift__' in t.__dict__ and '__ilshift__' not in t.__dict__:
        t.__ilshift__ = t.__lshift__
    if '__rshift__' in t.__dict__ and '__irshift__' not in t.__dict__:
        t.__irshift__ = t.__rshift__
    if '__and__' in t.__dict__ and '__iand__' not in t.__dict__:
        t.__iand__ = t.__and__
    if '__or__' in t.__dict__ and '__ior__' not in t.__dict__:
        t.__ior__ = t.__or__
    if '__xor__' in t.__dict__ and '__ixor__' not in t.__dict__:
        t.__ixor__ = t.__xor__
    
    return t


def r_generator(t: type[T]) -> type[T]:
    if '__add__' in t.__dict__ and '__radd__' not in t.__dict__:
        t.__radd__ = t.__add__
    if '__sub__' in t.__dict__ and '__rsub__' not in t.__dict__:
        t.__rsub__ = t.__sub__
    if '__mul__' in t.__dict__ and '__rmul__' not in t.__dict__:
        t.__rmul__ = t.__mul__
    if '__floordiv__' in t.__dict__ and '__rfloordiv__' not in t.__dict__:
        t.__rfloordiv__ = t.__floordiv__
    if '__div__' in t.__dict__ and '__rdiv__' not in t.__dict__:
        t.__rdiv__ = t.__div__
    if '__truediv__' in t.__dict__ and '__rtruediv__' not in t.__dict__:
        t.__rtruediv__ = t.__truediv__
    if '__mod__' in t.__dict__ and '__rmod__' not in t.__dict__:
        t.__rmod__ = t.__mod__
    if '__pow__' in t.__dict__ and '__rpow__' not in t.__dict__:
        t.__rpow__ = t.__pow__
    if '__lshift__' in t.__dict__ and '__rlshift__' not in t.__dict__:
        t.__rlshift__ = t.__lshift__
    if '__rshift__' in t.__dict__ and '__rrshift__' not in t.__dict__:
        t.__rrshift__ = t.__rshift__
    if '__and__' in t.__dict__ and '__rand__' not in t.__dict__:
        t.__rand__ = t.__and__
    if '__or__' in t.__dict__ and '__ror__' not in t.__dict__:
        t.__ror__ = t.__or__
    if '__xor__' in t.__dict__ and '__rxor__' not in t.__dict__:
        t.__rxor__ = t.__xor__

    return t


def generate_all_math_operations_magic_methods(t: type[T]) -> type[T]:
    t = math_generator(t)  # Generate math operations
    t = i_generator(t)  # Generate i methods
    t = r_generator(t)  # Generate r methods
    return t
