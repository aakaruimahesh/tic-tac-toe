
class Player:
    name = ''

    def __init__(self, player_number):
        is_valid_name = False
        name = ''
        while not is_valid_name:
            name = input('Enter the Player {0} name: '.format(player_number))
            if name:
                is_valid_name = True
            else:
                print('Please enter the valid name.')
        self.set_name(name)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
