__all__ = (
    'get_items_for_several_keys',
    'set_items_for_several_keys',
    'del_items_for_several_keys',
    'is_iterable',
)

from collections.abc import Iterable
from typing import TypeVar, Callable, Any

from ufpy.typ.protocols import SupportsGet, SupportsSetItem, SupportsDelItem, SupportsMathOperations
from ufpy.typ.type_alias import AnyCollection, MathOperations

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


def is_iterable(o: object) -> bool:
    return isinstance(o, Iterable)


def get_math_operation(o: SupportsMathOperations, math_op: MathOperations) -> Callable[[Any], Any]:
    match o:
        case '+':
            return o.__add__
        case '-':
            return o.__sub__
        case '*':
            return o.__mul__
        case '/':
            return o.__truediv__
        case '//':
            return o.__floordiv__
        case '%':
            return o.__mod__
        case '**':
            return o.__pow__
        case '<<':
            return o.__lshift__
        case '>>':
            return o.__rshift__
        case '&':
            return o.__and__
        case '|':
            return o.__or__
        case '^':
            return o.__xor__
