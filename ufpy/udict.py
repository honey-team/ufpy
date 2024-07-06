from __future__ import annotations

from typing import Generic, Iterator, overload, TypeVar, Callable

from ufpy.cmp import cmp_generator
from ufpy.math_op import i_generator, r_generator
from ufpy.typ import AnyDict, AnyCollection
from ufpy.utils import set_items_for_several_keys, get_items_for_several_keys, del_items_for_several_keys

__all__ = (
    'UDict',
)

KT = TypeVar('KT')
VT = TypeVar('VT')
CDV = TypeVar('CDV')
DV = TypeVar('DV')

class _ClassDefault:
    ...

@cmp_generator
@i_generator
@r_generator
class UDict(Generic[KT, VT, CDV]):
    """
    Class for simplifying working with dicts in Python.
    
    Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict
    """
    @overload
    def __init__(self, dictionary: AnyDict[KT, VT]): ...
    @overload
    def __init__(self, dictionary: AnyDict[KT, VT], *, default: CDV): ...
    @overload
    def __init__(self, **kwargs: VT): ...
    @overload
    def __init__(self, *, default: CDV, **kwargs: VT): ...

    def __init__(self, dictionary: AnyDict[KT, VT] = None, *, default: CDV = None, **kwargs: VT):
        if isinstance(dictionary, UDict):
            dictionary = dictionary.dictionary
        self.__dict = dictionary or kwargs
        self.__default = default
    
    # dictionary
    @property
    def dictionary(self) -> dict[KT, VT]:
        """
        UDict's dictionary. A regular Python Dictionary.
        
        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#property-settable-dictionary-dictkt-vt
        """
        return self.__dict
    
    @dictionary.setter
    def dictionary(self, value: AnyDict[KT, VT]):
        if isinstance(value, UDict):
            value = value.dictionary
        self.__dict = value

    # keys
    @property
    def keys(self) -> list[KT]:
        """
        All dict's keys

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#property-settable-keys-listkt
        """
        return list(self.__dict.keys())

    @keys.setter
    def keys(self, value: AnyCollection[KT]):
        self.__dict = dict(list(zip(value, self.values)))

    # values
    @property
    def values(self) -> list[VT]:
        """
        All dict's values

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#property-settable-values-listvt
        """
        return list(self.__dict.values())

    @values.setter
    def values(self, value: AnyCollection[VT]):
        self.__dict = dict(list(zip(self.keys, value)))

    # items
    @property
    def items(self) -> list[tuple[KT, VT]]:
        """
        All dict's items

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#property-settable-items-listtuplekt-vt
        """
        return list(zip(self.keys, self.values))

    @items.setter
    def items(self, value: AnyCollection[tuple[KT, VT] | list[KT | VT]]):
        self.__dict = dict(value)
    
    # default
    @property
    def default(self) -> CDV:
        """
        The value that will be returned when .get() function or the [] operator are called if the entered key is not in the UDict

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#property-settable-default-cdv
        """
        return self.__default
    
    @default.setter
    def default(self, value: CDV):
        self.__default = value

    # call
    def __call__(self, func: Callable[[KT, VT], VT]) -> UDict[KT, VT, CDV]:
        """
        Generate new UDict with function

        Args:
            func: First argument of function is key, second is value. Returns new value

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__call__func-callablekt-vt-vt-udictkt-vt-cdv
        """
        new_dict = self.__dict
        for k, v in self:
            new_dict[k] = func(k, v)
        return UDict(new_dict, default=self.__default)

    # reverse integers
    def __neg__(self) -> UDict[KT, VT, CDV]:
        return self(lambda k, v: -v)
    
    # reverse
    def reverse(self) -> UDict[KT, VT, CDV]:
        """
        Reverses UDict and returns it.

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#reverse-udictkt-vt-cdv
        """
        self.__dict = self.reversed().__dict
        return self

    def reversed(self) -> UDict[KT, VT, CDV]:
        """
        Returns reversed UDict, but doesn't change it

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#reversed-udictkt-vt-cdv
        """
        keys, values = list(self.__dict.keys())[::-1], list(self.__dict.values())[::-1]
        return UDict(dict(list(zip(keys, values))))

    def __invert__(self) -> UDict[KT, VT, CDV]:
        return self.reversed()

    def __reversed__(self) -> UDict[KT, VT, CDV]:
        return self.reversed()

    # sort
    def sort(self) -> UDict[KT, VT, CDV]:
        """
        Sorts UDict and returns it

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#sort-udictkt-vt-cdv
        """
        self.__dict = self.sorted().__dict
        return self

    def sorted(self) -> UDict[KT, VT, CDV]:
        """
        Returns sorted UDict, but doesn't change it

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#sorted-udictkt-vt-cdv
        """
        keys = sorted(list(self.__dict.keys()))
        values = get_items_for_several_keys(self.__dict, keys)
        return UDict(dict(list(zip(keys, values))))

    # get/set/del items
    def __get_keys_from_slice_or_int(self, key: KT | int | slice) -> list[KT]:
        if isinstance(key, int) and key not in self.__dict:
            if key == 0:
                raise IndexError("You can't use 0 as index in UDict. Use 1 index instead.")
            return [list(self.__dict.keys())[key - 1]]
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self) + 1)
            if start == 0:
                start += 1
            if stop == len(self) + 1:
                stop -= 1
            indexes = list(range(start, stop + 1, step))
            return [list(self.__dict.keys())[i - 1] for i in indexes]
        return [key]
    
    def __getitem__(self, key: KT | int | slice) -> UDict[KT, VT, DV] | VT:
        keys = self.__get_keys_from_slice_or_int(key)

        l = get_items_for_several_keys(self.__dict, keys, self.__default)
        return l if len(l) > 1 else l[0]

    def __setitem__(self, key: KT | int | slice, value: VT | list[VT]) -> None:
        keys = self.__get_keys_from_slice_or_int(key)

        # Ensure 'values' is always a list for consistent processing
        values = value if isinstance(value, (list, tuple)) else [value]

        if len(keys) > len(values):
            values.extend([values[-1] for _ in range(len(keys) - len(values) + 1)])

        self.__dict = set_items_for_several_keys(self.__dict, keys, values)

    def __delitem__(self, key: KT | int | slice) -> None:
        keys = self.__get_keys_from_slice_or_int(key)

        self.__dict = del_items_for_several_keys(self.__dict, keys)

    # get
    @overload
    def get(self, *, key: KT) -> VT | CDV: ...
    @overload
    def get(self, *, key: KT, default: DV) -> VT | DV: ...
    @overload
    def get(self, *, index: int) -> VT | CDV: ...
    @overload
    def get(self, *, index: int, default: DV) -> VT | DV: ...
    @overload
    def get(self, *, value: VT) -> KT | CDV: ...
    @overload
    def get(self, *, value: VT, default: DV) -> KT | DV: ...

    def get(
            self, *, key: KT = None, index: int = None, value: VT = None,
            default: DV | CDV = _ClassDefault
    ) -> KT | VT | CDV | DV:
        """
        Get a value with key or it's index.

        If value is defined, returns key

        Parameters:
        key: Key of value in dict (optional)
        index: Index of value in dict (optional)
        value: Value in dict (optional)
        default: Default value (if none -> UDict.default) (optional)

        Raises:
        ValueError: You defined 0 or 2 or 3 params (from `key`, `index` and `value`)
        IndexError: index is bigger that length of dict

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#get
        """
        if key and index and value:
            raise ValueError(
                'You defined both key, index and value params. Please cancel the definition one of this params.'
            )
        if not key and not index and not value:
            raise ValueError(
                "You don't defined neither key, not index, not value params." +
                " Please cancel the definition one of this params."
            )
        if key and value:
            raise ValueError('You defined both key and value params. Please cancel the definition one of this params.')
        if key and index:
            raise ValueError('You defined both key and index params. Please cancel the definition one of this params.')
        if index and value:
            raise ValueError(
                'You defined both index and value params. Please cancel the definition one of this params.'
            )

        if index and index > len(self):
            raise IndexError('Index is bigger that length of UDict.')

        if default == _ClassDefault:
            default = self.__default

        if value:
            if value not in self.values:
                return default
            i = self.values.index(value)
            return self.keys[i]
        return self.__dict.get(self.keys[index-1], default) if index else self.__dict.get(key, default)

    # Len, iterator and reversed version
    def __len__(self) -> int:
        """
        Implements `len(self)`

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__len__-int
        """
        return len(self.__dict)
    
    def __iter__(self) -> Iterator[tuple[KT, VT]]:
        """
        Implements `iter(self)`

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__iter__-iteratortuplekt-vt
        """
        return iter(self.__dict.items())
    
    # Booleans
    def is_empty(self) -> bool:
        """
        Returns `True` if `len(self)` equals `0`

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#is_empty-bool
        """
        return len(self) == 0

    def __bool__(self) -> bool:
        """
        Returns `False` if `len(self)` equals `0`

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__bool__-bool
        """
        return not self.is_empty()

    def __contains__(self, item: tuple[KT, VT] | list[KT | VT] | KT) -> bool:
        """
        Returns `True` if `item` is in `UDict`

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__contains__item-tuplekt-vt-listkt-vt-kt-bool
        """
        if isinstance(item, (list, tuple)):
            k, v = item
            return k in self.__dict and self.__dict.get(k, self.__default) == v
        return item in self.__dict
    
    # Transform to other types
    def __repr__(self) -> str:
        """
        Transforms `UDict` to `str`

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__repr__-str
        """
        return f'u{self.__dict}'

    def __hash__(self) -> int:
        """
        Returns UDict's hash

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__hash__-int
        """
        return hash(self.__repr__())
    
    # Comparing
    def __cmp__(self, other: dict[KT, VT] | UDict[KT, VT, CDV]) -> int:
        """
        Returns `len(self) - len(other)` (this method is used by `@cmp_generator`)

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__cmp__other-dictkt-vt-udictkt-vt-cdv-int
        """
        return len(self) - len(other)
    
    def __eq__(self, other: dict[KT, VT] | UDict[KT, VT, CDV]) -> bool:
        """
        Returns True if UDict.dictionary is equal to other UDict.dictionary / UDict.dictionary is equal to dict

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__eq__other-dictkt-vt-udictkt-vt-cdv-bool
        """
        if isinstance(other, UDict):
            other = other.dictionary
        return self.__dict == other
    
    # Math operations
    def __add__(self, other: dict[KT, VT] | UDict[KT, VT, CDV]) -> UDict[KT, VT, CDV]:
        """
        Combines 2 UDict / 1 UDict and 1 Dictionary

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__add__other-dictkt-vt-udictkt-vt-cdv-udictkt-vt-cdv
        """
        new_dict = self.__dict.copy()
        
        if isinstance(other, UDict):
            other: dict[KT, VT] = other.dictionary
        
        for k, v in other.items():
            new_dict[k] = v
        return UDict(new_dict)
    
    def __sub__(self, other: dict[KT, VT] | UDict[KT, VT, CDV]) -> UDict[KT, VT, CDV]:
        """
        Subtracts from UDict another UDict / from UDict a regular dict

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__sub__other-dictkt-vt-udictkt-vt-cdv-udictkt-vt-cdv
        """
        new_dict = self.__dict.copy()
        if isinstance(other, UDict):
            other: dict[KT, VT] = other.dictionary
        
        for k, v in other.items():
            if new_dict.get(k) == v:
                del new_dict[k]
        return UDict(new_dict)
    
    def __mul__(
            self, other: dict[KT, float | int] | UDict[KT, float | int, DV] | float | int
    ) -> UDict[KT, VT, CDV]:
        """
        Multiplies each value by another value with the same key or all values by integer or float number

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__mul__other-dictkt-float-int-udictkt-float-int-dv-float-int-udictkt-supportsmul-cdv
        """
        new_dict = self.__dict.copy()
        
        if isinstance(other, UDict):
            other: dict[KT, VT] = other.dictionary
        if isinstance(other, (int, float)):
            other = dict([(k, other) for k in new_dict.keys()])
        
        for k, v in other.items():
            new_dict[k] *= v
        
        return UDict(new_dict)

    def __truediv__(
            self, other: dict[KT, float | int] | UDict[KT, float | int, DV] | float | int
    ) -> UDict[KT, VT, CDV]:
        """
        Divides each value by another value with the same key or all values by integer or float number

        Online docs: https://honey-team.github.io/ufpy-website/main/useful_classes/udict/#__truediv__other-dictkt-float-int-udictkt-float-int-dv-float-int-udictkt-supportstruediv-cdv
        """
        new_dict = self.__dict.copy()
        
        if isinstance(other, UDict):
            other: dict[KT, VT] = other.dictionary
        if isinstance(other, (int, float)):
            other = dict([(k, other) for k in new_dict.keys()])
        
        for k, v in other.items():
            new_dict[k] /= v
        
        return UDict(new_dict)
