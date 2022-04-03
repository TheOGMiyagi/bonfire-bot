"""This module has tools and helper functions for dealing with JSON data.
"""
import json
import logging

# Script Configuration
logging.basicConfig(level=logging.DEBUG)


def homebrew_strings_handler(json_string: str, **kwargs):
    """This method writes JSON files for homebrew items.
    """
    _filename = kwargs.get('filename', 'homebrew_object.json')
    with open(_filename, 'w') as file:
        file.write(json_string)

# MAIN METHOD
def main():
    """This method tests if homebrew_strings_handler() is working.
    """
    _test_string = '{\n\t"test-results" : "Test Passed!"\n}'
    homebrew_strings_handler(_test_string)
    with open('homebrew_object.json', 'r') as file:
        test_object = json.loads(file.read())
    print(test_object['test-results'])


# DRIVER CODE
if __name__ == '__main__':
    main()
else:
    logging.debug('%s was successfully imported!', __name__)