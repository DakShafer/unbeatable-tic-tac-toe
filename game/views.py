
BORDER = '      +---+---+---+\n'


def make_row(array):
    raw_string = f'      |{array[0]}|{array[1]}|{array[2]}|\n'
    return raw_string.replace('None', '   ').replace('X', ' X ').replace('O', ' O ')


def prettify(matrix):
    board = '\n'+BORDER
    for i in range(3):
        board += make_row(matrix[i]) + BORDER

    return board

