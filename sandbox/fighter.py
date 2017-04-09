class Fighter(object):
    def __init__(self, name):
        self.name = name

    def punch(self, Opponent):
        Opponent.damage(self.punchPower)

    def kick(self, Opponent):
        Opponent.damage(self.kickPower)

    def damage(self, amount):
        self.health = self.health - amount

    def get_health(self):
        return self.health