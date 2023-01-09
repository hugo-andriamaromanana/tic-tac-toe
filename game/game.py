board = ["#"]*9
wincond = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
gamestate=False

def writeboard(board):

    print(f"{' '.join(map(str , board[:3]))}\n{' '.join(map(str , board[3:6]))}\n{' '.join(map(str , board[6:]))}")

def checkwin(combs,check):
    for i in combs:
        points=0
        for j in i:
            if check[j]=='O':
                points+=1
            if check[j]=='X':
                points+=1
        if points==3:
            print('Yes')
            if i==['X','X','X']:
                print('Wow! Player1 Wins!')
            if i==['O','O','O']:
                print('Wow! Player2 Wins!')
            return True
        if "#" not in board:
            print('Draw!')
            return True
    return False
        
while gamestate == False:

    validmove1=False
    validmove2=False

    print('Player1 ~X~ to play')
    play= int(input('Please select a position [0-8] to play: '))
    while validmove1==False:
        while board[play]!="#":
            print('WARNING! Please enter a position that was not already played')
            play= int(input('Please select a position [0-8] to play: '))
        board[play]='X'
        validmove1=True
    writeboard(board)

    gamestate=checkwin(wincond,board)
    if gamestate==True:
        break

    print('Player2 ~O~ to play')
    play= int(input('Please select a position [0-8] to play: '))
    while validmove2==False:
        while board[play]!="#":
            print('WARNING! Please enter a position that was not already played')
            play= int(input('Please select a position [0-8] to play: '))
        board[play]='O'
        validmove2=True
    writeboard(board)
    gamestate=checkwin(wincond,board)