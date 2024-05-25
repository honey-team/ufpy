from typing import Generic, Iterator, overload, TypeVar, Iterable, Callable

from .cmp import cmp_generator
from .math_op import i_generator, r_generator
from .utils import set_items_for_several_keys, get_items_for_several_keys, del_items_for_several_keys

__all__ = (
    'UDict',
)

KT = TypeVar('KT')
VT = TypeVar('VT')
DV = TypeVar('DV')

@cmp_generator
@i_generator
@r_generator
class UDict(Generic[KT, VT, DV]):
    @overload
    def __init__(self, dictionary: dict[KT, VT]): ...
    @overload
    def __init__(self, dictionary: dict[KT, VT], *, default: DV): ...
    @overload
    def __init__(self, **kwargs: VT): ...
    @overload
    def __init__(self, *, default: DV, **kwargs: VT): ...
    def __init__(self, dictionary = None, *, default = None, **kwargs):
        self.__dict = dictionary if dictionary is not None else kwargs
        self.__default = default
    
    # dictionary
    @property
    def dictionary(self) -> dict[KT, VT]:
        return self.__dict
    
    @dictionary.setter
    def dictionary(self, value: 'dict[KT, VT] | UDict[KT, VT]'):
        if isinstance(value, UDict):
            value = value.dictionary
        self.__dict = value

    # keys
    @property
    def keys(self) -> list[KT]:
        return list(self.__dict.keys())

    @keys.setter
    def keys(self, value: Iterable[KT]):
        values = list(self.__dict.values())
        self.__dict = dict(list(zip(value, values)))

    # values
    @property
    def values(self) -> list[VT]:
        return list(self.__dict.values())

    @values.setter
    def values(self, value: Iterable[VT]):
        keys = list(self.__dict.keys())
        self.__dict = dict(list(zip(keys, value)))

    # items
    @property
    def items(self) -> list[tuple[KT, VT]]:
        return list(zip(self.keys, self.values))
    
    # default
    @property
    def default(self) -> DV:
        return self.__default
    
    @default.setter
    def default(self, value: DV):
        self.__default = value

    # call
    def __call__(self, func: Callable[[KT, VT], VT]) -> 'UDict[KT, VT, DV]':
        new_dict = self.__dict
        for k, v in self:
            new_dict[k] = func(k, v)
        return UDict(new_dict, default=self.__default)
    
    # reverse
    def reverse(self) -> 'UDict[KT, VT, DV]':
        self.__dict = self.reversed().__dict
        return self

    def reversed(self) -> 'UDict[KT, VT, DV]':
        keys, values = list(self.__dict.keys())[::-1], list(self.__dict.values())[::-1]
        return UDict(dict(list(zip(keys, values))))
    
    def __neg__(self) -> 'UDict[KT, VT, DV]':
        return self.reversed()

    def __reversed__(self) -> 'UDict[KT, VT, DV]':
        return self.reversed()

    # sort
    def sort(self) -> 'UDict[KT, VT, DV]':
        self.__dict = self.sorted().__dict
        return self

    def sorted(self) -> 'UDict[KT, VT, DV]':
        keys = sorted(list(self.__dict.keys()))
        values = get_items_for_several_keys(self.__dict, keys)
        return UDict(dict(list(zip(keys, values))))

    # get/set/del items
    def __get_keys_from_slice_or_int(self, key: KT | int | slice) -> list[KT]:
        if isinstance(key, int) and key not in self.__dict:
            return [list(self.__dict.keys())[key - 1]]
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self) + 1)
            if start == 0: start += 1
            if stop == len(self) + 1: stop -= 1
            indexes = list(range(start, stop + 1, step))
            return [list(self.__dict.keys())[i - 1] for i in indexes]
        return [key]
    
    def __getitem__(self, key: KT | int | slice) -> 'UDict[KT, VT, DV] | VT':
        keys = self.__get_keys_from_slice_or_int(key)

        l = get_items_for_several_keys(self.__dict, keys, self.__default)
        return l if len(l) > 1 else l[0]

    def __setitem__(self, key: KT | int | slice, value: VT | list[VT]) -> None:
        keys = self.__get_keys_from_slice_or_int(key)
        values = [value] if not isinstance(value, (list, tuple)) else value

        if len(keys) > len(values):
            values.extend([values[-1] for _ in range(len(keys) - len(values) + 1)])

        self.__dict = set_items_for_several_keys(self.__dict, keys, values)

    def __delitem__(self, key: KT | int | slice) -> None:
        keys = self.__get_keys_from_slice_or_int(key)

        self.__dict = del_items_for_several_keys(self.__dict, keys)

    # Len, iterator and reversed version
    def __len__(self) -> int:
        return len(self.items)
    
    def __iter__(self) -> Iterator[tuple[KT, VT]]:
        return iter(self.items)
    
    # Booleans
    def __nonzero__(self) -> bool:
        return len(self) > 0

    def __contains__(self, item: tuple[KT, VT] | list[KT | VT] | KT) -> bool:
        if isinstance(item, (list, tuple)):
            k, v = item
            return k in self.__dict and self.__dict.get(k, self.__default) == v
        return item in self.__dict
    
    # Transform to other types
    def __str__(self) -> str:
        return str(self.__dict)

    def __repr__(self) -> str:
        return f'''u{self.__dict}'''

    def __hash__(self) -> int:
        return hash(self.__repr__())
    
    # Comparing
    def __cmp__(self, other: 'dict[KT, VT] | UDict[KT, VT, DV]') -> int:
        return len(self) - len(other)
    
    def __eq__(self, other: 'dict[KT, VT] | UDict[KT, VT, DV]') -> bool:
        if isinstance(other, UDict):
            other = other.dictionary
        return self.__dict == other
    
    # Math operations
    def __add__(self, other: 'dict[KT, VT] | UDict[KT, VT, DV]') -> 'UDict[KT, VT, DV]':
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other: dict[KT, VT] = other.dictionary
        
        for k, v in other.items():
            new_dict[k] = v
        return UDict(new_dict)
    
    def __sub__(self, other: 'dict[KT, VT] | UDict[KT, VT, DV]') -> 'UDict[KT, VT, DV]':
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other: dict[KT, VT] = other.dictionary
        
        for k, v in other.items():
            if new_dict.get(k) == v:
                del new_dict[k]
        return UDict(new_dict)
    
    def __mul__(self, other: 'dict[KT, float | int] | UDict[KT, float | int, DV] | float | int') -> 'UDict[KT, VT, DV]':
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other: dict[KT, VT] = other.dictionary
        if isinstance(other, (int, float)):
            other = dict([(k, other) for k in new_dict.keys()])
        
        for k, v in other.items():
            new_dict[k] *= v
        
        return UDict(new_dict)

    def __truediv__(
            self, other: 'dict[KT, float | int] | UDict[KT, float | int, DV] | float | int'
    ) -> 'UDict[KT, VT, DV]':
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other: dict[KT, VT] = other.dictionary
        if isinstance(other, (int, float)):
            other = dict([(k, other) for k in new_dict.keys()])
        
        for k, v in other.items():
            new_dict[k] /= v
        
        return UDict(new_dict)
