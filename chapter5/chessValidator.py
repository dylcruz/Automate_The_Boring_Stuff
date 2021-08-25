def isValidChessBoard(board):
    wpawnNum = 0
    wkingNum = 0
    wpieceNum = 0

    bpawnNum = 0
    bkingNum = 0
    bpieceNum = 0

    for v in board.values():
        if v == 'wpawn':
            wpawnNum += 1
            wpieceNum += 1
        if v == 'wking':
            wkingNum += 1
            wpieceNum += 1
        if v == 'wrook' or v == 'wknight' or v == 'wbishop' or v == 'wqueen':
            wpieceNum += 1

        if v == 'bpawn':
            bpawnNum += 1
            bpieceNum += 1
        if v == 'bking':
            bkingNum += 1
            bpieceNum += 1
        if v == 'brook' or v == 'bknight' or v == 'bbishop' or v == 'bqueen':
            bpieceNum += 1
    
    if wpawnNum > 8:
        print("TOO MANY WHITE PAWNS!")
        return False
    if wkingNum > 1:
        print("TOO MANY WHITE KINGS!")
        return False
    if wpieceNum > 16:
        print("TOO MANY WHITE PIECES!")
        return False
    
    if bpawnNum > 8:
        print("TOO MANY BLACK PAWNS!")
        return False
    if bkingNum > 1:
        print("TOO MANY BLACK KINGS!")
        return False
    if bpieceNum > 16:
        print("TOO MANY BLACK PIECES!")
        return False
    
    for i in board.keys():
        if int(i[0]) > 8 or int(i[0]) < 1:
            print("There is a piece on an invalid space. Space is " + i[0] + i[1])
            return False
        if i[1] < 'a' or i[1] > 'h':
            print("There is a piece on an invalid space. Space is " + i[0] + i[1])
            return False

    return True

myBoard = {'1a': 'wrook', '2a': 'wpawn', '3a': '', '4a': '', '5a': '', '6a': '', '7a': 'bpawn', '8a': 'brook',
           '1b': 'wknight', '2b': 'wpawn', '3b': '', '4b': '', '5b': '', '6b': '', '7b': 'bpawn', '8b': 'bknight',
           '1c': 'wbishop', '2c': 'wpawn', '3c': '', '4c': '', '5c': '', '6c': '', '7c': 'bpawn', '8c': 'bbishop',
           '1d': 'wqueen', '2d': 'wpawn', '3d': '', '4d': '', '5d': '', '6d': '', '7d': 'bpawn', '8d': 'bking',
           '1e': 'wking', '2e': 'wpawn', '3e': '', '4e': '', '5e': '', '6e': '', '7e': 'bpawn', '8e': 'bqueen',
           '1f': 'wbishop', '2f': 'wpawn', '3f': '', '4f': '', '5f': '', '6f': '', '7f': 'bpawn', '8f': 'bbishop',
           '1g': 'wknight', '2g': 'wpawn', '3g': '', '4g': '', '5g': '', '6g': '', '7g': 'bpawn', '8g': 'bknight',
           '1h': 'wrook', '2h': 'wpawn', '3h': '', '4h': '', '5h': '', '6h': '', '7h': 'bpawn', '8h': 'brook',}

if isValidChessBoard(myBoard):
    print("The board is valid.")
else:
    print("The board is invalid")
