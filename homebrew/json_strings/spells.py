"""Module Docstring Text
"""
import json
import logging


#? Script Configuration Instructions
logging.basicConfig(level=logging.DEBUG)


def questions(**kwargs):
    """This method asks about the properties of a new spell, returning a JSON-encoded string representing it.
    """
    _default = kwargs.get('defaults', False)
    #* Gather Data
    if _default:
        _name = 'Default Name'
        _spell_type = 'Sorcery'
        _requirement_amount = 0
        _casting_number = 0
        _effect = None
    else:
        _name = input('What is the name of this spell?\n')
        _spell_type = input('What is the requirement type for this spell?\n')
        _requirement_amount = int(input(f'What is the required amount of {_spell_type.title()} for this spell?\n'))
        _casting_number = int(input('What is the casting number for this spell?\n'))
        _effect = input('What is the effect text associated with this spell?\n')

    #? Conditional re-assignment of relevant variables.
    try:
        if _spell_type.lower() not in ('miracle', 'sorcery', 'pyromancy'):
            raise KeyError
    except KeyError:
        print(KeyError)
    
    _object = {'name': _name,
        'spell-type': _spell_type,
        'requirement-amount': _requirement_amount,
        'casting-number': _casting_number,
        'effect': _effect}
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