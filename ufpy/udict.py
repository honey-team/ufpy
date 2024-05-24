from typing import Generic, Iterator, overload, TypeVar

from .cmp import cmp_generator
from .i import i_generator
from .utils import set_items_for_several_keys, get_items_for_several_keys, del_items_for_several_keys

__all__ = (
    'UDict',
)

KT = TypeVar('KT')
VT = TypeVar('VT')

@cmp_generator
@i_generator
class UDict(Generic[KT, VT]):
    @overload
    def __init__(self, dictionary: dict[KT, VT]): ...
    @overload
    def __init__(self, dictionary: dict[KT, VT], *, default: VT): ...
    @overload
    def __init__(self, **kwargs: VT): ...
    @overload
    def __init__(self, *, default: VT, **kwargs: VT): ...
    def __init__(self, dictionary = None, *, default = None, **kwargs):
        self.__dict = dictionary if dictionary is not None else kwargs
        self.__default = default
    
    # dictionary
    @property
    def dictionary(self) -> dict[KT, VT]:
        return self.__dict
    
    @dictionary.setter
    def dictionary(self, value: 'dict[KT, VT] | UDict'):
        if isinstance(value, UDict):
            value = value.dictionary
        self.__dict = value
    
    # default
    @property
    def default(self) -> VT:
        return self.__default
    
    @default.setter
    def default(self, value: VT):
        self.__default = value
    
    # reverse
    def reverse(self) -> 'UDict[KT, VT]':
        self.__dict = self.reversed().__dict
        return self

    def reversed(self) -> 'UDict[KT, VT]':
        keys, values = list(self.__dict.keys())[::-1], list(self.__dict.values())[::-1]
        return UDict(dict(list(zip(keys, values))))
    
    def __neg__(self) -> 'UDict[KT, VT]':
        return self.reversed()

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
    
    def __getitem__(self, key: KT | int | slice) -> 'UDict[KT, VT] | VT':
        keys = self.__get_keys_from_slice_or_int(key)

        l = get_items_for_several_keys(self.__dict, keys, self.__default)
        return l if len(l) > 1 else l[0]

    def __setitem__(self, key: KT | int | slice, value: VT | list[VT]) -> None:
        keys = self.__get_keys_from_slice_or_int(key)
        values = [value] if not isinstance(value, (list, tuple)) else value

        if len(keys) > len(values):
            values.extend([values[-1] for _ in range(len(keys) - len(values) + 1)])

        self.__dict = set_items_for_several_keys(self.__dict, keys, values)

    def __delitem__(self, key: KT | int | slice):
        keys = self.__get_keys_from_slice_or_int(key)

        self.__dict = del_items_for_several_keys(self.__dict, keys)

    # get/set/del attrs
    def __getattr__(self, name: str):
        return self.__dict.get(name, self.__default)

    # TODO: make __getattr__()
    # def __setattr__(self, name: str, value: VT): ...

    # TODO: make __delattr__()
    # def __delattr__(self, name: str): ...

    # Len, iterator and reversed version
    def __len__(self) -> int:
        return len(self.__dict.keys())
    
    def __iter__(self) -> Iterator[tuple[KT, VT]]:
        res = []
        
        for k, v in self.__dict.items():
            res.append((k, v))
        
        return iter(res)

    def __reversed__(self) -> 'UDict[KT, VT]':
        return self.reversed()
    
    # Booleans
    def __nonzero__(self) -> bool:
        return len(self) > 0

    # TODO: make __contains__()
    def __contains__(self, item: tuple[KT, VT] | list[KT | VT] | KT) -> bool:
        if isinstance(item, (list, tuple)):
            k, v = item
            return k in self.__dict and self.__dict.get(k, self.__default) == v
        return item in self.__dict
    
    # Transform to other types
    def __repr__(self) -> str:
        return f'''u{self.__dict}'''
    
    # Comparing
    def __cmp__(self, other: 'dict[KT, VT] | UDict') -> int:
        return len(self) - len(other)
    
    def __eq__(self, other: 'dict[KT, VT] | UDict') -> bool:
        if isinstance(other, UDict):
            other = other.dictionary
        return self.__dict == other
    
    # Math operations
    def __add__(self, other: 'dict[KT, VT] | UDict') -> 'UDict':
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other = other.dictionary
        
        for k, v in other.items():
            new_dict[k] = v
        return UDict(new_dict)
    
    def __sub__(self, other: 'dict[KT, VT] | UDict') -> 'UDict':
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other = other.dictionary
        
        for k, v in other.items():
            if new_dict.get(k) == v:
                del new_dict[k]
        return UDict(new_dict)
    
    def __mul__(self, other: 'dict[KT, float | int] | UDict[KT, float | int] | float | int') -> 'UDict':
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other = other.dictionary
        if isinstance(other, (int, float)):
            other = dict([(k, other) for k in new_dict.keys()])
        
        for k, v in other.items():
            new_dict[k] *= v
        
        return UDict(new_dict)

    def __truediv__(self, other: 'dict[KT, float | int] | UDict[KT, float | int] | float | int') -> 'UDict':
        new_dict = self.__dict
        
        if isinstance(other, UDict):
            other = other.dictionary
        if isinstance(other, (int, float)):
            other = dict([(k, other) for k in new_dict.keys()])
        
        for k, v in other.items():
            new_dict[k] /= v
        
        return UDict(new_dict)
