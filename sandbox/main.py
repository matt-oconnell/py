from Ninja import Ninja
from Soldier import Soldier
import random

# f1 = Fighter(20, 20)
# f2 = Fighter(10, 30)
#
# game = Engine(f1, f2)
#
# game.start()


fighter_types = [Ninja, Soldier]

class User(object):
    def __init__(self):
        self.get_name()
        self.get_fighter_type()

    def get_name(self):
        self.name = raw_input('What\'s your name?')

    def get_fighter_type(self):
        choice_string = 'Choose a fighter type'
        for i, fighter in enumerate(fighter_types):
            choice_string += '[{}] {}'.format(i, fighter.type)
        charIndex = raw_input(choice_string)

        Fighter = fighter_types[int(charIndex)]
        self.fighter = Fighter(self.name)

class Opponent(object):
    def __init__(self):
        self.set_name()
        self.set_fighter()

    def set_name(self):
        self.name = 'The AI of Doom'

    def set_fighter(self):
        fighter_arr_length = len(fighter_types)
        self.fighter = fighter_types[int(random.uniform(0, fighter_arr_length))]
        # todo

# Initialize User
user = User()
