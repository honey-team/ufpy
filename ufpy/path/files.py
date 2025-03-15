"""
Module which provides `UOpen` class for simplifying open files for read and write. UOpen automaticlly creates
directories when they weren't existing.
"""

import os
from typing import AnyStr, Literal


__all__ = (
    'UOpen',
)

from ufpy import is_iterable


class UOpen:
    """
    Class for simplifying working with files.

    Key features:
    - Auto create location of file (e.g. if path = '~/dev/test.txt' then program will create this path if not exists).
    - Work together with strings and bytes
    """
    def __init__(
            self, filepath: str,
            mode: Literal["r+", "+r", "rt+", "r+t", "+rt", "tr+", "t+r", "+tr", "w+", "+w", "wt+", "w+t", "+wt", "tw+",
            "t+w", "+tw", "a+", "+a", "at+", "a+t", "+at", "ta+", "t+a", "+ta", "x+", "+x", "xt+", "x+t", "+xt", "tx+",
            "t+x", "+tx", "w", "wt", "tw", "a", "at", "ta", "x", "xt", "tx", "r", "rt", "tr", "U", "rU", "Ur", "rtU",
            "rUt", "Urt", "trU", "tUr", "Utr"] = "r", encoding: str = 'utf-8'
    ):
        self.__path = filepath
        self.__mode = mode
        self.__encoding = encoding
        directory = '/'.join(self.__path.split('/')[:-1]) or '\\'.join(self.__path.split('\\')[:-1])
        if directory:
            os.makedirs(directory, exist_ok=True)
        self.__f = open(file=self.__path, mode=self.__mode, encoding=self.__encoding) # pylint: disable=(consider-using-with

    def write(self, data: AnyStr):
        """
        Write data to file
        """
        self.__f.write(data)

    def writelines(self, *lines: AnyStr | list[AnyStr]):
        """
        Write lines to file
        """
        nl = []
        for i in lines:
            nl += i if is_iterable(i) else [i]
        lines = nl

        lines = [i.decode(self.__encoding) if isinstance(i, bytes) else i for i in lines]

        self.__f.writelines(lines)


    def read(self, n: int = -1) -> AnyStr:
        """
        Read text from file
        """
        return self.__f.read(n)

    def readlines(self, hint: int = -1) -> list[AnyStr]:
        """
        Read lines from file
        """
        return self.__f.readlines(hint)

    def close(self) -> None:
        """
        Close file
        """
        if self.__f:
            self.__f.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
