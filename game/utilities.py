

from numpy import (
    unique,
    fliplr
)


def check_if_game_over(matrix):
    """
    checks all directions of the game board matrix to see if there has been
    a winner.
    :return:
    """
    winnable_directions = [
        matrix[0],  # first row
        matrix[1],  # second row
        matrix[2],  # third row
        matrix[:, 0],  # first col
        matrix[:, 1],  # second col
        matrix[:, 2],  # third col
        matrix.diagonal(),  # top left to bottom right
        fliplr(matrix).diagonal()  # top right to bottom left
    ]

    for direction in winnable_directions:
        if None not in direction:
            n_unique = len(unique(direction))
            if n_unique == 1:
                return True


def is_empty_space(matrix, row, col):
    """

    :param matrix:
    :param position:
    :return:
    """
    if not matrix[row, col]:
        return True
    else:
        return False


def map_position(pos):
    mapper = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }

    if pos in mapper.keys():
        return mapper[pos]
    else:
        return None

