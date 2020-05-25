import sys

# Declare a variable called board which would houses the X and O markers
board = [["", "", ""], ["", "", ""], ["", "", ""]]

#Declara a variable exampleBoard which serves as an example of a board at the beginning instance of the game
exampleBoard = [[1,2,3], [4,5,6], [7,8,9]]

#Declare an int variable which lets us know if the game is won or not. This helps when we want to call the rematch function.
gameWon = 0

#This function displays the board as is at that moment in time
def displayBoard():
    global board
    print (board[0][0]," |",board[0][1],"  |", board[0][2])
    print ('------------')
    print (board[1][0]," |",board[1][1],"  |", board[1][2])
    print ('------------')
    print (board[2][0]," |",board[2][1],"  |", board[2][2])

#This function takes in player 1's input, that is the position the player wants the marker on
def playerInput():
    global board
    global marker

    print("Hey, Player One - X", "\n")

    marker = "X"
    row = int(input("Which row do you want to play on?(1-3): "))
    col = int(input("Which column do you want to play on?(1-3): "))

    if board[row - 1][col - 1] == "":
        board[row - 1][col -1] = marker
    else:
        print("That position is occupied, kindly pick another")
        playerInput()

#This function takes in player 2's input, that is the position the player wants the marker on
def playerTwoInput():
    global board
    global marker

    print("Hey, Player Two - O", "\n")
    marker = "O"
    row = int(input("Which row do you want to play on?(1-3): "))
    col = int(input("Which column do you want to play on?(1-3): "))

    if board[row - 1][col - 1] == "":
        board[row - 1][col -1] = marker
    else:
        print("That position is occupied, kindly pick another")
        playerTwoInput()

#This function determines whether there would be a rematch or not
def rematch():
    global board
    global gameWon
    ans = input("Do you want to play another match? Y or N: ")
    if ans == "Y" or ans == "y":
        board = [["", "", ""], ["", "", ""], ["", "", ""]]

        gameWon = 0
        runCode()
    else: 
        print("Thanks for playing!")

#This function checks whether a game has been won or not
def checkGameStatus():
    global board
    global gameWon
    if board[0][0] == board[1][1] == board[2][2] == marker or board[0][2] == board[1][1] == board[2][0] == marker:
        gameWon = 1
        print("{playerI} is the winner!".format(playerI = marker))

        rematch()
        sys.exit()
    elif board[0][0] == board[0][1] == board[0][2] == marker or board[0][1] == board[1][1] == board[2][1] == marker:
        gameWon = 1
        print("{playerI} is the winner!".format(playerI = marker))
        rematch()
        sys.exit()
    elif board[1][0] == board[1][1] == board[1][2] == marker or board[2][0] == board[2][1] == board[2][2] == marker:
        gameWon = 1
        print("{playerI} is the winner!".format(playerI = marker))
        rematch()
        sys.exit()
    elif board[0][0] == board[1][0] == board[2][0] == marker or board[0][2] == board[1][2] == board[2][2] == marker:
        gameWon = 1
        print("{playerI} is the winner!".format(playerI = marker))
        rematch()
        sys.exit()

    return

#This function is the holy grail, it runs the game.
def runCode():
    x = 0

    while x < 4:
        playerInput()
        displayBoard()
        checkGameStatus()
        playerTwoInput()
        displayBoard()
        checkGameStatus()

        x += 1
    if gameWon == 0:
        playerInput()
        displayBoard()
        checkGameStatus()
    print("It's a tie. ")
    rematch()

print("This is a sample board with three rows and three columns. ")

print (exampleBoard[0][0]," |",exampleBoard[0][1],"  |", exampleBoard[0][2])
print ('------------')
print (exampleBoard[1][0]," |",exampleBoard[1][1],"  |", exampleBoard[1][2])
print ('------------')
print (exampleBoard[2][0]," |",exampleBoard[2][1],"  |", exampleBoard[2][2])
runCode()






























