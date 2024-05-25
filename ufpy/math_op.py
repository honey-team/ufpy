__all__ = (
    'i_generator',
    'r_generator',
)

from typing import Type, TypeVar


T = TypeVar('T')

def i_generator(t: Type[T]) -> Type[T]:
    if '__add__' in t.__dict__:
        t.__iadd__ = t.__add__
    if '__sub__' in t.__dict__:
        t.__isub__ = t.__sub__
    if '__mul__' in t.__dict__:
        t.__imul__ = t.__mul__
    if '__floordiv__' in t.__dict__:
        t.__ifloordiv__ = t.__floordiv__
    if '__div__' in t.__dict__:
        t.__idiv__ = t.__div__
    if '__truediv__' in t.__dict__:
        t.__itruediv__ = t.__truediv__
    if '__mod__' in t.__dict__:
        t.__imod__ = t.__mod__
    if '__pow__' in t.__dict__:
        t.__ipow__ = t.__pow__
    if '__lshift__' in t.__dict__:
        t.__ilshift__ = t.__lshift__
    if '__rshift__' in t.__dict__:
        t.__irshift__ = t.__rshift__
    if '__and__' in t.__dict__:
        t.__iand__ = t.__and__
    if '__or__' in t.__dict__:
        t.__ior__ = t.__or__
    if '__xor__' in t.__dict__:
        t.__ixor__ = t.__xor__
    
    return t

def r_generator(t: Type[T]) -> Type[T]:
    if '__add__' in t.__dict__:
        t.__radd__ = t.__add__
    if '__sub__' in t.__dict__:
        t.__rsub__ = t.__sub__
    if '__mul__' in t.__dict__:
        t.__rmul__ = t.__mul__
    if '__floordiv__' in t.__dict__:
        t.__rfloordiv__ = t.__floordiv__
    if '__div__' in t.__dict__:
        t.__rdiv__ = t.__div__
    if '__truediv__' in t.__dict__:
        t.__rtruediv__ = t.__truediv__
    if '__mod__' in t.__dict__:
        t.__rmod__ = t.__mod__
    if '__pow__' in t.__dict__:
        t.__rpow__ = t.__pow__
    if '__lshift__' in t.__dict__:
        t.__rlshift__ = t.__lshift__
    if '__rshift__' in t.__dict__:
        t.__rrshift__ = t.__rshift__
    if '__and__' in t.__dict__:
        t.__rand__ = t.__and__
    if '__or__' in t.__dict__:
        t.__ror__ = t.__or__
    if '__xor__' in t.__dict__:
        t.__rxor__ = t.__xor__

    return t
