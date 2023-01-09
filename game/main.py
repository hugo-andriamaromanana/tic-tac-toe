import curses

POSSIBLE_KEYS = [ord(str(i)) for i in range(1, 10)]

DEFAULT_CHAR = "#"
X_CHAR = "X"
O_CHAR = "O"

COMBS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


def write_board(stdscr, board):
    line = 0
    for i in range(2, -1, -1):
        stdscr.addstr(line+1, 0, " ".join(board[i*3:(i+1)*3]))
        line += 1


def check_win(board):
    for comb in COMBS:
        if board[comb[0]] == board[comb[1]] == board[comb[2]] != DEFAULT_CHAR:
            return board[comb[0]]
    return None


def swap_player(player): return O_CHAR if player == X_CHAR else X_CHAR


def main():
    stdscr = curses.initscr()
    curses.curs_set(0)
    board = [DEFAULT_CHAR]*9
    player = "X"
    while True:
        write_board(stdscr, board)
        winner = check_win(board)

        if winner:
            stdscr.addstr(5, 0, f"Player {winner} wins!\n")
            stdscr.refresh()
            break

        player = swap_player(player)
        stdscr.addstr(5, 0, f"Player {player} turn: ")
        stdscr.refresh()

        key = stdscr.getch()

        if key == ord("q"):
            stdscr.addstr(5, 0, "Bye bye!\n")
            stdscr.refresh()
            break

        if key in POSSIBLE_KEYS and board[key - 49] == DEFAULT_CHAR:
            board[key - 49] = player
        else:
            player = swap_player(player)
            stdscr.refresh()


main()