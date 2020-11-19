
class Player:
    name = ''

    def __init__(self, player_number):
        name = input('Enter the Player {0} name: '.format(player_number))
        self.set_name(name)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
