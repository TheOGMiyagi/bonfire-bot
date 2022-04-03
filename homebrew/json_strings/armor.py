"""Module Docstring Text
"""
import json
import logging


#? Script Configuration Instructions
logging.basicConfig(level=logging.DEBUG)


def questions(**kwargs):
    """This method asks about the properties of a new armor set, returning a JSON-encoded string representing it.
    """
    _default = kwargs.get('defaults', False)
    #* Gather Data
    if _default:
        _name = 'Default Name'
        _bolt_defense = 0
        _crush_defense = 0
        _dark_defense = 0
        _fire_defense = 0
        _magic_defense = 0
        _pierce_defense = 0
        _slash_defense = 0
        _toxic_defense = 0
        _weight_rating = 'Normal'
        _special = None
    else:
        _name = input('What is the name of this armor set?\n')
        _bolt_defense = int(input('What is the Bolt Defense for this armor set?\n'))
        _crush_defense = int(input('What is the Crush Defense for this armor set?\n'))
        _dark_defense = int(input('What is the Dark Defense for this armor set?\n'))
        _fire_defense = int(input('What is the Fire Defense for this armor set?\n'))
        _magic_defense = int(input('What is the Magic Defense for this armor set?\n'))
        _pierce_defense = int(input('What is the Pierce Defense for this armor set?\n'))
        _slash_defense = int(input('What is the Slash Defense for this armor set?\n'))
        _toxic_defense = int(input('What is the Toxic Defense for this armor set?\n'))
        _weight_rating = input('What is the weight rating for this armor set?\n0 = Normal\n1 = Heavy (Minimum Endurance: 30)\n2 = Very Heavy (Minimum Endurance: 40)\n')
        _special = input("What is the special effect text associated with this armor set?\n(Just press enter if the armor doesn't have a special trait.)\n")
    
    #? Conditional re-assignment of relevant variables.
    try:
        if _weight_rating.lower() == 'normal' or _weight_rating == '0':
            _weight_rating = 0
        elif _weight_rating.lower() == 'heavy' or _weight_rating == '1':
            _weight_rating = 1
        elif _weight_rating.lower() == 'very heavy' or _weight_rating == '2':
            _weight_rating = 2
    except KeyError:
        logging.error(KeyError)
    
    _object = {'name': _name,
        'defenses': {
            'bolt': _bolt_defense,
            'crush': _crush_defense,
            'dark': _dark_defense,
            'fire': _fire_defense,
            'magic': _magic_defense,
            'pierce': _pierce_defense,
            'slash': _slash_defense,
            'toxic': _toxic_defense
            },
            'weight-rating': _weight_rating,
            'special': _special}
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