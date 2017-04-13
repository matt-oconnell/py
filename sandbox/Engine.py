import random

class Engine():
    def __init__(self, fighter1, fighter2):
        self.opponent_fighter = fighter1
        self.user_fighter = fighter2
        self.turn = random.uniform(0, 1)

    def start(self):
        print 'Starting match....'
        self.next_turn()

    def next_turn(self):
        self.print_status()
        self.turn = int(abs(self.turn - 1))
        if self.turn == 1:
            self.prompt_user()
        else:
            self.auto_attack()

    def print_status(self):
        print """Opponent: {} Your Fighter: {}
        """.format(self.opponent_fighter.get_health(), self.user_fighter.get_health())

    def prompt_user(self):
        move = raw_input("""
        Choose a move. (z = Kick, x = Punch)
        """)
        if move == 'x':
            self.user_fighter.punch(self.opponent_fighter)
            print "Punched!"
        else:
            self.user_fighter.kick(self.opponent_fighter)
            print "Kicked!"
        self.check_healths()


    def auto_attack(self):
        attacks = [self.opponent_fighter.punch, self.opponent_fighter.kick]
        attack_descs = ['punch', 'kick']
        i = int(random.uniform(0, 1))
        attacks[i](self.user_fighter)
        print 'Opponent attacked with a {}'.format(attack_descs[i])
        self.check_healths()

    def check_healths(self):
        someones_dead = False
        if (self.opponent_fighter.get_health() <= 0):
            print 'You are the Champion!!!!'
            someones_dead = True
        if (self.user_fighter.get_health() <= 0):
            print 'You died....'
            someones_dead = True
        if (someones_dead):
            print 'Game Over.'
            exit(0)
        else:
            self.next_turn()