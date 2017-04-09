from fighter import Fighter

class Ninja(Fighter):
    type = 'Ninja'
    attacks = {
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
