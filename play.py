
from game.main import TicTacToe


def play():
    print('Tic Tac Toe!!')
    print('~~~~~~~~~~~~')
    print('\nGame-play is simple... when prompted, select a numbered position, 1-9, to place your marker')
    print('(the numbers are organized like a telephone... 1-3 across the top, 4-6 in the middle, etc.)\n')
    print('Loading first game...')

    while True:
        game = TicTacToe()
        while True:
            game.show()
            game.take_turn()
            if game.is_game_over():
                print(f'Player {game.player} wins!')
                break
        play_again = input('Would you like to play again? [y/n] ')

        if play_again == 'n':
            print('Thanks for playing!')
            break

