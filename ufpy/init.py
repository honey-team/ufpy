import json
import os.path
from pathlib import Path
from tempfile import gettempdir
from typing import Any

import ujson

__all__ = (
    'init',
    'defaults'
)

default_settings = {
    'starting': 1,
    'udict': {
        'default_default': None
    }
}

settings_path = Path(gettempdir()) / 'ufpy-settings' / 'settings.json'


def __jload() -> dict[str, Any]:
    with open(settings_path) as f:
        raw_json = f.read()
    return ujson.loads(raw_json)


def __jwrite(new_settings: dict[str, Any]) -> None:
    with open(settings_path, 'w') as f:
        f.write(json.dumps(new_settings, indent=4))


class _Missing:
    ...


def __not_missing(x: object) -> bool:
    return x != _Missing


def __get_dict(path: str, __dict: dict[str, Any]) -> dict[str, Any]:
    if not '/' in path:
        return __dict
    keys = path.split('/')[:-1]

    r = __dict
    for i in keys:
        r = r[i]
    return r


def init(*, starting: int = _Missing, udict_default_default: Any = _Missing) -> None:
    basedir = os.path.dirname(settings_path)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    if not os.path.exists(settings_path):
        __jwrite(default_settings)
    s = __jload()

    def __change(name: str, obj: object) -> None:
        if __not_missing(obj):
            s2 = __get_dict(name, s)
            s2[name.split('/')[-1]] = obj

    __change('starting', starting)
    __change('udict/default_default', udict_default_default)
    __jwrite(s)


def defaults() -> None:
    __jwrite(default_settings)


def get_setting(name: str) -> Any:
    return __get_dict(name, __jload())[name.split('/')[-1]]
