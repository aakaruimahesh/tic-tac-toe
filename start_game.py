from board import Board
from player import Player


class StartGame:
    board = None
    move_history = list()

    # constructor
    def __init__(self):
        self.board = Board()
        print('#################################')
        print('Starting the game:')
        self.board.draw_board()

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

    def run(self):
        players = dict()
        players['X'] = Player(1)
        print('Hello {0}, your symbol is "X"'.format(players['X'].get_name()))
        players['O'] = Player(2)
        if players['X'].get_name() == players['O'].get_name():
            players['O'].set_get_name()(players['O'].get_name() + '_2')
        print('Hello {0}, your symbol is "O"'.format(players['O'].get_name()))

        total_blocks = self.board.get_total_blocks()
        block_size = len(self.move_history)
        board = self.board.get_board()
        keep_filling = True
        while keep_filling:
            turn = 'X' if block_size % 2 == 0 else 'O'
            player = players[turn]
            move = self.get_player_move(player, turn)
            if move is not None:
                board[move] = turn
                self.move_history.append({'player': player, 'move': move})
            self.board.draw_board(board)
            check_winner = self.board.check_winner(turn)
            block_size = len(self.move_history)
            player = players.get(check_winner, None)
            if player:
                print('{0} ({1}) have won the game.'.format(player.name, turn))
                break

            if block_size >= total_blocks:
                print('The game is draw.')
                break
