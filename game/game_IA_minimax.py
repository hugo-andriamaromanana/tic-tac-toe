from math import inf as infinity
from random import choice
import platform
from os import system

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    return [player, player, player] in win_state


def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    cells = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells


def valid_move(x, y):
    return [x, y] in empty_cells(board)


def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]
    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]
    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score
    return best


def clear_term():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, computer_char, human_char):
    chars = {
        -1: human_char,
        +1: computer_char,
        0: ' '
    }
    sep = '---------------'

    print('\n' + sep)
    for row in reversed(state):
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + sep)


def ai_turn(computer_char, human_char):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clear_term()
    print(f'Computer turn [{computer_char}]')
    render(board, computer_char, human_char)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)


def human_turn(computer_char, human_char):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clear_term()
    print(f'[{human_char}] to move.')
    render(board, computer_char, human_char)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move, you stoopid')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('\nBye ragequitter')
            exit()
        except (KeyError, ValueError):
            print('Bro cant you read?')


def main():
    clear_term()
    human_char = ''  
    computer_char = '' 
    first = '' 
    while human_char != 'O' and human_char != 'X':
        try:
            print('')
            human_char = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Rly? Try again.')

    if human_char == 'X':
        computer_char = 'O'
    else:
        computer_char = 'X'
    clear_term()
    while first != 'Y' and first != 'N':
        try:
            first = input('Are you confident enough to let me start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Thats a yes/no question, are you stupid?')
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'Y':
            ai_turn(computer_char, human_char)
            first = ''

        human_turn(computer_char, human_char)
        ai_turn(computer_char, human_char)

    if wins(board, HUMAN):
        clear_term()
        print(f'Your turn insect [{human_char}]')
        render(board, computer_char, human_char)
        print('IF you can read that, you cheated!')
    elif wins(board, COMP):
        clear_term()
        print(f'My turn [{computer_char}]')
        render(board, computer_char, human_char)
        print('ez')
    else:
        clear_term()
        render(board, computer_char, human_char)
        print('Nigger')

    exit()


if __name__ == '__main__':
    main()
