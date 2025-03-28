__all__ = (
    'Fibonacci',
)

from typing import overload, Any

from ufpy.utils import mul


class Fibonacci:
    # 1, 1, 2, 3, 5, 8, ...
    def __init__(self):
        self.__n = 1

    def reset(self):
        self.__n = 1

    @overload
    def __call__(self, n: int) -> int: ...
    @overload
    def __call__(self, start: int, end: int) -> list[int]: ...
    def __call__(self, start_or_end: int, end: int = None):
        # Format input parameters
        if end is None:
            end = start_or_end
        start = start_or_end

        # Generate fibonacci sequence from 1st to `end`th item
        r = []

        for i in range(end):
            if i <= 1:
                r.append(1)
            else:
                r.append(r[i - 1] + r[i - 2])

        # Return result
        return r[-1] if start == end else r[start - 1:]

    def __getitem__(self, n: int | slice):
        if isinstance(n, slice):
            start, end = x if (x := n.start) else 1, n.stop
            return self(start, end)
        return self(n)

    def __next__(self):
        item = self(self.__n)
        self.__n += 1
        return item

    def __iter__(self):
        return self

    def __check_for_list(self, l_or_v: list | Any):
        return l_or_v if isinstance(l_or_v, list) else [l_or_v]

    @overload
    def s(self, n: int) -> int: ...
    @overload
    def s(self, start: int, end: int) -> int: ...
    def s(self, start_or_n: int, end: int = None) -> int:
        if end:
            start = start_or_n
        else:
            start, end = 1, start_or_n
        return sum(self.__check_for_list(self(start, end)))

    @overload
    def p(self, n: int) -> int: ...
    @overload
    def p(self, start: int, end: int) -> int: ...
    def p(self, start_or_n: int, end: int = None) -> int:
        if end:
            start = start_or_n
        else:
            start, end = 1, start_or_n
        return mul(self.__check_for_list(self(start, end)))
