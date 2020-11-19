from start_game import StartGame


if __name__ == "__main__":
    try:
        keep_playing = True
        while keep_playing:
            start_game = StartGame()
            start_game.run()

            play_again = input('Do you want to play new game again? (Y / N or any key to exit): ')
            if play_again.lower() != 'y':
                keep_playing = False
    except AssertionError:
        print('GameError. Input the valid ROW_SIZE')
    except Exception as e:
        print('Error: ' + str(e))
