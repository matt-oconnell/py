from User import User
from Engine import Engine

user_1 = User(True)
user_2 = User()

game = Engine(user_1, user_2)
game.start()

# print user_1.name
# print user_1.fighter.is_computer
# print user_1.fighter
# print user_2.name
# print user_2.fighter.is_computer
# print user_2.fighter