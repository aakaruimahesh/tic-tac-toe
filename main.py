import sys
from start_game import StartGame
from constants import PLAYER_ID1, PLAYER_ID2


def run_game(player, game_option):
    try:
        keep_playing = True
        while keep_playing:
            start_game = StartGame()
            if game_option == 1:
                start_game.run()
            else:
                start_game.initiate_client(player)
            play_again = input('Do you want to play new game again? (Y / N or any key to exit): ')
            if play_again.lower() != 'y':
                keep_playing = False
    except AssertionError:
        print('GameError. Input the valid ROW_SIZE')
    except Exception as e:
        print('Error: ' + str(e))

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print('Do you want to play the game locally or over the network?')
        print('1. Locally')
        print('2. Over the network')
        game_option = input('Press 1 or 2 to choose the game option: ')
        if game_option == '1' or game_option == '2':
            run_game(player=1, game_option=game_option)
        else:
            print('Please input the valid option.')
    else:
        if args[1] == 'joingame':
            network_detail = input('Please enter the network detail to join')
