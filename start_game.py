from board import Board
from player import Player

'''
This is StartGame Class.
This class initiates the game showing the manual and input from players.
'''
class StartGame:
    # initializing class variables
    move_history = list()                           # history of moves that player have placed

    # constructor
    def __init__(self):
        self.board = Board()                            # initializing Class Board
        print('#################################')
        print('Starting the game:')
        self.board.draw_board()                         # draw the empty grid of board to show players

    # mathod that takes the valid input from player to place their move
    def get_player_move(self, player, turn):
        is_valid_move = False
        move = None
        while not is_valid_move:
            move = input('{0} ({1}) turn. \nPlease place your move({1}): '.format(player.get_name(), turn))
            try:
                move = int(move) - 1
            except ValueError:
                print('Please enter the valid move.')
            else:
                valid_move, message = self.board.is_validate_move(self.board.get_board(), move)
                if valid_move:
                    is_valid_move = True
                else:
                    print(message)
        return move

    # method to start the game
    def run(self):
        players = dict()
        players['X'] = Player(1)
        print('Hello {0}, your symbol is "X"'.format(players['X'].get_name()))
        players['O'] = Player(2)
        if players['X'].get_name() == players['O'].get_name():  # checking if the name of player 1 and player 2 collides or not
            players['O'].set_get_name()(players['O'].get_name() + '_2') # renaming to remove the name collision
        print('Hello {0}, your symbol is "O"'.format(players['O'].get_name()))

        total_blocks = self.board.get_total_blocks()
        block_size = len(self.move_history)
        board = self.board.get_board()
        keep_filling = True
        winner = None
        for i in range(total_blocks):
            turn = 'X' if block_size % 2 == 0 else 'O'
            player = players[turn]
            move = self.get_player_move(player, turn)
            board[move] = turn
            self.move_history.append({'player': player, 'move': move})  # saving players moves in history
            self.board.draw_board(board)                                # draw board to display player move
            block_size = len(self.move_history)                         # update the length of history
            check_winner = self.board.check_winner(turn)                # check the winner of game
            winner = players.get(check_winner, None)                    # get the winner player object
            if winner:
                print('{0} ({1}) have won the game.'.format(player.name, turn))
                break
        if not winner:
            print('The game is draw.')
