import random
from Ninja import Ninja
from Soldier import Soldier

fighter_types = [
    Ninja,
    Soldier
]


def prompt_for_type():
    choice_string = 'Choose a fighter type\n'
    for i, fighter in enumerate(fighter_types):
        choice_string += '[{}] {}\n'.format(i, fighter.type)
    return raw_input(choice_string)

def create(is_computer):
    if not is_computer:
        fighter = fighter_types[int(prompt_for_type())](False)
    else:
        fighter = random.choice(fighter_types)(True)
    return fighter
