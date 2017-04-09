from fighter import Fighter

class Soldier(Fighter):
    type = 'Soldier'
    attacks = {
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

