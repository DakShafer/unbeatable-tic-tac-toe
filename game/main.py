
from numpy import (
    array,
)

from itertools import cycle

from game.utilities import (
    check_if_game_over,
    is_empty_space,
    map_position
)

from game.bot.optimize import optimal_move

from game.views import prettify


class TicTacToe:
    def __init__(self):
        # initialize an empty board
        self.board = array([[None, None, None], [None, None, None], [None, None, None]])

        # create iterator to cycle between X and O
        self.player_cycle = cycle('XO')
        self.player = None

        self.taken_spots = []

    def is_game_over(self):
        return check_if_game_over(self.board)

    def take_turn(self):
        self.player = next(self.player_cycle)
        if self.player == 'X':
            while True:
                position = int(input(f'player {self.player}: enter position [1-9]: '))
                row, col = map_position(position)
                if is_empty_space(self.board, row=row, col=col):
                    self.board[row, col] = self.player
                    self.taken_spots.append(position)
                    break
                else:
                    print('spot is already taken... try again: \n')
        else:
            print('Bot:')
            row, col = map_position(optimal_move(self.taken_spots))
            self.board[row, col] = self.player

    def show(self):
        print(prettify(self.board))










