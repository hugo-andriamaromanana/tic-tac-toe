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

def main():
    board = [DEFAULT_CHAR]*9
    player=PLAYER1_CHAR
    while True:
        winner=checkwin(board)
        if winner:
            print(f'Player {winner} Wins!')
            break
        if checkdraw(board):
            print('Draw!')
            break
        key= input(f'Player {player} to play (Between 1-9): ')
        if key not in POSSIBLE_KEYS:
            print('Please enter a number between 1-9')
            continue
        if board[int(key)-1]!=DEFAULT_CHAR:
            print('Please enter a legal move')
            continue
        board[int(key)-1]=player
        player=swap(player)
        writeboard(board)

main()

