import time

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player = 'O'
computer = 'X'

def printBoard(board):
    print(" ___________")
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |" + "  1  2  3")
    print("|---|---|---|")
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |" + "  4  5  6")
    print("|---|---|---|")
    print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |" + "  7  8  9")

def spaceIsFree(position):
    if board[position] == ' ':
        return True
    return False

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("DRAW!")
            exit()
        if checkWin():
            if letter == 'X':
                print("BOT WINS!")
                exit()
            else:
                print("PLAYER WINS!")
                exit()
        return
    else:
        print("INVALID POSITION")
        position = int(input("ENTER A NEW POSITION: "))
        insertLetter(letter, position)
        return

def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def playerMove():
    position = int(input("ENTER A POSITION FOR 'O': "))
    insertLetter(player, position)
    return

def compMove():
    print("BOT MOVES")
    time.sleep(1)
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter(computer, bestMove)
    return

def minimax(board, isMaximizing):
    if checkWhichMarkWon(computer):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


label = ("""
who go first?
1) PLAYER
2) BOT
ENTER: """)


while True:
    user = int(input(label))
    if user == 1:
        printBoard(board)
        while not checkWin():
            playerMove()
            compMove()
    elif user == 2:
        while not checkWin():
            compMove()
            playerMove()
    else:
        user = int(input("ENTER 1 OR 2 YOU DUMP FUCK: "))