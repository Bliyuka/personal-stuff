board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ',
10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ',
19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ',
28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ',
37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ',
46: ' ', 47: ' ', 48: ' ', 49: ' ', 50: ' ', 51: ' ', 52: ' ', 53: ' ', 54: ' ',
55: ' ', 56: ' ', 57: ' ', 58: ' ', 59: ' ', 60: ' ', 61: ' ', 62: ' ', 63: ' ',
64: ' ', 65: ' ', 66: ' ', 67: ' ', 68: ' ', 69: ' ', 70: ' ', 71: ' ', 72: ' ',
73: ' ', 74: ' ', 75: ' ', 76: ' ', 77: ' ', 78: ' ', 79: ' ', 80: ' ', 81: ' ',
}

p1 = 'X'
p2 = 'O'

def printBoard(board):
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " || " + board[4] + " | " + board[5] + " | " + board[6] + " || " + board[7] + " | " + board[8] + " | " + board[9] + " |" + "   1  2  3  4  5  6  7  8  9")
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[10] + " | " + board[11] + " | " + board[12] + " || " + board[13] + " | " + board[14] + " | " + board[15] + " || " + board[16] + " | " + board[17] + " | " + board[18] + " |" + "  10 11 12 13 14 15 16 17 18")   
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[19] + " | " + board[20] + " | " + board[21] + " || " + board[22] + " | " + board[23] + " | " + board[24] + " || " + board[25] + " | " + board[26] + " | " + board[27] + " |" + "  19 20 21 22 23 24 25 26 27")   
    print("|===========||===========||===========|          +        +")
    print("| " + board[28] + " | " + board[29] + " | " + board[30] + " || " + board[31] + " | " + board[32] + " | " + board[33] + " || " + board[34] + " | " + board[35] + " | " + board[36] + " |" + "  28 29 30 31 32 33 34 35 36")   
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[37] + " | " + board[38] + " | " + board[39] + " || " + board[40] + " | " + board[41] + " | " + board[42] + " || " + board[43] + " | " + board[44] + " | " + board[45] + " |" + "  37 38 39 40 41 42 43 44 45")   
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[46] + " | " + board[47] + " | " + board[48] + " || " + board[49] + " | " + board[50] + " | " + board[51] + " || " + board[52] + " | " + board[53] + " | " + board[54] + " |" + "  46 47 48 49 50 51 52 53 54")   
    print("|===========||===========||===========|          +        +")
    print("| " + board[55] + " | " + board[56] + " | " + board[57] + " || " + board[58] + " | " + board[59] + " | " + board[60] + " || " + board[61] + " | " + board[62] + " | " + board[63] + " |" + "  55 56 57 58 59 60 61 62 63")   
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[64] + " | " + board[65] + " | " + board[66] + " || " + board[67] + " | " + board[68] + " | " + board[69] + " || " + board[70] + " | " + board[71] + " | " + board[72] + " |" + "  64 65 66 67 68 69 70 71 72")   
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[73] + " | " + board[74] + " | " + board[75] + " || " + board[76] + " | " + board[77] + " | " + board[78] + " || " + board[79] + " | " + board[80] + " | " + board[81] + " |" + "  73 74 75 76 77 78 79 80 81")   
# printBoard(board)

def spaceIsFree(position):
    if board[position] == ' ':
        return True
    return False

def makeMove(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("DRAW!")
            exit()
        if checkWinBig():
            if letter == 'X':
                print("player 1 WINS!")
                exit()
            else:
                print("player 2 WINS!")
                exit()
            # HELP??????????????????????????????
        return
    else:
        print("INVALID POSITION")
        position = int(input("ENTER A NEW POSITION: "))
        makeMove(letter, position)
        return

def checkWinSmall():
    # ngang 1
    if board[1] == board[2] == board[3] and board[1] != ' ': return True
    elif board[10] == board[11] == board[12] and board[10] != ' ': return True
    elif board[19] == board[20] == board[21] and board[19] != ' ': return True
    # doc 1
    elif board[1] == board[10] == board[19] and board[1] != ' ': return True
    elif board[2] == board[11] == board[20] and board[2] != ' ': return True
    elif board[3] == board[12] == board[21] and board[3] != ' ': return True
    # cheo 1
    elif board[1] == board[11] == board[21] and board[1] != ' ': return True
    elif board[3] == board[11] == board[19] and board[3] != ' ': return True
    # done
    
    # ngang 2
    elif board[4] == board[5] == board[6] and board[4] != ' ': return True
    elif board[13] == board[14] == board[15] and board[13] != ' ': return True
    elif board[22] == board[23] == board[24] and board[22] != ' ': return True
    # doc 2
    elif board[4] == board[13] == board[22] and board[4] != ' ': return True
    elif board[5] == board[14] == board[23] and board[5] != ' ': return True
    elif board[6] == board[15] == board[24] and board[6] != ' ': return True
    # cheo 2
    elif board[4] == board[14] == board[24] and board[4] != ' ': return True
    elif board[6] == board[14] == board[22] and board[6] != ' ': return True
    # done
    
    # ngang 3
    elif board[7] == board[8] == board[9] and board[7] != ' ': return True
    elif board[16] == board[17] == board[18] and board[18] != ' ': return True
    elif board[25] == board[26] == board[27] and board[27] != ' ': return True
    # doc 3
    elif board[7] == board[16] == board[25] and board[25] != ' ': return True
    elif board[8] == board[17] == board[26] and board[26] != ' ': return True
    elif board[9] == board[18] == board[27] and board[27] != ' ': return True
    # cheo 3
    elif board[7] == board[17] == board[27] and board[27] != ' ': return True
    elif board[9] == board[17] == board[25] and board[25] != ' ': return True
    # done
    
    # ngang 4
    elif board[28] == board[29] == board[30] and board[30] != ' ': return True
    elif board[37] == board[38] == board[39] and board[39] != ' ': return True
    elif board[46] == board[47] == board[48] and board[48] != ' ': return True
    # doc 4
    elif board[28] == board[37] == board[46] and board[46] != ' ': return True
    elif board[29] == board[38] == board[47] and board[47] != ' ': return True
    elif board[30] == board[39] == board[48] and board[48] != ' ': return True
    # cheo 4
    elif board[28] == board[38] == board[48] and board[48] != ' ': return True
    elif board[30] == board[38] == board[46] and board[46] != ' ': return True
    # done
    
    # ngang 5
    elif board[31] == board[32] == board[33] and board[33] != ' ': return True
    elif board[40] == board[41] == board[42] and board[42] != ' ': return True
    elif board[49] == board[50] == board[51] and board[51] != ' ': return True
    # doc 5
    elif board[31] == board[40] == board[49] and board[49] != ' ': return True
    elif board[32] == board[41] == board[50] and board[50] != ' ': return True
    elif board[33] == board[42] == board[51] and board[51] != ' ': return True
    # cheo 5
    elif board[31] == board[41] == board[51] and board[51] != ' ': return True
    elif board[33] == board[41] == board[49] and board[49] != ' ': return True
    # done
    
    # ngang 6
    elif board[34] == board[35] == board[36] and board[36] != ' ': return True
    elif board[43] == board[44] == board[45] and board[45] != ' ': return True
    elif board[52] == board[53] == board[54] and board[54] != ' ': return True
    # doc 6
    elif board[34] == board[43] == board[52] and board[52] != ' ': return True
    elif board[35] == board[44] == board[53] and board[53] != ' ': return True
    elif board[36] == board[45] == board[54] and board[54] != ' ': return True
    # cheo 6
    elif board[34] == board[44] == board[54] and board[54] != ' ': return True
    elif board[36] == board[44] == board[52] and board[52] != ' ': return True
    # done
    
    # ngang 7
    elif board[55] == board[56] == board[57] and board[57] != ' ': return True
    elif board[64] == board[65] == board[66] and board[66] != ' ': return True
    elif board[73] == board[74] == board[75] and board[75] != ' ': return True
    # doc 7
    elif board[55] == board[64] == board[73] and board[73] != ' ': return True
    elif board[56] == board[65] == board[74] and board[74] != ' ': return True
    elif board[57] == board[66] == board[75] and board[75] != ' ': return True
    # cheo 7
    elif board[55] == board[65] == board[75] and board[75] != ' ': return True
    elif board[57] == board[65] == board[73] and board[73] != ' ': return True
    # done
    
    # ngang 8
    elif board[58] == board[59] == board[60] and board[60] != ' ': return True
    elif board[67] == board[68] == board[69] and board[69] != ' ': return True
    elif board[76] == board[77] == board[78] and board[78] != ' ': return True
    # doc 8
    elif board[58] == board[67] == board[76] and board[76] != ' ': return True
    elif board[59] == board[68] == board[77] and board[77] != ' ': return True
    elif board[60] == board[69] == board[78] and board[78] != ' ': return True
    # cheo 8
    elif board[58] == board[68] == board[78] and board[78] != ' ': return True
    elif board[60] == board[68] == board[76] and board[76] != ' ': return True
    # done
    
    # ngang 9
    elif board[61] == board[62] == board[63] and board[63] != ' ': return True
    elif board[70] == board[71] == board[12] and board[72] != ' ': return True
    elif board[79] == board[80] == board[81] and board[81] != ' ': return True
    # doc 9
    elif board[61] == board[70] == board[79] and board[79] != ' ': return True
    elif board[62] == board[71] == board[80] and board[80] != ' ': return True
    elif board[63] == board[72] == board[81] and board[81] != ' ': return True
    # cheo 9
    elif board[61] == board[71] == board[81] and board[81] != ' ': return True
    elif board[63] == board[71] == board[79] and board[79] != ' ': return True
    
    else: return False

def checkWinBig():
    # ngang 1
    if board[11] == board[14] == board[17] and board[17] != ' ': return True
    elif board[38] == board[41] == board[44] and board[44] != ' ': return True
    elif board[65] == board[68] == board[71] and board[71] != ' ': return True
    # doc 1
    elif board[11] == board[38] == board[65] and board[65] != ' ': return True
    elif board[14] == board[41] == board[68] and board[68] != ' ': return True
    elif board[17] == board[44] == board[71] and board[71] != ' ': return True
    # cheo 1
    elif board[11] == board[41] == board[71] and board[71] != ' ': return True
    elif board[17] == board[41] == board[65] and board[65] != ' ': return True
    
def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def player1move():
    position = int(input("ENTER A POSITION FOR 'X': "))
    makeMove(p1, position)
    return

def player2move():
    position = int(input("ENTER A POSITION FOR 'X': "))
    makeMove(p2, position)
    return

while not checkWinBig():
    player1move()
    player2move()