# Deprecated
def __deprecated(deprecated_name: str, x, start_version: str, end_version: str):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    from functools import wraps
    from warnings import warn, simplefilter

    @wraps(x)
    def new_func(*args, **kwargs):
        simplefilter('always', DeprecationWarning)  # turn off filter
        warn(f"{deprecated_name} is deprecated in {start_version} and will be deleted in {end_version}. "
             f"Use {x.__name__} instead.",
             category=DeprecationWarning,
             stacklevel=2)
        simplefilter('default', DeprecationWarning)  # reset filter
        return x(*args, **kwargs)
    return new_func


__version__ = '0.2.1.1'
from ufpy.cmp import *
from ufpy.math_op import *
from ufpy.udict import *
from ufpy.utils import *

# Typing package
__typ_version__ = '0.2'
from ufpy.typ import *

# Ustl package
__ustl_version__ = '0.1'
from ufpy.ustl import *
UStack = __deprecated("UStack", Stack, '0.2', '0.5')

# Path package
__path_version__ = '0.2'
from ufpy.path import *

# GitHub package
__github_version__ = '0.1'
from ufpy.github import *

# Algebra package
__algebra_version__ = '0.1'
from ufpy.algebra import *
