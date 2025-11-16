import numpy as np

board = np.zeros((3,3),dtype=int)


def check_winner(board):
    if 3 in np.sum(board,axis=0) or 3 in np.sum(board,axis=1) or np.trace(board)==3 or np.trace(np.fliplr(board)) == 3:
        return 'X won the game'
    if -3 in np.sum(board,axis=0)  or -3 in np.sum(board,axis=1) or np.trace(np.fliplr(board)) == -3 or np.trace(board)==-3:
        return 'O won the game!'
    if not 0 in board:
        return "DRAW"
    else:
        return None

current = 1
print("Lets start the game!!")

while True:
    if current == 1:
        player = 'X'
    else:
        player = 'O'
    
    try:
        print(f"Its turn of player {player}")
        row = int(input("Enter the row number (0,1,2): "))
        col = int(input("Enter the column number (0,1,2): "))
        if row not in [0,1,2] or col not in [0,1,2]:
            print("Enter the rows and col between 0 and 2 only")
            continue
    except ValueError:
        print("Enter only numbers!!")
        continue

    if board[row,col] == 0 and player == 'X':
        board[row,col] = 1
        result = check_winner(board)
        if result is not None:
            print(result)
            break
        current = 0
    elif board[row,col] == 0 and player == 'O':
        board[row,col] = -1
        result = check_winner(board)
        if result is not None:
            print(result)
            break
        current = 1
    else:
        print("Space occupied!")
        continue
        

        