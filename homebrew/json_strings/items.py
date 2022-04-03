"""Module Docstring Text
"""
import json
import logging


#? Script Configuration Instructions
logging.basicConfig(level=logging.DEBUG)


def questions(**kwargs):
    """This method asks about the properties of a new item, returning a JSON-encoded string representing it.
    """
    _default = kwargs.get('defaults', False)
    if _default:
        _name = 'Default Name'
        _charges = 0
        _effect = None
    else:
        _name = input("Please enter the name of this item.\n")
        _consumable = input("Is this item a consumable?\n")
        if _consumable.lower() in ('y', 'yes'):
            _charges = int(input("Please enter (in numeric form) how many uses/charges one of this item has?\n"))
        elif _consumable.lower() in ('n', 'no'):
            _charges = 0
        _effect = input("Please enter the effect text for this item.\n")
    _object = {'name': _name, 'charges': _charges, 'effect': _effect}
    return json.dumps(_object)


# MAIN METHOD
def main():
    """Method Docstring Text
    """
    #_string = questions(defaults=True)
    _string = questions()
    print(_string)


# DRIVER CODE
if __name__ == '__main__':
    main()
else:
    logging.debug(('%s was successfully imported!', __name__))