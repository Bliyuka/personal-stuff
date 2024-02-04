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
preMove = 0
list = []

def printBoard(board):
    print("======================================= +        +        +        +")
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " || " + board[4] + " | " + board[5] + " | " + board[6] + " || " + board[7] + " | " + board[8] + " | " + board[9] + " |" + "   1  2  3  4  5  6  7  8  9")
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[10] + " | " + board[11] + " | " + board[12] + " || " + board[13] + " | " + board[14] + " | " + board[15] + " || " + board[16] + " | " + board[17] + " | " + board[18] + " |" + "  10 11 12 13 14 15 16 17 18")   
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[19] + " | " + board[20] + " | " + board[21] + " || " + board[22] + " | " + board[23] + " | " + board[24] + " || " + board[25] + " | " + board[26] + " | " + board[27] + " |" + "  19 20 21 22 23 24 25 26 27")   
    print("|===========||===========||===========| +        +        +        +")
    print("| " + board[28] + " | " + board[29] + " | " + board[30] + " || " + board[31] + " | " + board[32] + " | " + board[33] + " || " + board[34] + " | " + board[35] + " | " + board[36] + " |" + "  28 29 30 31 32 33 34 35 36")   
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[37] + " | " + board[38] + " | " + board[39] + " || " + board[40] + " | " + board[41] + " | " + board[42] + " || " + board[43] + " | " + board[44] + " | " + board[45] + " |" + "  37 38 39 40 41 42 43 44 45")   
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[46] + " | " + board[47] + " | " + board[48] + " || " + board[49] + " | " + board[50] + " | " + board[51] + " || " + board[52] + " | " + board[53] + " | " + board[54] + " |" + "  46 47 48 49 50 51 52 53 54")   
    print("|===========||===========||===========| +        +        +        +")
    print("| " + board[55] + " | " + board[56] + " | " + board[57] + " || " + board[58] + " | " + board[59] + " | " + board[60] + " || " + board[61] + " | " + board[62] + " | " + board[63] + " |" + "  55 56 57 58 59 60 61 62 63")   
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[64] + " | " + board[65] + " | " + board[66] + " || " + board[67] + " | " + board[68] + " | " + board[69] + " || " + board[70] + " | " + board[71] + " | " + board[72] + " |" + "  64 65 66 67 68 69 70 71 72")   
    print("|---|---|---||---|---|---||---|---|---|")
    print("| " + board[73] + " | " + board[74] + " | " + board[75] + " || " + board[76] + " | " + board[77] + " | " + board[78] + " || " + board[79] + " | " + board[80] + " | " + board[81] + " |" + "  73 74 75 76 77 78 79 80 81")   
    print("======================================= +        +        +        +")
# printBoard(board)

def spaceIsFree(position):
    if board[position] == ' ':
        return True
    return False

def checkMove(position, letter):
    global preMove
    if preMove == 1 or preMove == 4 or preMove == 7 or preMove == 28 or preMove == 31 or preMove == 34 or preMove == 55 or preMove == 58 or preMove == 61:
        if position == 1 or position == 2 or position == 3 or position == 10 or position == 11 or position == 12 or position == 19 or position == 20 or position == 21:
            return True
        elif 1 in list: 
            return True
        else: return False 


    elif preMove == 2 or preMove ==5 or preMove == 8 or preMove == 29 or preMove == 32 or preMove == 35 or preMove == 56 or preMove == 59 or preMove == 62:
        if position == 4 or position == 5 or position == 6 or position == 13 or position == 14 or position == 15 or position == 22 or position == 23 or position == 24:
            return True
        elif 2 in list: 
            return True
        else: return False 


    elif preMove == 3 or preMove == 6 or preMove == 9 or preMove == 30 or preMove == 33 or preMove == 36 or preMove == 57 or preMove == 60 or preMove == 63:
        if position == 7 or position == 8 or position == 9 or position == 16 or position == 17 or position == 18 or position == 25 or position == 26 or position == 27:
            return True
        elif 3 in list: 
            return True
        else: return False 


    elif preMove == 10 or preMove == 13 or preMove == 16 or preMove == 37 or preMove == 40 or preMove == 43 or preMove == 64 or preMove == 67 or preMove == 70:
        if position == 28 or position == 29 or position == 30 or position == 37 or position == 38 or position == 39 or position == 46 or position == 47 or position == 48:
            return True
        elif 4 in list: 
            return True
        else: return False 


    elif preMove == 11 or preMove == 14 or preMove == 17 or preMove == 38 or preMove == 41 or preMove == 44 or preMove == 65 or preMove == 68 or preMove == 71:
        if position == 31 or position == 32 or position == 33 or position == 40 or position == 41 or position == 42 or position == 49 or position == 50 or position == 51:
            return True
        elif 5 in list: 
            return True
        else: return False 


    elif preMove == 12 or preMove == 15 or preMove == 18 or preMove == 39 or preMove == 42 or preMove == 45 or preMove == 66 or preMove == 69 or preMove == 72:
        if position == 34 or position == 35 or position == 36 or position == 43 or position == 44 or position == 45 or position == 52 or position == 53 or position == 54:
            return True
        elif 6 in list: 
            return True
        else: return False 


    elif preMove == 19 or preMove == 22 or preMove == 25 or preMove == 46 or preMove == 49 or preMove == 52 or preMove == 73 or preMove == 76 or preMove == 79:
        if position == 55 or position == 56 or position == 57 or position == 64 or position == 65 or position == 66 or position == 73 or position == 74 or position == 75:
            return True
        elif 7 in list: 
            return True
        else: return False 


    elif preMove == 20 or preMove == 23 or preMove == 26 or preMove == 47 or preMove == 50 or preMove == 53 or preMove == 74 or preMove == 77 or preMove == 80:
        if position == 58 or position == 59 or position == 60 or position == 67 or position == 68 or position == 69 or position == 76 or position == 77 or position == 78:
            return True
        elif 8 in list: 
            return True
        else: return False 


    elif preMove == 21 or preMove == 24 or preMove == 27 or preMove == 48 or preMove == 51 or preMove == 54 or preMove == 75 or preMove == 78 or preMove == 81:
        if position == 61 or position == 62 or position == 63 or position == 70 or position == 71 or position == 72 or position == 78 or position == 80 or position == 81:
            return True
        elif 9 in list: 
            return True
        else: return False 

def makeMove(letter, position):
    global preMove
    if spaceIsFree(position):
        while not checkMove(position, letter):
            if preMove == 0: return False
            elif preMove == 1 or preMove == 4 or preMove == 7 or preMove == 28 or preMove == 31 or preMove == 34 or preMove == 55 or preMove == 58 or preMove == 61:
                print("Your next move is in the TOP LEFT part")
            elif preMove == 2 or preMove ==5 or preMove == 8 or preMove == 29 or preMove == 32 or preMove == 35 or preMove == 56 or preMove == 59 or preMove == 62:
                print("Your next move is in the TOP part")
            elif preMove == 3 or preMove == 6 or preMove == 9 or preMove == 30 or preMove == 33 or preMove == 36 or preMove == 57 or preMove == 60 or preMove == 63:
                print("Your next move is in the TOP RIGHT part")
            elif preMove == 10 or preMove == 13 or preMove == 16 or preMove == 37 or preMove == 40 or preMove == 43 or preMove == 64 or preMove == 67 or preMove == 70:
                print("Your next move is in the LEFT part")
            elif preMove == 11 or preMove == 14 or preMove == 17 or preMove == 38 or preMove == 41 or preMove == 44 or preMove == 65 or preMove == 68 or preMove == 71:
                print("Your next move is in the MIDDLE part")
            elif preMove == 12 or preMove == 15 or preMove == 18 or preMove == 39 or preMove == 42 or preMove == 45 or preMove == 66 or preMove == 69 or preMove == 72:
                print("Your next move is in the RIGHT part")
            elif preMove == 19 or preMove == 22 or preMove == 25 or preMove == 46 or preMove == 49 or preMove == 52 or preMove == 73 or preMove == 76 or preMove == 79:
                print("Your next move is in the BOTTOM LEFT part")
            elif preMove == 20 or preMove == 23 or preMove == 26 or preMove == 47 or preMove == 50 or preMove == 53 or preMove == 74 or preMove == 77 or preMove == 80:
                print("Your next move is in the BOTTOM part")
            elif preMove == 21 or preMove == 24 or preMove == 27 or preMove == 48 or preMove == 51 or preMove == 54 or preMove == 75 or preMove == 78 or preMove == 81:
                print("Your next move is in the BOTTOM RIGHT part")
            position = int(input("Enter again: "))
        board[position] = letter
        checkWinSmall(letter)
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
        preMove = position
        return
    else:
        print("INVALID POSITION")
        position = int(input("ENTER A NEW POSITION: "))
        print("----- ----- -----")
        makeMove(letter, position)
        return

def checkWinSmall(letter):
    # ngang 1
    if board[1] == board[2] == board[3] and board[1] != ' ' and 1 not in list: 
        board[1] = board[2] = board[3] = board[10] = board[11] = board[12] = board[19] = board[20] = board[21] = letter
        list.append(1)
    elif board[10] == board[11] == board[12] and board[10] != ' ' and 1 not in list: 
        board[1] = board[2] = board[3] = board[10] = board[11] = board[12] = board[19] = board[20] = board[21] = letter
        list.append(1)
    elif board[19] == board[20] == board[21] and board[19] != ' ' and 1 not in list: 
        board[1] = board[2] = board[3] = board[10] = board[11] = board[12] = board[19] = board[20] = board[21] = letter
        list.append(1)
    # doc 1
    elif board[1] == board[10] == board[19] and board[1] != ' ' and 1 not in list: 
        board[1] = board[2] = board[3] = board[10] = board[11] = board[12] = board[19] = board[20] = board[21] = letter
        list.append(1)
    elif board[2] == board[11] == board[20] and board[2] != ' ' and 1 not in list: 
        board[1] = board[2] = board[3] = board[10] = board[11] = board[12] = board[19] = board[20] = board[21] = letter
        list.append(1)
    elif board[3] == board[12] == board[21] and board[3] != ' ' and 1 not in list: 
        board[1] = board[2] = board[3] = board[10] = board[11] = board[12] = board[19] = board[20] = board[21] = letter
        list.append(1)
    # cheo 1
    elif board[1] == board[11] == board[21] and board[1] != ' ' and 1 not in list: 
        board[1] = board[2] = board[3] = board[10] = board[11] = board[12] = board[19] = board[20] = board[21] = letter
        list.append(1)
    elif board[3] == board[11] == board[19] and board[3] != ' ' and 1 not in list: 
        board[1] = board[2] = board[3] = board[10] = board[11] = board[12] = board[19] = board[20] = board[21] = letter
        list.append(1)
    # done
    
    # ngang 2
    elif board[4] == board[5] == board[6] and board[4] != ' ' and 2 not in list: 
        board[4] = board[5] = board[6] = board[13] = board[14] = board[15] = board[22] = board[23] = board[24] = letter
        list.append(2)
    elif board[13] == board[14] == board[15] and board[13] != ' ' and 2 not in list: 
        board[4] = board[5] = board[6] = board[13] = board[14] = board[15] = board[22] = board[23] = board[24] = letter
        list.append(2)
    elif board[22] == board[23] == board[24] and board[22] != ' ' and 2 not in list: 
        board[4] = board[5] = board[6] = board[13] = board[14] = board[15] = board[22] = board[23] = board[24] = letter
        list.append(2)
    # doc 2
    elif board[4] == board[13] == board[22] and board[4] != ' ' and 2 not in list: 
        board[4] = board[5] = board[6] = board[13] = board[14] = board[15] = board[22] = board[23] = board[24] = letter
        list.append(2)
    elif board[5] == board[14] == board[23] and board[5] != ' ' and 2 not in list: 
        board[4] = board[5] = board[6] = board[13] = board[14] = board[15] = board[22] = board[23] = board[24] = letter
        list.append(2)
    elif board[6] == board[15] == board[24] and board[6] != ' ' and 2 not in list: 
        board[4] = board[5] = board[6] = board[13] = board[14] = board[15] = board[22] = board[23] = board[24] = letter
        list.append(2)
    # cheo 2
    elif board[4] == board[14] == board[24] and board[4] != ' ' and 2 not in list: 
        board[4] = board[5] = board[6] = board[13] = board[14] = board[15] = board[22] = board[23] = board[24] = letter
        list.append(2)
    elif board[6] == board[14] == board[22] and board[6] != ' ' and 2 not in list: 
        board[4] = board[5] = board[6] = board[13] = board[14] = board[15] = board[22] = board[23] = board[24] = letter
        list.append(2)
    # done
    
    # ngang 3
    elif board[7] == board[8] == board[9] and board[7] != ' ' and 3 not in list: 
        board[7]  = board[8] = board[9] = board[16] = board[17] = board[18] = board[25] = board[26] = board[27] = letter
        list.append(3)
    elif board[16] == board[17] == board[18] and board[18] != ' ' and 3 not in list: 
        board[7]  = board[8] = board[9] = board[16] = board[17] = board[18] = board[25] = board[26] = board[27] = letter
        list.append(3)
    elif board[25] == board[26] == board[27] and board[27] != ' ' and 3 not in list: 
        board[7]  = board[8] = board[9] = board[16] = board[17] = board[18] = board[25] = board[26] = board[27] = letter
        list.append(3)
    # doc 3
    elif board[7] == board[16] == board[25] and board[25] != ' ' and 3 not in list: 
        board[7]  = board[8] = board[9] = board[16] = board[17] = board[18] = board[25] = board[26] = board[27] = letter
        list.append(3)
    elif board[8] == board[17] == board[26] and board[26] != ' ' and 3 not in list: 
        board[7]  = board[8] = board[9] = board[16] = board[17] = board[18] = board[25] = board[26] = board[27] = letter
        list.append(3)
    elif board[9] == board[18] == board[27] and board[27] != ' ' and 3 not in list: 
        board[7]  = board[8] = board[9] = board[16] = board[17] = board[18] = board[25] = board[26] = board[27] = letter
        list.append(3)
    # cheo 3
    elif board[7] == board[17] == board[27] and board[27] != ' ' and 3 not in list: 
        board[7]  = board[8] = board[9] = board[16] = board[17] = board[18] = board[25] = board[26] = board[27] = letter
        list.append(3)
    elif board[9] == board[17] == board[25] and board[25] != ' ' and 3 not in list: 
        board[7]  = board[8] = board[9] = board[16] = board[17] = board[18] = board[25] = board[26] = board[27] = letter
        list.append(3)
    # done
    
    # ngang 4
    elif board[28] == board[29] == board[30] and board[30] != ' ' and 4 not in list: 
        board[28]  = board[29] = board[30] = board[37] = board[38] = board[39] = board[46] = board[47] = board[48] = letter
        list.append(4)
    elif board[37] == board[38] == board[39] and board[39] != ' ' and 4 not in list: 
        board[28]  = board[29] = board[30] = board[37] = board[38] = board[39] = board[46] = board[47] = board[48] = letter
        list.append(4)
    elif board[46] == board[47] == board[48] and board[48] != ' ' and 4 not in list: 
        board[28]  = board[29] = board[30] = board[37] = board[38] = board[39] = board[46] = board[47] = board[48] = letter
        list.append(4)
    # doc 4
    elif board[28] == board[37] == board[46] and board[46] != ' ' and 4 not in list: 
        board[28]  = board[29] = board[30] = board[37] = board[38] = board[39] = board[46] = board[47] = board[48] = letter
        list.append(4)
    elif board[29] == board[38] == board[47] and board[47] != ' ' and 4 not in list: 
        board[28]  = board[29] = board[30] = board[37] = board[38] = board[39] = board[46] = board[47] = board[48] = letter
        list.append(4)
    elif board[30] == board[39] == board[48] and board[48] != ' ' and 4 not in list: 
        board[28]  = board[29] = board[30] = board[37] = board[38] = board[39] = board[46] = board[47] = board[48] = letter
        list.append(4)
    # cheo 4
    elif board[28] == board[38] == board[48] and board[48] != ' ' and 4 not in list: 
        board[28]  = board[29] = board[30] = board[37] = board[38] = board[39] = board[46] = board[47] = board[48] = letter
        list.append(4)
    elif board[30] == board[38] == board[46] and board[46] != ' ' and 4 not in list: 
        board[28]  = board[29] = board[30] = board[37] = board[38] = board[39] = board[46] = board[47] = board[48] = letter
        list.append(4)
    # done
    
    # ngang 5
    elif board[31] == board[32] == board[33] and board[33] != ' ' and 5 not in list: 
        board[31]  = board[32] = board[33] = board[40] = board[41] = board[42] = board[49] = board[50] = board[51] = letter
        list.append(5)
    elif board[40] == board[41] == board[42] and board[42] != ' ' and 5 not in list: 
        board[31]  = board[32] = board[33] = board[40] = board[41] = board[42] = board[49] = board[50] = board[51] = letter
        list.append(5)
    elif board[49] == board[50] == board[51] and board[51] != ' ' and 5 not in list: 
        board[31]  = board[32] = board[33] = board[40] = board[41] = board[42] = board[49] = board[50] = board[51] = letter
        list.append(5)
    # doc 5
    elif board[31] == board[40] == board[49] and board[49] != ' ' and 5 not in list: 
        board[31]  = board[32] = board[33] = board[40] = board[41] = board[42] = board[49] = board[50] = board[51] = letter
        list.append(5)
    elif board[32] == board[41] == board[50] and board[50] != ' ' and 5 not in list: 
        board[31]  = board[32] = board[33] = board[40] = board[41] = board[42] = board[49] = board[50] = board[51] = letter
        list.append(5)
    elif board[33] == board[42] == board[51] and board[51] != ' ' and 5 not in list: 
        board[31]  = board[32] = board[33] = board[40] = board[41] = board[42] = board[49] = board[50] = board[51] = letter
        list.append(5)
    # cheo 5
    elif board[31] == board[41] == board[51] and board[51] != ' ' and 5 not in list: 
        board[31]  = board[32] = board[33] = board[40] = board[41] = board[42] = board[49] = board[50] = board[51] = letter
        list.append(5)
    elif board[33] == board[41] == board[49] and board[49] != ' ' and 5 not in list: 
        board[31]  = board[32] = board[33] = board[40] = board[41] = board[42] = board[49] = board[50] = board[51] = letter
        list.append(5)
    # done
    
    # ngang 6
    elif board[34] == board[35] == board[36] and board[36] != ' ' and 6 not in list: 
        board[34]  = board[35] = board[36] = board[43] = board[44] = board[45] = board[52] = board[53] = board[54] = letter
        list.append(6)
    elif board[43] == board[44] == board[45] and board[45] != ' ' and 6 not in list: 
        board[34]  = board[35] = board[36] = board[43] = board[44] = board[45] = board[52] = board[53] = board[54] = letter
        list.append(6)
    elif board[52] == board[53] == board[54] and board[54] != ' ' and 6 not in list: 
        board[34]  = board[35] = board[36] = board[43] = board[44] = board[45] = board[52] = board[53] = board[54] = letter
        list.append(6)
    # doc 6
    elif board[34] == board[43] == board[52] and board[52] != ' ' and 6 not in list: 
        board[34]  = board[35] = board[36] = board[43] = board[44] = board[45] = board[52] = board[53] = board[54] = letter
        list.append(6)
    elif board[35] == board[44] == board[53] and board[53] != ' ' and 6 not in list: 
        board[34]  = board[35] = board[36] = board[43] = board[44] = board[45] = board[52] = board[53] = board[54] = letter
        list.append(6)
    elif board[36] == board[45] == board[54] and board[54] != ' ' and 6 not in list: 
        board[34]  = board[35] = board[36] = board[43] = board[44] = board[45] = board[52] = board[53] = board[54] = letter
        list.append(6)
    # cheo 6
    elif board[34] == board[44] == board[54] and board[54] != ' ' and 6 not in list: 
        board[34]  = board[35] = board[36] = board[43] = board[44] = board[45] = board[52] = board[53] = board[54] = letter
        list.append(6)
    elif board[36] == board[44] == board[52] and board[52] != ' ' and 6 not in list: 
        board[34]  = board[35] = board[36] = board[43] = board[44] = board[45] = board[52] = board[53] = board[54] = letter
        list.append(6)
    # done
    
    # ngang 7
    elif board[55] == board[56] == board[57] and board[57] != ' ' and 7 not in list: 
        board[55]  = board[56] = board[57] = board[64] = board[65] = board[66] = board[73] = board[74] = board[75] = letter
        list.append(7)
    elif board[64] == board[65] == board[66] and board[66] != ' ' and 7 not in list: 
        board[55]  = board[56] = board[57] = board[64] = board[65] = board[66] = board[73] = board[74] = board[75] = letter
        list.append(7)
    elif board[73] == board[74] == board[75] and board[75] != ' ' and 7 not in list: 
        board[55]  = board[56] = board[57] = board[64] = board[65] = board[66] = board[73] = board[74] = board[75] = letter
        list.append(7)
    # doc 7
    elif board[55] == board[64] == board[73] and board[73] != ' ' and 7 not in list: 
        board[55]  = board[56] = board[57] = board[64] = board[65] = board[66] = board[73] = board[74] = board[75] = letter
        list.append(7)
    elif board[56] == board[65] == board[74] and board[74] != ' ' and 7 not in list: 
        board[55]  = board[56] = board[57] = board[64] = board[65] = board[66] = board[73] = board[74] = board[75] = letter
        list.append(7)
    elif board[57] == board[66] == board[75] and board[75] != ' ' and 7 not in list: 
        board[55]  = board[56] = board[57] = board[64] = board[65] = board[66] = board[73] = board[74] = board[75] = letter
        list.append(7)
    # cheo 7
    elif board[55] == board[65] == board[75] and board[75] != ' ' and 7 not in list: 
        board[55]  = board[56] = board[57] = board[64] = board[65] = board[66] = board[73] = board[74] = board[75] = letter
        list.append(7)
    elif board[57] == board[65] == board[73] and board[73] != ' ' and 7 not in list: 
        board[55]  = board[56] = board[57] = board[64] = board[65] = board[66] = board[73] = board[74] = board[75] = letter
        list.append(7)
    # done
    
    # ngang 8
    elif board[58] == board[59] == board[60] and board[60] != ' ' and 8 not in list: 
        board[58]  = board[59] = board[60] = board[67] = board[68] = board[69] = board[76] = board[77] = board[78] = letter
        list.append(8)
    elif board[67] == board[68] == board[69] and board[69] != ' ' and 8 not in list: 
        board[58]  = board[59] = board[60] = board[67] = board[68] = board[69] = board[76] = board[77] = board[78] = letter
        list.append(8)
    elif board[76] == board[77] == board[78] and board[78] != ' ' and 8 not in list: 
        board[58]  = board[59] = board[60] = board[67] = board[68] = board[69] = board[76] = board[77] = board[78] = letter
        list.append(8)
    # doc 8
    elif board[58] == board[67] == board[76] and board[76] != ' ' and 8 not in list: 
        board[58]  = board[59] = board[60] = board[67] = board[68] = board[69] = board[76] = board[77] = board[78] = letter
        list.append(8)
    elif board[59] == board[68] == board[77] and board[77] != ' ' and 8 not in list: 
        board[58]  = board[59] = board[60] = board[67] = board[68] = board[69] = board[76] = board[77] = board[78] = letter
        list.append(8)
    elif board[60] == board[69] == board[78] and board[78] != ' ' and 8 not in list: 
        board[58]  = board[59] = board[60] = board[67] = board[68] = board[69] = board[76] = board[77] = board[78] = letter
        list.append(8)
    # cheo 8
    elif board[58] == board[68] == board[78] and board[78] != ' ' and 8 not in list: 
        board[58]  = board[59] = board[60] = board[67] = board[68] = board[69] = board[76] = board[77] = board[78] = letter
        list.append(8)
    elif board[60] == board[68] == board[76] and board[76] != ' ' and 8 not in list: 
        board[58]  = board[59] = board[60] = board[67] = board[68] = board[69] = board[76] = board[77] = board[78] = letter
        list.append(8)
    # done
    
    # ngang 9
    elif board[61] == board[62] == board[63] and board[63] != ' ' and 9 not in list: 
        board[61]  = board[62] = board[63] = board[70] = board[71] = board[72] = board[79] = board[80] = board[81] = letter
        list.append(9)
    elif board[70] == board[71] == board[12] and board[72] != ' ' and 9 not in list: 
        board[61]  = board[62] = board[63] = board[70] = board[71] = board[72] = board[79] = board[80] = board[81] = letter
        list.append(9)
    elif board[79] == board[80] == board[81] and board[81] != ' ' and 9 not in list: 
        board[61]  = board[62] = board[63] = board[70] = board[71] = board[72] = board[79] = board[80] = board[81] = letter
        list.append(9)
    # doc 9
    elif board[61] == board[70] == board[79] and board[79] != ' ' and 9 not in list: 
        board[61]  = board[62] = board[63] = board[70] = board[71] = board[72] = board[79] = board[80] = board[81] = letter
        list.append(9)
    elif board[62] == board[71] == board[80] and board[80] != ' ' and 9 not in list: 
        board[61]  = board[62] = board[63] = board[70] = board[71] = board[72] = board[79] = board[80] = board[81] = letter
        list.append(9)
    elif board[63] == board[72] == board[81] and board[81] != ' ' and 9 not in list: 
        board[61]  = board[62] = board[63] = board[70] = board[71] = board[72] = board[79] = board[80] = board[81] = letter
        list.append(9)
    # cheo 9
    elif board[61] == board[71] == board[81] and board[81] != ' ' and 9 not in list: 
        board[61]  = board[62] = board[63] = board[70] = board[71] = board[72] = board[79] = board[80] = board[81] = letter
        list.append(9)
    elif board[63] == board[71] == board[79] and board[79] != ' ' and 9 not in list: 
        board[61]  = board[62] = board[63] = board[70] = board[71] = board[72] = board[79] = board[80] = board[81] = letter
        list.append(9)
    
    else: return

def checkWinBig():
    # ngang 1
    if board[11] == board[4] == board[27] and board[17] != ' ': return True
    elif board[38] == board[31] == board[54] and board[44] != ' ': return True
    elif board[65] == board[58] == board[81] and board[71] != ' ': return True
    # doc 1
    elif board[1] == board[30] == board[73] and board[65] != ' ': return True
    elif board[4] == board[51] == board[76] and board[68] != ' ': return True
    elif board[7] == board[45] == board[81] and board[71] != ' ': return True
    # cheo 1
    elif board[1] == board[51] == board[72] and board[71] != ' ': return True
    elif board[7] == board[42] == board[74] and board[65] != ' ': return True

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def player1move():
    global preMove
    # print("----- ----- -----")
    # position = int(input("ENTER A POSITION FOR 'X': "))
    # print("----- ----- -----")
    # makeMove(p1, position)
    # return
    while True:
        try:
            print("----- ----- -----")
            position = int(input("ENTER A POSITION FOR 'X': "))
            print("----- ----- -----")
        except ValueError:
            print("Please enter position as number")
            continue
        else:
            print(f"Last move: {preMove}")
            makeMove(p1, position)
            # preMove = position
            break

def player2move():
    global preMove
    # print("----- ----- -----")
    # position = int(input("ENTER A POSITION FOR 'O': "))
    # print("----- ----- -----")
    # makeMove(p2, position)
    while True:
        try:
            print("----- ----- -----")
            position = int(input("ENTER A POSITION FOR 'O': "))
            print("----- ----- -----")
        except ValueError:
            print("Please enter position as number")
            continue
        else:
            print(f"Last move: {preMove}")
            makeMove(p2, position)
            # preMove = position
            break


printBoard(board)
while True:
    try:
        print("----- ----- -----")
        position = int(input("ENTER A POSITION FOR 'X': "))
        print("----- ----- -----")
    except ValueError:
        print("Please enter position as number")
        continue
    else:
        preMove = position
        makeMove(p1, position)
        # preMove = position
        break

while not checkWinBig():
    player2move()
    player1move()
