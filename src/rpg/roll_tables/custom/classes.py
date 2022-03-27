"""Roll table logic for lord information.
"""
from random import choice


_LIST_OF_CLASSES = ('Assassin',
    'Bandit',
    'Cleric',
    'Deprived',
    'Explorer',
    'Herald',
    'Hunter',
    'Knight',
    'Mercenary',
    'Northern Warrior',
    'Pyromancer',
    'Sorcerer',
    'Thief',
    'Wanderer',
    'Warrior')


def rt_classes():
    return choice(_LIST_OF_CLASSES)

def main():
    for _ in range(10):
        _class = rt_classes()
        print('\n\n', f'Class: {_class}')


if __name__ == '__main__':
    main()
