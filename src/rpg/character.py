"""# character.py
This module contains logic regarding player characters.
"""
from dataclasses import dataclass
from math import floor
from random import randint
import logging

@dataclass(order=True)
class Character:
    """This class contains logic and stats regarding player characters.
    """
    attunement: int = 10
    dexterity: int = 10
    endurance: int = 10
    faith: int = 10
    intelligence: int = 10
    strength: int = 10
    vitality: int = 10

    def roll_stats(self):
        """This method generates a randomized set of stats.
        """
        def _stat_roll():
            """This method returns the sum of two random numbers and 12.
            """
            return randint(1, 6) + randint(1, 6) + 12
        self.attunement = _stat_roll()
        logging.debug('Attunement Determined Randomly...')
        self.dexterity = _stat_roll()
        logging.debug('Dexterity Determined Randomly...')
        self.endurance= _stat_roll()
        logging.debug('Endurance Determined Randomly...')
        self.faith = _stat_roll()
        logging.debug('Faith Determined Randomly...')
        self.intelligence = _stat_roll()
        logging.debug('Intelligence Determined Randomly...')
        self.strength = _stat_roll()
        logging.debug('Strength Determined Randomly...')
        self.vitality = _stat_roll()
        logging.debug('Vitality Determined Randomly...')

        logging.debug('Instance initialization completed successfully.')
    def __str__(self):
        """This method handles the printability of the class and its attributes.
        """
        logging.info('<Class "main.Character(object)"> is being printed as a string...')
        _stats = (f'Attunememt:\t{self.attunement}\t(AB +{self.attunement_bonus})',
            f'Dexterity:\t{self.dexterity}\t(DB +{self.dexterity_bonus})',
            f'Endurance:\t{self.endurance}\t(EB +{self.endurance_bonus})',
            f'Faith:\t\t{self.faith}\t(FB +{self.faith_bonus})',
            f'Intelligence:\t{self.intelligence}\t(IB +{self.intelligence_bonus})',
            f'Strength:\t{self.strength}\t(SB +{self.strength_bonus})',
            f'Vitality:\t{self.vitality}\t(VB +{self.vitality_bonus})\n',
            f'Level: {self.level}')
        _output = '\n'.join(_stats)
        logging.debug('main.character(object).__str__() completed successfully.')
        return _output
    
    @property
    def attunement_bonus(self):
        return floor(self.attunement/10)
    @property
    def dexterity_bonus(self):
        return floor(self.dexterity/10)
    @property
    def endurance_bonus(self):
        return floor(self.endurance/10)
    @property
    def faith_bonus(self):
        return floor(self.faith/10)
    @property
    def intelligence_bonus(self):
        return floor(self.intelligence/10)
    @property
    def strength_bonus(self):
        return floor(self.strength/10)
    @property
    def vitality_bonus(self):
        return floor(self.vitality/10)
    @property
    def level(self):
        _stat_bonuses = (self.attunement_bonus,
            self.dexterity_bonus,
            self.endurance_bonus,
            self.faith_bonus,
            self.intelligence_bonus,
            self.strength_bonus,
            self.vitality_bonus)
        return sum(_stat_bonuses)


def main():
    """Main Module Method.
    """
    c = Character()
    c.roll_stats()
    print(c)

if __name__ == '__main__':
    main()
