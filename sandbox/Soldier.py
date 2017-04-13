from Fighter import Fighter


class Soldier(Fighter):
    type = 'Soldier'

    def __init__(self, is_computer=False):
        super(Soldier, self).__init__(is_computer)
        self.attacks = {
            'Kick': {
                'power': 50,
                'accuracy': 50
            },
            'Machine Gun': {
                'power': 80,
                'accuracy': 20,
            },
            'Tear Gas': {
                'power': 20,
                'accuracy': 80
            }
        }

