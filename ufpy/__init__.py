"""
Library with some useful features like classes, functions and variables.

Online docs: https://honey-team.ru/ufpy-website
"""

from ufpy.cmp import *
from ufpy.math_op import *
from ufpy.udict import *
from ufpy.utils import *
from ufpy.typ import *
from ufpy.ustl import *
from ufpy.path import *
from ufpy.github import *

# Deprecated
def __deprecated(deprecated_name: str, x, start_version: str, end_version: str):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    # pylint: disable=import-outside-toplevel
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

Stack = __deprecated("Stack", Stack, '0.3', '0.5')
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
