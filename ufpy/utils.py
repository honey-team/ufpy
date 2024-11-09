__all__ = (
    'get_items_for_several_keys',
    'set_items_for_several_keys',
    'del_items_for_several_keys',
    'withrepr'
)

from ast import Call
from typing import Any, Callable, TypeVar
import functools

from ufpy.typ import SupportsGet, SupportsSetItem, SupportsDelItem, AnyCollection

KT = TypeVar('KT')
VT = TypeVar('VT')
DV = TypeVar('DV')


def get_items_for_several_keys(o: SupportsGet[KT, VT], keys: AnyCollection[KT], default: DV = None) -> list[VT | DV]:
    return [o.get(k, default) for k in keys]


def set_items_for_several_keys(
        o: SupportsSetItem[KT, VT], keys: AnyCollection[KT], values: AnyCollection[VT]
) -> SupportsSetItem[KT, VT]:
    res = o
    for i, k in enumerate(keys):
        res[k] = values[i]
    return res


def del_items_for_several_keys(o: SupportsDelItem[KT, VT], keys: AnyCollection[KT]) -> SupportsDelItem[KT, VT]:
    res = o
    for k in keys:
        del res[k]
    return res

# Useful decorators

class __reprwrapper:
    def __init__(self, repr, func):
        self._repr = repr
        self._func = func
        functools.update_wrapper(self, func)
    def __call__(self, *args, **kw):
        return self._func(*args, **kw)
    def __repr__(self):
        return self._repr(self._func)

T = TypeVar('T', bound=Callable)

def withrepr(f: Callable[[T], str]):
    def _wrap(func: T):
        return __reprwrapper(f, func)
    return _wrap
