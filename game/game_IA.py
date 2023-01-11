import random
DEFAULT_CHAR='#'
PLAYER1_CHAR='X'
PLAYER2_CHAR='O'
WINCOND = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

POSSIBLE_KEYS= [str(i) for i in range(1,10)]

def writeboard(board):
    print(f"{' '.join(map(str , board[:3]))}\n{' '.join(map(str , board[3:6]))}\n{' '.join(map(str , board[6:]))}")


def swap(player):
    return PLAYER2_CHAR if player==PLAYER1_CHAR else PLAYER1_CHAR

def checkwin(board):
    for i in WINCOND:
        if board[i[0]]==board[i[1]]==board[i[2]]!=DEFAULT_CHAR:
            return board[i[0]]
    return None

def checkdraw(board):
    return DEFAULT_CHAR not in board

def ia_choice_random(board):
    print('IA plays: Hahaha I am very very smart IA')
    return random.choice([i for i in range(9) if board[i]==DEFAULT_CHAR])

def coinflip():
    return random.choice([PLAYER1_CHAR, PLAYER2_CHAR])

def play_again():
    restart= input('Play again (Y/N)?: ').upper()
    if restart == 'Y':
        return True
    elif restart == 'N':
        return False
    elif restart != 'Y' or 'N':
        print('Yes or No (Y/N)?: ')
        return play_again()

def main():
    print('New Tic Tac Toe!')
    board = [DEFAULT_CHAR]*9
    player = coinflip()
    while True:
        winner = checkwin(board)
        if winner:
            print(f'Player {winner} Wins!')
            print(winner==PLAYER1_CHAR and 'You Win!' or 'You Lose!')
            if not play_again():
                break
            main()
        elif checkdraw(board):
            print('Draw!')
            if not play_again():
                break
            main()
        elif player == PLAYER2_CHAR:
            key = ia_choice_random(board)
        else:
            key = input(f'Player {player} to play (Between 1-9): ')
            if key not in POSSIBLE_KEYS or board[int(key)-1] != DEFAULT_CHAR:
                print('Please enter a legal move')
                continue
        board[int(key)-1] = player
        player = swap(player)
        writeboard(board)

main()