__all__ = (
    'number_of_files_with_extensions',
)

import os

def number_of_files_with_extensions(path, extension) -> int:
    """
    Count number of files with specified extension in specified path.
    """
    r = 0
    for p in os.listdir(path):
        if os.path.isdir(f'{path}/{p}'):
            r += number_of_files_with_extensions(f'{path}/{p}', extension)
        elif p.endswith(f'.{extension}'):
            r += 1
    return r
