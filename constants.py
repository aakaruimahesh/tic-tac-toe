'''
Every constant variable is declared in this file.
'''

## This is size of game in a each row.
## If ROW size is 3, generated board will be square of row size i.e.9
ROW_SIZE = 3
## Number of player to play in game
## DONOT MODIFY unless you have everything setup for more players than 2
PLAYER_SIZE = 2
##
HOST = '127.0.0.1'
PORT = 8080
PLAYER_ID1 = 41799
PLAYER_ID2 = 35171
DATA_TYPE = {
    'INITIALIZING_PLAYER': 'INITIALIZING_PLAYER',
    'WAITING_PLAYER': 'WAITING_PLAYER',
}
GAME_STATUS = {
    'START': 'START',
    'WAITING': 'WAITING',
    'PLAYING': 'PLAYING',
    'COMPLETE': 'COMPLETE'
}
