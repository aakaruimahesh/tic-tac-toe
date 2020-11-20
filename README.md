# tic-tac-toe

[![Tic-Tac-Toe compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/aakaruimahesh/tic-tac-toe)

A simple terminal based tic-tac-toe game of 3X3 board size.
Supported for python3.3 or above

## Table of Contents

- [Feature](#feature)
- [Assumption](#assumption)
- [Install](#install)
- [Setup](#setup)
- [Unit Test](#unit-test)
- [Run game](#run-game)
- [Limitation](#limitation)
- [Maintainers](#maintainers)
- [License](#license)

## Feature

1. Program starts, prints out an empty grid
2. The program then prompts for Player 1 name, followed by their preferred symbol; assigns a default 'X'.
3. Same for Player 2 name, followed by their preferred symbol; assigns a default 'O'.
4. Players take turns making their move. If a step is illegal or invalid, the program prints out the error and asks them to enter again.
5. The game continues until it's over, when the game is over, it announces the result.

## Assumption

1. Game size may expand from 3X3 to 4X4 based on requirement.
2. User is prompt to ask if he/she wants to play again.
3. There can be multiple players more than 2.
4. Player name should not match with each other.
5. Symbol of each user should not be same.


## Install

This project uses [python](https://www.python.org/). Go check them out if you don't have them locally installed. If you already have the python installed, run the following command to install the pip package from requirement.txt. (Recommend to use virtual environment for installation.)

```sh
$ pip install -r requirement
```

## Setup

You can change the attributes in constants.py file to modify the game.

- ROW_SIZE: Increase the board size of game. default 3X3 size of board. (Min 3, Max 10)
- PLAYER_SIZE: Number of player to play in game. (Donot change the value unless you are modifying the game logic)

## Unit Test

Run the test with following command:
- python test.py

## Run Game

Run the game with following command:
- python main.py

## limitation

- The game winning logic supports only 3X3 size of board and 2 players.
- Max size of board is set to 10 to avoid the design disarray in console.

## Maintainers

[@aakaruimahesh](https://github.com/aakaruimahesh).

## License

[MIT](LICENSE) © Aakarui
