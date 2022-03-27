"""Roll table logic for land names.
"""
from random import choice

from src.rpg.roll_tables.variables import land_names_variables as _VARS

_LIST_OF_ROLL_TABLES = (_VARS.TUPLE_A1,
    _VARS.TUPLE_A2,
    _VARS.TUPLE_A3,
    _VARS.TUPLE_A4,
    _VARS.TUPLE_A5,
    _VARS.TUPLE_A6)


def rt_land_name():
    _tuple = choice(_LIST_OF_ROLL_TABLES)
    return choice(_tuple)

def main():
    for _ in range(10):
        print(rt_land_name())


if __name__ == '__main__':
    main()
