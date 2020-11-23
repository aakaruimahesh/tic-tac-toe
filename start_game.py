import socket
import sys
from board import Board
from player import Player
from symbol import Symbol
from constants import PLAYER_SIZE, DATA_TYPE, GAME_STATUS
from constants import HOST, PORT

'''
This is StartGame Class.
This class initiates the game showing the manual and input from players.
'''
class StartGame:
    # initializing class variablesGAME_STATUS
    move_history = list()                                # history of moves that player have placed
    player_id = None
    start_game = False

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
        symbol_list = list()
        for i in range(PLAYER_SIZE):
            player = Player(i + 1)
            player_name = player.get_name()
            symbol = Symbol(i, player_name, symbol_list)
            print('Hello {0}, your symbol is "{1}"'.format(player_name, symbol.get_symbol()))
            players[symbol] = player

        total_blocks = self.board.get_total_blocks()
        board = self.board.get_board()
        keep_filling = True
        winner = None
        index = 0
        keep_playing = True
        while keep_playing:
            for symbol, player in players.items():
                turn = symbol.get_symbol()
                move = self.get_player_move(player, turn)
                board[move] = turn
                self.move_history.append({'player': player, 'move': move})  # saving players moves in history
                self.board.draw_board(board)                                # draw board to display player move
                winner = self.board.check_winner(turn, player)              # get the winner player object
                index += 1
                if index >= total_blocks or winner:
                    keep_playing = False
                    if winner:
                        print('{0} ({1}) have won the game.'.format(player.name, turn))
                    break

        if not winner:
            print('The game is draw.')

    def send_data(self, sock, data_type, data):
        if isinstance(data, dict):
            data['data_type'] = data_type
        sock.sendall(bytes(str(data) + "\n", "utf-8"))

    def parse_data(self, data):
        try:
            data = eval(data)
        except:
            data = dict()
        return data

    def initiate_client(self, player_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.connect((HOST, PORT))
            self.run_game_client(sock=sock, player_id=player_id)

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            parsed = self.parse_data(received)
            print(received)

    def run_game_client(self, sock, player_id):
        players = dict()
        symbol_list = list()
        player = Player(player_id)
        player_name = player.get_name()
        symbol = Symbol(player_id, player_name, symbol_list)
        print('Hello {0}, your symbol is "{1}"'.format(player_name, symbol.get_symbol()))
        players[symbol] = player

        total_blocks = self.board.get_total_blocks()
        board = self.board.get_board()
        data = {
            'player': players
        }
        self.send_data(sock, DATA_TYPE['INITIALIZING_PLAYER'], data)
        if self.start_game:
            keep_filling = True
            winner = None
            index = 0
            keep_playing = True
            while keep_playing:
                for symbol, player in players.items():
                    turn = symbol.get_symbol()
                    move = self.get_player_move(player, turn)
                    board[move] = turn
                    self.move_history.append({'player': player, 'move': move})  # saving players moves in history
                    self.board.draw_board(board)                                # draw board to display player move
                    winner = self.board.check_winner(turn, player)              # get the winner player object
                    index += 1
                    if index >= total_blocks or winner:
                        keep_playing = False
                        if winner:
                            print('{0} ({1}) have won the game.'.format(player.name, turn))
                        break

            if not winner:
                print('The game is draw.')
