from constants import ROW_SIZE

'''
This class generates the board for tic-tac-toe based on row_size defined in constants file.
It displays the manual for the game as well.
'''
class Board:

    row_size = ROW_SIZE
    total_blocks = row_size * row_size

    # constructor
    def __init__(self):
        self.display_manual()

    # generates the board size based on row_size in each row
    def generate_board(self):
        board = dict()
        row_size = self.row_size

        if row_size < 3:
            raise AssertionError ('The game size should not be less than 3.')
        if row_size > 10:
            raise AssertionError ('The game size should not be greater than 10.')

        for i in range(self.total_blocks):
            key = i + 1
            board[key] = ' ' if key < 10 else '  '
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
    def draw_board(self, auto_fill=False):
        row_size = self.row_size
        total_blocks = self.total_blocks
        board = self.generate_board()
        border_line = self.draw_border()
        display_string = ''                                 # board UI
        for key, value in board.items():
            data = value if auto_fill == False else key
            if key % row_size != 0:
                block = ' {0} |' if key < 10 else '{0} |'
                display_string += block.format(data)
            else:
                block = ' {0} ' if key < 10 else '{0} '
                display_string += block.format(data) + '\n'
                if key != total_blocks:
                    display_string += '{0}\n'.format(border_line)
        print(display_string)

    # It is to show the greeting and manual of the game to user
    def display_manual(self):
        print('Welcome to the game.')
        print('Here is how you play tic tac toe.')
        print('Please press 1 to {} to place your move.'.format(self.total_blocks))
        display_board = self.draw_board(auto_fill=True)     # manual display for game
        print('#################################')
        print('Starting the game:')
        display_board = self.draw_board()                   # Start of game with empty grid line
