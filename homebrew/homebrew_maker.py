"""This module lets you create JSON files via user-friendly prompts.
"""
import logging

from json_strings import jsonify
from json_strings import armor, items, spells, weapons

# Script Configuration
logging.basicConfig(level=logging.INFO)



# DATA COLLECTION Method
def collect_data():
    """This method prompts the user to provide the type of object they wish to create.
    with this, the method serves those prompts and collects the answers to be returned to jsonify().
    """
    _types = {"armor": armor.questions,
        "item": items.questions,
        "spell": spells.questions,
        "weapon": weapons.questions}
    _homebrew_type = input('\n'.join(('What type of homebrew are we creating?',
        '\nOPTIONS:',
        '- Armor',
        '- Item',
        '- Spell',
        '- Weapon',
        ''))) #? Passing an empty string should give a free newline at the end of the options.
    if _homebrew_type.lower() not in _types:
        raise KeyError
    return _types[_homebrew_type]()
        

def main():
    """This method asks for object data.
    With this data, it then creates a .JSON file
    """
    _string = collect_data()
    _filename = input('Please enter a filename ending in ".json"\n')
    jsonify(_string, filename=_filename)


# DRIVER CODE
if __name__ == '__main__':
    main()
    while True:
        _repeat = input('Would you like to run this program again?\n(Yes/No)\n')
        if _repeat.lower() in ('y', 'yes'):
            main()
        elif _repeat.lower() in ('n', 'no'):
            break
        else:
            print(f'{_repeat} is not a valid input.')

else:
    logging.debug('%s was successfully imported!', __name__)