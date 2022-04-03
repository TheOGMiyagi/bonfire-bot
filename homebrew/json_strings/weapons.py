"""Module Docstring Text
"""
import json
import logging


#? Script Configuration Instructions
logging.basicConfig(level=logging.DEBUG)

WEAPON_PROPERTIES = ('Bash',
    'Block',
    'Brutal',
    'Deadly',
    'Miracle Effect',
    'Pyromancy Effect',
    'Sorcery Effect',
    'Guard Break',
    'Heavy',
    'Parry',
    'Ranged',
    'Reach',
    'Requires',
    'Split',
    'Sweep',
    'Two-Handed',
    'Weapon Damage')


def questions(**kwargs):
    """This method asks about the properties of a new weapon, returning a JSON-encoded string representing it.
    """
    _default = kwargs.get('defaults', False)
    if _default:
        _name = 'Default Name'
        _damage_formula = '(0 + DB + SB)'
        _properties = 'Brutal 1, Parry (2-4), Reach'
    else:
        _name = input('Please enter the name of this weapon.\n')
        _damage_formula = input('Please enter the damage formula for this weapon.\n')
        _properties = input('Please enter the properties for this weapon.\n(Separated by commas)\n')
    _object = {'name': _name, 'damage-formula': _damage_formula, 'properties': _properties}
    return json.dumps(_object)


# MAIN METHOD
def main():
    """Method Docstring Text
    """
    _string = questions(defaults=True)
    #_string = questions()
    print(_string)


# DRIVER CODE
if __name__ == '__main__':
    main()
else:
    logging.debug(('%s was successfully imported!', __name__))