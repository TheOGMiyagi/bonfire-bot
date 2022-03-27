"""Roll table logic for character names.
"""
from random import choice

from src.rpg.roll_tables.variables import character_names_variables as _VARS


def rt_neutral_name():
    return choice(_VARS.NEUTRAL_NAMES)
def rt_male_name():
    return choice(_VARS.MALE_NAMES)
def rt_female_name():
    return choice(_VARS.FEMALE_NAMES)

def main():
    for _ in range(10):
        _male_name = rt_male_name()
        _neutral_name = rt_neutral_name()
        _female_name = rt_female_name()
        print('\n\n', f'Male Name: {_male_name}\nNeutral Name: {_neutral_name}\nFemale Name: {_female_name}')


if __name__ == '__main__':
    main()
