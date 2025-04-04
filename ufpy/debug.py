from os import PathLike, environ
from typing import Callable, Any, Optional
from datetime import datetime
import colorama

__all__ = (
    'Level',
    'DebuggerDefaults',
    'Debugger'
    )

class Level:
    INFO = 'info'
    WARN = 'warn'
    ERROR = 'error'


class DebuggerDefaults:
    LAYOUT = '{emoji} [{level}] {{time}} {msg}'
    TIME = '%d %b %Y, %H:%M:%S'
    COLOR = {
        Level.INFO: colorama.Fore.LIGHTBLUE_EX,
        Level.WARN: colorama.Fore.LIGHTYELLOW_EX,
        Level.ERROR: colorama.Fore.LIGHTRED_EX
    }
    EMOJI = {
        Level.INFO: 'ℹ️',
        Level.WARN: '⚠️',
        Level.ERROR: '❌'
    }
    LEVEL_MSG = {
        Level.INFO: 'INFO',
        Level.WARN: 'WARNING',
        Level.ERROR: 'ERROR'
    }


class Debugger:
    def __init__(
        self, *, file: Optional[str | PathLike] = '',
        func: Optional[Callable[[str, ...], Any]] = None,
        # Settings
        layout: str = DebuggerDefaults.LAYOUT,
        time: bool | str = True,
        color: bool | dict[str, str] = True,
        emoji: bool | dict[str, str] = True,
        level_msg: bool | dict[str, str] = True
        ):
        # Init
        if environ.get('COLORAMA_INIT', None) is None:
            environ['COLORAMA_INIT'] = '1'
            colorama.init()

        self.file = file
        self.func = func or (lambda *_: None)
        self.layout = layout
        
        if time is True:
            self.time = DebuggerDefaults.TIME
        elif time is False:
            self.time = None
        else:
            self.time = time

        if color is True:
            self.color = DebuggerDefaults.COLOR
        elif color is False:
            self.color = {}
        else:
            self.color = color

        if emoji is True:
            self.emoji = DebuggerDefaults.EMOJI
        elif emoji is False:
            self.emoji = {}
        else:
            self.emoji = emoji

        if level_msg is True:
            self.level_msg = DebuggerDefaults.LEVEL_MSG
        elif level_msg is False:
            self.level_msg = {}
        else:
            self.level_msg = level_msg

    def log(self, level: str, msg: str) -> None:
        pr_msg = self.layout.replace('{level}', self.level_msg.get(level, ''))
        pr_msg = pr_msg.replace('{emoji}', self.emoji.get(level, ''))
        pr_msg = pr_msg.replace('{msg}', msg)
        pr_msg = pr_msg.replace('{time}', datetime.now().strftime(self.time or ''))

        # Func
        self.func(f'{self.color.get(level, '')}{pr_msg}{colorama.Fore.RESET}')

        # File
        if self.file:
            with open(self.file, mode='a', encoding='utf-8') as f:
                f.write(pr_msg + '\n')

    def info(self, msg: str) -> None:
        return self.log(Level.INFO, msg)
    
    def warn(self, msg: str) -> None:
        return self.log(Level.WARN, msg)

    def error(self, msg: str) -> None:
        return self.log(Level.ERROR, msg)

