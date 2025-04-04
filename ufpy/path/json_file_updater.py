"""
Module with `JsonFileUpdater` class. This class simplify working with `json` files. You can create `JsonFileUpdater`
object and work how with python dictionary.

```py
with JsonFileUpdater('test.json') as j:
    print(j['hello'])
    j['hi'] = 'hello'
```
"""

from __future__ import annotations

__all__ = (
    'JsonFileUpdater',
)

import os.path
from io import BytesIO
from typing import Any, Generic, TypeVar, overload

from ujson import dumps, loads # pylint: disable=no-name-in-module

from ufpy import ReadWriteIO

VT = TypeVar('VT')


class JsonFileUpdater(Generic[VT]):
    """
    This class simplify working with `json` files. You can create `JsonFileUpdater`
    object and work how with python dictionary.

    ```py
    with JsonFileUpdater('test.json') as j:
        print(j['hello'])
        j['hi'] = 'hello'
    ```
    """
    @overload
    def __init__(self, path: str, indent: int = 4):
        ...

    @overload
    def __init__(self, stream: ReadWriteIO[str | bytes], indent: int = 4):
        ...

    @overload
    def __init__(self, stream: BytesIO, indent: int = 4):
        ...

    def __init__(self, stream_or_path: str | ReadWriteIO[str | bytes] | BytesIO, indent: int = 4) -> None:
        self.indent = indent
        self.__d: dict[str, VT] | None = None

        self.path = None
        self.stream = None
        if isinstance(stream_or_path, BytesIO) or (
                hasattr(stream_or_path, 'write') and hasattr(stream_or_path, 'read')):
            self.stream = stream_or_path
        else:
            self.path = stream_or_path

        if not (self.stream or os.path.exists(self.path)):
            print(f'Warning: No such file or directory: {self.path}. JsonFileUpdater will create it automaticly.')
            with open(self.path, encoding='utf-8', mode='x') as f:
                f.write('{}')

    def __load(self) -> dict[str, VT]:
        if self.path:
            with open(self.path, encoding='utf-8') as f:
                d = f.read()
        elif isinstance(self.stream, BytesIO):
            d = self.stream.getvalue().decode('utf-8')
        else:
            d = self.stream.read()  # type: ignore[union-attr]

        return loads(d) if d else {}

    def write(self, dictionary: dict[str, VT]) -> None:
        """
        Writes dictionary to file/stream/BytesIO

        Arguments:
            dictionary: Dictionary to write
        """
        d = dumps(
            dictionary,
            ensure_ascii=False,
            indent=self.indent
        )
        if self.stream:
            try:
                self.stream.write(d)
            except TypeError:  # bytes-like object is required
                self.stream.write(d.encode('utf-8'))
        else:
            with open(self.path, 'w', encoding='utf-8') as f:
                f.write(d)

    def __get_dict(self, path: str, __dict: dict[str, Any]) -> dict[str, Any]:
        if ' / ' not in path:
            return __dict
        keys = path.split(' / ')[:-1]

        current = __dict
        for key in keys:
            if not isinstance(current[key], dict):
                raise TypeError(f"Path component '{key}' exists but is not a dictionary")
            current = current[key]
        return current

    def __getitem__(self, key: str) -> VT:
        if self.__d is None:
            d = self.__load()
        else:
            d = self.__d

        keys = key.split(' / ')

        return self.__get_dict(key, d)[keys[-1]]

    def __setitem__(self, key: str, value: VT) -> None:
        keys = key.split(' / ')
        if self.__d is None:
            d = self.__load()
            r = d
            for i in keys:
                r.setdefault(i, {})
                r = r[i]
        else:
            r = self.__d
            for i in keys:
                r.setdefault(i, {})
                r = r[i]
            d = self.__d
        d2 = self.__get_dict(key, d)
        d2[keys[-1]] = value

    def __enter__(self) -> JsonFileUpdater:
        self.__d = self.__load()
        return self

    def __exit__(self, exception_type, exception_value, traceback) -> None:
        self.write(self.__d)
        self.__d = None

    def __repr__(self) -> str:
        if self.__d is None:
            return dumps(
                self.__load(),
                ensure_ascii=False,
                indent=self.indent
            )
        return repr(self.__d)
