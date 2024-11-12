from __future__ import annotations

from ufpy.cmp import cmp_generator
from ufpy.typ.type_alias import NumberLiteral

__all__ = (
    'UInterval',
    'inf',
)

from typing import Generic, Literal, Optional, TypeVar


@cmp_generator
class Inf:
    def __init__(self, sign: Literal[-1, 0, 1]) -> None:
        self.sign = sign
    
    def __neg__(self) -> Inf:
        return Inf(-1)
    
    def __pos__(self) -> Inf:
        return Inf(+1)
    
    def __invert__(self) -> Inf:
        return Inf(+1 if self.sign == -1 else -1 if self.sign == 1 else 0)
    
    def __cmp__(self, other) -> int:
        if isinstance(other, Inf) and other.sign < self.sign:
            return 0
        return 1
    
    def __repr__(self) -> str:
        r = ''
        if self.sign == 1:
            r += '+'
        elif self.sign == -1:
            r += '-'
        
        return f'{r}∞'

inf = Inf(0)

IntervalNumber = NumberLiteral | list[NumberLiteral] | Inf

class UInterval:
    def __init__(self, start: IntervalNumber, end: IntervalNumber = +inf) -> None:
        self.__start = start[0] if isinstance(start, list) else start
        self.__end = end[0] if isinstance(end, list) else end
        self.inc = [int(isinstance(start, list)), int(isinstance(end, list))]
    
    @property
    def start(self) -> NumberLiteral | Inf:
        return self.__start
    
    @start.setter
    def start(self, value: IntervalNumber):
        self.__start = value[0] if isinstance(value, list) else value
        if isinstance(value, list):
            self.inc[0] = 1
        else:
            self.inc[0] = 0
    
    @property
    def end(self) -> NumberLiteral | Inf:
        return self.__end
    
    @end.setter
    def end(self, value: IntervalNumber):
        self.__end = value[0] if isinstance(value, list) else value
        if isinstance(value, list):
            self.inc[1] = 1
        else:
            self.inc[1] = 0
    
    def __repr__(self) -> str:
        fbracket = '[' if self.inc[0] else '('
        sbracket = ']' if self.inc[1] else ')'
        return f'u{fbracket}{self.__start}; {self.__end}{sbracket}'
    
    def in_interval(self, x: NumberLiteral | Inf) -> bool:
        b = True
        
        if self.inc[0]:
            b &= x >= self.__start
        else:
            b &= x > self.__start

        if self.inc[1]:
            b &= x <= self.__end
        else:
            b &= x < self.__end        
        
        return b
