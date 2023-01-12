import random

DEFAULT_CHAR='#'
PLAYER1_CHAR='X'
PLAYER2_CHAR='O'
board=[[DEFAULT_CHAR for i in range(3)] for j in range(3)]
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
    for row in board:
        print(' '.join(row))

def swap(player):
    return PLAYER2_CHAR if player==PLAYER1_CHAR else PLAYER1_CHAR

def checkwin(board):
    for i in WINCOND:
        if board[i[0]//3][i[0]%3]==board[i[1]//3][i[1]%3]==board[i[2]//3][i[2]%3]!=DEFAULT_CHAR:
            return board[i[0]//3][i[0]%3]
    return None

def checkdraw(board):
    for row in board:
        if DEFAULT_CHAR in row:
            return False
    return True

def coinflip():
    return random.choice([PLAYER1_CHAR, PLAYER2_CHAR])

def play_again():
    restart= input('Play again (Y/N)?: ').upper()
    if restart == 'Y':
        return True
    elif restart == 'N':
        return False
    else:
        print('Please enter Y or N')
        return play_again()


def main():
    print('New Tic Tac Toe!')
    board = [[DEFAULT_CHAR for i in range(3)] for j in range(3)]
    player = coinflip()
    while True:
        winner = checkwin(board)
        if winner:
            print(f'Player {winner} Wins!')
            if winner==PLAYER1_CHAR:
                print("You Win!")
            else:
                print("You Lose!")
            if not play_again():
                break
            main()
        elif checkdraw(board):
            print('Draw!')
            if not play_again():
                break
            main()
        if player==PLAYER2_CHAR:
            IA_turn()
        key = input(f'Player {player} to play (Between 1-9): ')
        if key not in POSSIBLE_KEYS or board[(int(key)-1)//3][(int(key)-1)%3] != DEFAULT_CHAR:
            print('Please enter a legal move')
            continue
        board[(int(key)-1)//3][(int(key)-1)%3] = player
        player = swap(player)
        writeboard(board)

def IA_turn():
    key = random.choice([i for i in range(1,10) if board[(int(key)-1)//3][(int(key)-1)%3] == DEFAULT_CHAR])
    board[(int(key)-1)//3][(int(key)-1)%3] = player
    player = swap(player)
    writeboard(board)

if __name__ == '__main__':
    main()