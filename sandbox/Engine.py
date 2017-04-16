import random


class Engine:
    def __init__(self, user1, user2):
        self.users = [user1, user2]
        self.turn = int(random.uniform(0, 1))

    def start(self):
        fighter1 = self.users[0].fighter
        fighter2 = self.users[1].fighter
        print 'Showdown!\n{} the {} takes on {} the {}'\
            .format(self.users[0].name, fighter1.type, self.users[1].name, fighter2.type)
        self._next_turn()

    def _next_turn(self):
        self.turn = abs(self.turn - 1)
        attacker = self.users[self.turn]
        defender = self.users[abs(self.turn - 1)]
        attack = self._attack(attacker.fighter.attack())
        print '\n{} attacks!'.format(attacker.name)
        if attack:
            print 'Hit! for {} damage'.format(attack)
            defender.fighter.take_damage(attack)
            print '{}\'s health is down to {}'.format(defender.name, defender.fighter.health)
            if defender.fighter.health < 1:
                print '{} the {} won!'.format(attacker.name, attacker.fighter.type)
                exit(0)
        else:
            print '{} missed!\n'.format(attacker.name)

        self._next_turn()

    def _attack(self, fighter_attack):
        rand = random.randint(0, 100)
        if rand < fighter_attack['accuracy']:
            return fighter_attack['power']