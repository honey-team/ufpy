__all__ = (
    'cmp_generator',
)

def cmp_generator(t: type):
    '''
    Decorator for auto generate compare magic methods (`__eq__()`, `__ne__()`, `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`).
    You should add `__cmp__()` method in your class. If your object more that other, `__cmp__()` should return positive number.
    If less that other, `__cmp__()` should return negative number. If equals, `__cmp__()` should return zero.
    
    `Note:`
    If you defined one of compare methods, they won't redefine.

    Example:
    ```py
    @cmp_generator
    class A:
        def __init__(self, num: int):
            self.num = num
        def __cmp__(self, other: int) -> int:
            return self.num - self.other
    
    a = A(2)
    print(a > 1) # True
    print(a < 2) # False
    print(a >= 3) # False
    print(a <= 4) # True
    ```
    
    Online docs: soon!
    '''
    
    if not '__eq__' in t.__dict__:
        t.__eq__ = lambda self, x: t.__cmp__(self, x) == 0
        t.__ne__ = lambda self, x: not t.__eq__(self, x)

    if not '__lt__' in t.__dict__:
        t.__lt__ = lambda self, x: t.__cmp__(self, x) < 0
    if not '__le__' in t.__dict__:
        t.__le__ = lambda self, x: t.__cmp__(self, x) <= 0

    if not '__gt__' in t.__dict__:
        t.__gt__ = lambda self, x: t.__cmp__(self, x) > 0
    if not '__ge__' in t.__dict__:
        t.__ge__ = lambda self, x: t.__cmp__(self, x) >= 0
    
    return t
