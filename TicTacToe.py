import sys

# Declare a variable called board which would house the marker

board = [["", "", ""], ["", "", ""], ["", "", ""]]

exampleBoard = [[1,2,3], [4,5,6], [7,8,9]]

#This function displays the board as is at that moment in time
def displayBoard():
    global board
    for row in range(len(board)):
        print(board[row])

    # print (board[0][0]," |",board[0][1],"  |", board[0][2])
    # print ('------------')
    # print (board[1][0]," |",board[1][1],"  |", board[1][2])
    # print ('------------')
    # print (board[2][0]," |",board[2][1],"  |", board[2][2])

def playerInput():
    global board
    global marker

    marker = input("What character do you want to use?: ").upper()
    row = int(input("Which row do you want to play on?(1-3): "))
    col = int(input("Which column do you want to play on?(1-3): "))
    if board[row - 1][col - 1] == "":
        board[row - 1][col -1] = marker
    else:
        print("That position is occupied, kindly pick another")
        playerInput()

def checkGameStatus():
    global board
    if board[0][0] == board[1][1] == board[2][2] == marker or board[0][2] == board[1][1] == board[2][0] == marker:
        print("{playerI} is the winner!".format(playerI = marker))
        sys.exit()
    elif board[0][0] == board[0][1] == board[0][2] == marker or board[0][1] == board[1][1] == board[2][1] == marker:
        print("{playerI} is the winner!".format(playerI = marker))
        sys.exit()
    elif board[1][0] == board[1][1] == board[1][2] == marker or board[2][0] == board[2][1] == board[2][2] == marker:
        print("{playerI} is the winner!".format(playerI = marker))
        sys.exit()

    return

def runCode():
    x = 0

    while x < 9:
        playerInput()
        displayBoard()
        checkGameStatus()

        x += 1
    
    print("It's a tie. ")

print("This is a sample board with three rows and three columns. ")

for row in range(len(exampleBoard)):
        print(exampleBoard[row])
# print (exampleBoard[0][0]," |",exampleBoard[0][1],"  |", exampleBoard[0][2])
# print ('------------')
# print (exampleBoard[1][0]," |",exampleBoard[1][1],"  |", exampleBoard[1][2])
# print ('------------')
# print (exampleBoard[2][0]," |",exampleBoard[2][1],"  |", exampleBoard[2][2])
runCode()




























