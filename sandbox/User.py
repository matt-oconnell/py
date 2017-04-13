import random
import fighterfactory

class User(object):
    def __init__(self, is_computer=False):
        self.is_computer = is_computer
        self.name = self._get_name()
        self.fighter = fighterfactory.create(is_computer)

    def _get_name(self):
        if not self.is_computer:
            return raw_input('What\'s your name?\n')
        else:
            return random.choice([
                'Dr. Evil',
                'Magneto',
                'The Joker',
                'Joe Shmoe',
                'Tony Soprano'
            ])
