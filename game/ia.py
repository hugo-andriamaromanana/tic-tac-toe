import random
DEFAULT_CHAR='#'
def ia_choice(board):
    return random.choice([i for i in range(9) if board[i]==DEFAULT_CHAR])