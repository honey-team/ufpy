__all__ = (
    'i_generator',
    'r_generator',
)

from typing import Type, TypeVar


T = TypeVar('T')

def check(t: Type[T], s: str, astr: str):
    return f'__{s}__' in t.__dict__ and f'__{astr}{s}__' not in t.__dict__

def i_generator(t: Type[T]) -> Type[T]:
    def check_i(s: str):
        return check(t, s, 'i')

    if check_i('add'):
        t.__iadd__ = t.__add__
    if check_i('sub'):
        t.__isub__ = t.__sub__
    if check_i('mul'):
        t.__imul__ = t.__mul__
    if check_i('floordiv'):
        t.__ifloordiv__ = t.__floordiv__
    if check_i('div'):
        t.__idiv__ = t.__div__
    if check_i('truediv'):
        t.__itruediv__ = t.__truediv__
    if check_i('mod'):
        t.__imod__ = t.__mod__
    if check_i('pow'):
        t.__ipow__ = t.__pow__
    if check_i('lshift'):
        t.__ilshift__ = t.__lshift__
    if check_i('rshift'):
        t.__irshift__ = t.__rshift__
    if check_i('and'):
        t.__iand__ = t.__and__
    if check_i('or'):
        t.__ior__ = t.__or__
    if check_i('xor'):
        t.__ixor__ = t.__xor__
    
    return t

def r_generator(t: Type[T]) -> Type[T]:
    def check_r(s: str):
        return check(t, s, 'r')

    if check_r('add'):
        t.__radd__ = t.__add__
    if check_r('sub'):
        t.__rsub__ = t.__sub__
    if check_r('mul'):
        t.__rmul__ = t.__mul__
    if check_r('floordiv'):
        t.__rfloordiv__ = t.__floordiv__
    if check_r('div'):
        t.__rdiv__ = t.__div__
    if check_r('truediv'):
        t.__rtruediv__ = t.__truediv__
    if check_r('mod'):
        t.__rmod__ = t.__mod__
    if check_r('pow'):
        t.__rpow__ = t.__pow__
    if check_r('lshift'):
        t.__rlshift__ = t.__lshift__
    if check_r('rshift'):
        t.__rrshift__ = t.__rshift__
    if check_r('and'):
        t.__rand__ = t.__and__
    if check_r('or'):
        t.__ror__ = t.__or__
    if check_r('xor'):
        t.__rxor__ = t.__xor__

    return t
