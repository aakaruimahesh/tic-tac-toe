import socket
import sys
import uuid
# from constants import HOST, CLIENT_PORT as PORT


'''
This is player class.
This class takes the name of players
'''
class Player:
    # declaring class variables
    id = ''
    name = ''

    # constructor: takes valid player name
    def __init__(self, player_number):
        is_valid_name = False
        while not is_valid_name:
            name = input('Enter the Player {0} name: '.format(player_number))
            if name:
                name += '{0}'.format(player_number)
                self.set_name(name)
                self.set_name(str(uuid.uuid4()))
                is_valid_name = True
            else:
                print('Please enter the valid name.')

    # getter method to return name from class variable
    def get_name(self):
        return self.name

    # setter method to set name in class variable
    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
