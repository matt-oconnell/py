from Fighter import Fighter


class Ninja(Fighter):
    type = 'Ninja'

    def __init__(self, is_computer=False):
        super(Ninja, self).__init__(is_computer)
        self.attacks = {
            'Low Kick': {
                'power': 50,
                'accuracy': 50
            },
            'Slash': {
                'power': 60,
                'accuracy': 40,
            },
            'Sneak Attack': {
                'power': 30,
                'accuracy': 70
            }
        }
