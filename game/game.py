import random

DEFAULT_CHAR='#'
PLAYER1_CHAR='X'
PLAYER2_CHAR='O'
WINCOND = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
POSSIBLE_KEYS= [str(i) for i in range(1,10)]

def write_board(board):
    print(f"{' '.join(map(str , board[:3]))}\n{' '.join(map(str , board[3:6]))}\n{' '.join(map(str , board[6:]))}")

def swap(player):
    return PLAYER2_CHAR if player==PLAYER1_CHAR else PLAYER1_CHAR

def check_win(board):
    for i in WINCOND:
        if board[i[0]]==board[i[1]]==board[i[2]]!=DEFAULT_CHAR:
            return board[i[0]]
    return None

def coin_flip():
    return random.choice([PLAYER1_CHAR, PLAYER2_CHAR])

def ia_choice(board):
    return random.choice([i for i in range(1,10) if board[i]==DEFAULT_CHAR])

def check_draw(board):
    return DEFAULT_CHAR not in board

def play_again():
    restart= input('Play again (Y/N)?: ').upper()
    if restart == 'Y':
        return True
    elif restart == 'N':
        return False
    else:
        print('Please enter Y or N')
        return play_again()

def play_turn(board, player):
    key = input(f'Player {player} to play (Between 1-9): ')
    if key not in POSSIBLE_KEYS or board[int(key)-1] != DEFAULT_CHAR:
        print('Please enter a legal move')
        play_turn(board, player)
    board[int(key)-1] = player
    write_board(board)

def ia_turn(board, player):
    key = ia_choice(board)
    board[int(key)-1] = player
    write_board(board)

def main():
    print('New Tic Tac Toe!')
    board = [DEFAULT_CHAR]*9
    player=PLAYER1_CHAR
    while True:
        winner=check_win(board)
        if winner:
            print(f'Player {winner} Wins!')
            if play_again():
                main()
            else:
                break
        elif check_draw(board):
            print('Draw!')
            if play_again():
                main()
            else:
                break
        if player==PLAYER1_CHAR:
            ia_turn(board, player)
        play_turn(board, player)
        player = swap(player)

main()