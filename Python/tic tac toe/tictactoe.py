import random

board = ["-","-","-",
        "-","-","-",
        "-","-","-",]

currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board 
def printBoard(board):
    print(" ___________")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |" + "  1  2  3")
    print("|---|---|---|")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |" + "  4  5  6")
    print("|---|---|---|")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |" + "  7  8  9")

# take player input
def playerInput(board):
    while True:
        inp = int(input("Enter a number 1-9: "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer
            break
        else:
            printBoard(board)
            print("\nyou dump fuck\n")

# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("\nT I E\n")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        printBoard(board)
        print(f"\n{winner} is the WINNER\n")
        gameRunning = False


# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

# check for win or tie again


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    if gameRunning == False:
        break
    else:
        switchPlayer()
        computer(board)
        checkWin()
        checkTie(board)