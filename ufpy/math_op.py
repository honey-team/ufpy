__all__ = (
    'i_generator',
    'r_generator',
)

from typing import Type, TypeVar


T = TypeVar('T')

def check(t: Type[T], s: str, astr: str):
    s2 = f'__{astr}{s.replace('__', '')}__'
    return s in t.__dict__ and s2 not in t.__dict__

def i_generator(t: Type[T]) -> Type[T]:
    def check_i(s: str):
        return check(t, s, 'i')

    if check_i('__add__'):
        t.__iadd__ = t.__add__
    if check_i('__sub__'):
        t.__isub__ = t.__sub__
    if check_i('__mul__'):
        t.__imul__ = t.__mul__
    if check_i('__floordiv__'):
        t.__ifloordiv__ = t.__floordiv__
    if check_i('__div__'):
        t.__idiv__ = t.__div__
    if check_i('__truediv__'):
        t.__itruediv__ = t.__truediv__
    if check_i('__mod__'):
        t.__imod__ = t.__mod__
    if check_i('__pow__'):
        t.__ipow__ = t.__pow__
    if check_i('__lshift__'):
        t.__ilshift__ = t.__lshift__
    if check_i('__rshift__'):
        t.__irshift__ = t.__rshift__
    if check_i('__and__'):
        t.__iand__ = t.__and__
    if check_i('__or__'):
        t.__ior__ = t.__or__
    if check_i('__xor__'):
        t.__ixor__ = t.__xor__
    
    return t

def r_generator(t: Type[T]) -> Type[T]:
    def check_r(s: str):
        return check(t, s, 'r')

    if check_r('__add__'):
        t.__radd__ = t.__add__
    if check_r('__sub__'):
        t.__rsub__ = t.__sub__
    if check_r('__mul__'):
        t.__rmul__ = t.__mul__
    if check_r('__floordiv__'):
        t.__rfloordiv__ = t.__floordiv__
    if check_r('__div__'):
        t.__rdiv__ = t.__div__
    if check_r('__truediv__'):
        t.__rtruediv__ = t.__truediv__
    if check_r('__mod__'):
        t.__rmod__ = t.__mod__
    if check_r('__pow__'):
        t.__rpow__ = t.__pow__
    if check_r('__lshift__'):
        t.__rlshift__ = t.__lshift__
    if check_r('__rshift__'):
        t.__rrshift__ = t.__rshift__
    if check_r('__and__'):
        t.__rand__ = t.__and__
    if check_r('__or__'):
        t.__ror__ = t.__or__
    if check_r('__xor__'):
        t.__rxor__ = t.__xor__

    return t
