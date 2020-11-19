from constants import ROW_SIZE
import numpy as np

'''
This is Baord Class.
This class generates the board for tic-tac-toe based on row_size defined in constants file.
It displays the manual for the game as well.
'''
class Board:
    # Class variables
    row_size = ROW_SIZE                             # size of row
    total_blocks = row_size * row_size              # Total block in game
    board = list()                                  # board game list for indexing position based on size

    # constructor
    def __init__(self, row_size=ROW_SIZE):
        self.row_size = row_size                    # dynamic board size
        self.total_blocks = row_size * row_size
        self.display_manual()                       # Displaying manual while initializing the class

    # getter method to return the board list from class variable
    def get_board(self):
        return self.board

    # setter method to set the board value in class variable
    def set_board(self, board):
        self.board = board

    # getter method to return total_blocks from class variable
    def get_total_blocks(self):
        return self.total_blocks

    # setter method to set total_blocks in class variable
    def set_total_blocks(self, total_blocks):
        self.total_blocks = total_blocks

    # generates the board size based on row_size in each row
    def generate_board(self):
        board = list()
        row_size = self.row_size

        if row_size < 3:
            raise AssertionError ('The game size should not be less than 3.')
        if row_size > 10:
            raise AssertionError ('The game size should not be greater than 10.')

        for i in range(self.total_blocks):
            key = i + 1
            board.append(' ' if key < 10 else '  ')
        return board

    #  generates the border to display in each row of game display
    def draw_border(self):
        row_size = self.row_size
        block = '---+'
        line = ''
        for i in range(row_size):
            index = i + 1
            if index != row_size:
                line += block
            else:
                line += block[:-1]
        return line

    # generates the string of board to be to show in console i.e. visibility of board in screen
    def draw_board(self, board=None, auto_fill=False):
        row_size = self.row_size
        total_blocks = self.total_blocks
        if not board:
            board = self.generate_board()
        border_line = self.draw_border()            # border to display after each row
        display_string = ''                         # board UI
        for i, value in enumerate(board):
            key = i + 1
            data = value if auto_fill == False else key
            if key % row_size != 0:
                block = ' {0} |' if key < 10 else '{0} |'
                display_string += block.format(data)
            else:
                block = ' {0} ' if key < 10 else '{0} '
                display_string += block.format(data) + '\n'
                if key != total_blocks:
                    display_string += '{0}\n'.format(border_line)
        self.set_board(board)
        print(display_string)

    # method to show the greeting and manual of the game to user
    def display_manual(self):
        print('Welcome to the game.')
        print('Here is how you play tic tac toe.')
        print('Please press 1 to {} to place your move.'.format(self.total_blocks))
        self.draw_board(auto_fill=True)         # manual display for game

    # method to validate moves with board size and free stop
    def is_validate_move(self, board, move):
        status = False, ''
        if move < 0 or move > (self.get_total_blocks() - 1):    # check if the move is within board size
            status = False, 'Invalid move. Please press from 1 to {} to place a move.'.format(self.total_blocks)
        elif board[move].strip():                               # check if stop is occupied or not
            status = False, 'That place is already filled. Please place a move on another place.'
        else:
            status = True, ''
        return status

    # methos to check if the player won the game
    def check_winner(self, turn, player):
        row_size = self.row_size
        board = np.reshape(self.get_board(), (-1, row_size))            # converting into 2D array
        mask = board == turn                                            # masking turn value into boolean
        is_winner = mask.all(0).any() | mask.all(1).any()               # checks horizontal and vertical win case
        is_winner |= np.diag(mask).all() | np.diag(mask[:,::-1]).all()  # checks diagonal win case
        if is_winner:
            return player
        return None # No winner
