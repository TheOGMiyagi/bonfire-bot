"""Roll table logic for lord information.
"""
from random import choice

from src.rpg.roll_tables.variables import lords_variables as _VARS


_LIST_OF_NAMES = (_VARS.TUPLE_A1,
    _VARS.TUPLE_A2,
    _VARS.TUPLE_A3,
    _VARS.TUPLE_A4,
    _VARS.TUPLE_A5,
    _VARS.TUPLE_A6)
_LIST_OF_DETAILS = (_VARS.TUPLE_B1,
    _VARS.TUPLE_B2,
    _VARS.TUPLE_B3,
    _VARS.TUPLE_B4,
    _VARS.TUPLE_B5,
    _VARS.TUPLE_B6)
_LIST_OF_THEMES = (_VARS.TUPLE_C1,
    _VARS.TUPLE_C2,
    _VARS.TUPLE_C3,
    _VARS.TUPLE_C4,
    _VARS.TUPLE_C5,
    _VARS.TUPLE_C6)


def rt_lord_info(**kwargs):
    _return_type = kwargs.get('return_type', 'tuple')
    _name = choice(choice(_LIST_OF_NAMES))
    _detail = choice(choice(_LIST_OF_DETAILS))
    _theme = choice(choice(_LIST_OF_THEMES))
    if _return_type == 'string':
        return f'Name: {_name}\nDetail: {_detail}\nTheme: {_theme}'
    elif _return_type == 'tuple':
        return _name, _detail, _theme

def main():
    for _ in range(10):
        _name, _detail, _theme = rt_lord_info()
        print('\n\n', f'Name: {_name}\nDetail: {_detail}\nTheme: {_theme}')


if __name__ == '__main__':
    main()
