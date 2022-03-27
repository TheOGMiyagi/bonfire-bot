"""Roll table logic for covenant names.
"""
from random import choice

from src.rpg.roll_tables.variables import covenant_names_variables as _VARS


_LIST_OF_PREFIXES = (_VARS.TUPLE_A1,
    _VARS.TUPLE_A2,
    _VARS.TUPLE_A3,
    _VARS.TUPLE_A4,
    _VARS.TUPLE_A5,
    _VARS.TUPLE_A6)
_LIST_OF_SUFFIXES = (_VARS.TUPLE_B1,
    _VARS.TUPLE_B2,
    _VARS.TUPLE_B3,
    _VARS.TUPLE_B4,
    _VARS.TUPLE_B5,
    _VARS.TUPLE_B6)  

def rt_covenant_name():
    _prefix = choice(choice(_LIST_OF_PREFIXES))
    _suffix = choice(choice(_LIST_OF_SUFFIXES))
    return f'{_prefix} {_suffix}'

def main():
    for _ in range(10):
        _prefix, _suffix = rt_covenant_name()
        print(rt_covenant_name)


if __name__ == '__main__':
    main()
