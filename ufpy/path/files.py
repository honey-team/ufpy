import os
from typing import AnyStr, Iterable


__all__ = (
    'UOpen',
)

class UOpen:
    def __init__(
            self, filepath: str, mode: str = "r", encoding: str = 'utf-8'
    ):
        self.__path = filepath
        self.__mode = mode
        self.__encoding = encoding

    def __enter__(self):
        directory = '/'.join(self.__path.split('/')[:-1]) or '\\'.join(self.__path.split('\\')[:-1])

        os.makedirs(directory, exist_ok=True)

        self.__f = open(file=self.__path, mode=self.__mode, encoding=self.__encoding)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.__f.closed:
            self.__f.close()

    def __del__(self):
        if not self.__f.closed:
            self.__f.close()

    def write(self, data: AnyStr):
        self.__f.write(data)

    def writelines(self, lines: Iterable[AnyStr]):
        self.__f.writelines(lines)

    def read(self, n: int = -1) -> AnyStr:
        return self.__f.read(n)

    def readlines(self, hint: int = -1) -> list[AnyStr]:
        return self.__f.readlines(hint)
