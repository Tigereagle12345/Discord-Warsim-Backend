### A core module of the game, used primarily for miscellaneous tasks used by most modules
import os
import random

def randStr(start, stop=None, step=1):
    return str(random.randrange(start, stop, step))
class ForegroundColors:
    ### ANSI color codes
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
class BackgroundColors:
    ### ANSI color codes
    BLACK = "\033[0;40m"
    RED = "\033[0;41m"
    GREEN = "\033[0;42m"
    BROWN = "\033[0;43m"
    BLUE = "\033[0;44m"
    PURPLE = "\033[0;45m"
    CYAN = "\033[0;46m"
    LIGHT_GRAY = "\033[0;47m"
    DARK_GRAY = "\033[1;40m"
    LIGHT_RED = "\033[1;41m"
    LIGHT_GREEN = "\033[1;42m"
    YELLOW = "\033[1;43m"
    LIGHT_BLUE = "\033[1;44m"
    LIGHT_PURPLE = "\033[1;45m"
    LIGHT_CYAN = "\033[1;46m"
    LIGHT_WHITE = "\033[1;47m"
class AdditionalColors:
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
class Regex:
    UKRAINE = 'slava ukraini|слава україні|glory to ukraine'