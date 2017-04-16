import random


class Fighter(object):
    attacks = {}

    def __init__(self, is_computer):
        self.health = 100
        self.is_computer = is_computer

    def attack(self):
        if not self.is_computer:
            attack = self._pick_attack()
        else:
            attack = self._random_attack()
        return self.attacks[attack]

    def take_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.health
        else:
            return 0

    def _pick_attack(self):
        choice_string = 'Pick an attack:\n'
        for attack in self.attacks:
            choice_string += '{}\n'.format(attack)
        return raw_input(choice_string)

    def _random_attack(self):
        return random.sample(self.attacks, 1)[0]
