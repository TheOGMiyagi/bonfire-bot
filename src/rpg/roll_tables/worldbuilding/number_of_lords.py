"""Roll table logic for the number of lords.
"""
from random import choices


_POSSIBLE_NUMBER_OF_LORDS = (4, 5, 6)


def rt_number_of_lords():
    return choices(_POSSIBLE_NUMBER_OF_LORDS, weights=(4, 2, 2), k=1)[0]

def main():
    for _ in range(10):
       print(rt_number_of_lords(), end=', ')


if __name__ == '__main__':
    main()
