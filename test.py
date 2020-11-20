import unittest
from unittest.mock import patch

from board import Board
from player import Player
from start_game import StartGame


class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """

    @patch('board.Board.display_manual')
    def test_manual_displayed(self, mock):
        StartGame()
        self.assertTrue(mock.called)

    @patch('board.Board.generate_board')
    def test_board_generated(self, mock):
        StartGame()
        self.assertTrue(mock.called)

    def test_draw_board_for_n_squares(self):
        for n in range(3, 10):
            board = Board(n)
            generated_board = board.generate_board()
            self.assertEquals(len(generated_board), n**2)

    def test_disallows_invalid_move(self):
        game = StartGame()
        game_board = game.board
        game_board.board[1] = 'X'
        self.assertEquals(game.board.is_validate_move(game_board.board, 1)[0], False)

    @patch('builtins.input')
    def test_valid_winner(self, mocked_input):
        game = StartGame()
        game_board = game.board
        p1 = Player('X')
        p1.set_name('p1')
        game_board.board = ['X', ' ', 'Y', ' ', 'X', ' ', 'Y', ' ', 'X']
        self.assertEquals(game_board.check_winner('X', p1), p1)

    @patch('builtins.input')
    def test_no_winner(self, mocked_input):
        game = StartGame()
        game_board = game.board
        p1 = Player('X')
        p1.set_name('p1')
        game_board.board = ['X', ' ', 'X', ' ', 'Y', ' ', 'Y', ' ', 'X']
        self.assertEquals(game_board.check_winner('X', p1), None)


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()

