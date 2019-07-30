
from numpy.random import randint


def optimal_move(taken_spots):
    while True:
        position = randint(1, 9, 1)
        if position not in taken_spots:
            return int(position)
