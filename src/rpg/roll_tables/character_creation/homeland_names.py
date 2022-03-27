"""Roll table logic for homeland names.
"""
from random import choice

from src.rpg.roll_tables.variables import homeland_names_variables as _VARS


_LIST_OF_ROLL_TABLES = (_VARS.TUPLE_A1,
    _VARS.TUPLE_A2,
    _VARS.TUPLE_A3,
    _VARS.TUPLE_A4,
    _VARS.TUPLE_A5,
    _VARS.TUPLE_A6)

def rt_homeland_name():
    return choice(choice(_LIST_OF_ROLL_TABLES))

def main():
    for _ in range(10):
        _name = rt_homeland_name()
        print('\n\n', f'Homeland: {_name}')


if __name__ == '__main__':
    main()
