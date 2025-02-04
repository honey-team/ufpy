from __future__ import annotations

__all__ = (
    'JsonFileUpdater',
)

import os.path
from typing import Any, Generic, TypeVar
from ujson import dumps, loads

VT = TypeVar('VT')

class JsonFileUpdater(Generic[VT]):
    def __init__(self, json_file_path: str, indent: int = 4) -> None:
        self.path = json_file_path
        self.indent = indent
        self.__d: dict[str, VT] | None = None

        if not os.path.exists(self.path):
            print(f'Warning: No such file or directory: {self.path}. JsonFileUpdater will create it automaticly.')
            with open(self.path, encoding='utf-8', mode='x') as f:
                f.write('{}')
    
    def __load(self) -> dict[str, VT]:
        with open(self.path, encoding='utf-8') as f:
            r = loads(f.read())
        return r
    
    def __write(self, d: dict[str, VT]) -> None:
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(dumps(
                d,
                ensure_ascii=False,
                indent=self.indent
            ))

    def __get_dict(self, path: str, __dict: dict[str, Any]) -> dict[str, Any]:
        if not ' / ' in path:
            return __dict
        keys = path.split(' / ')[:-1]

        r = __dict
        for i in keys:
            r = r[i]
        return r

    def __getitem__(self, key: str) -> VT:
        if self.__d == None:
            d = self.__load()
        else:
            d = self.__d
        
        keys = key.split(' / ')
        
        return self.__get_dict(key, d)[keys[-1]]
    
    def __setitem__(self, key: str, value: VT) -> None:
        if self.__d == None:
            d = self.__load()
            
            keys = key.split(' / ')
            
            r = d
            for i in keys:
                r.setdefault(i, {})
                r = r[i]
            
            d2 = self.__get_dict(key, d)
            d2[keys[-1]] = value
            
            self.__write(d)
        else:
            keys = key.split(' / ')
            
            r = self.__d
            for i in keys:
                r.setdefault(i, {})
                r = r[i]
            
            d2 = self.__get_dict(key, self.__d)
            d2[keys[-1]] = value
    def __enter__(self) -> JsonFileUpdater:
        self.__d = self.__load()
        return self
    
    def __exit__(self, exception_type, exception_value, traceback) -> None:
        self.__write(self.__d)
        self.__d = None
    
    def __repr__(self) -> str:
        if self.__d == None:
            return dumps(
                self.__load(),
                ensure_ascii=False,
                indent=self.indent
            )
        return repr(self.__d)
