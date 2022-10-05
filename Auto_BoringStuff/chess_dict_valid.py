"""Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False
depending on if the board is valid.
Requirements: 1 black king, 1 white king, 16 >= pieces per player, 8 >= pawns per player, 
All on valid spaces '1a' to '8h'. Piece names begin with 'b' or 'w' to indicate color followed by
'pawn', 'knight', 'bishop', 'rook', 'queen' or 'king'.
Function should detect when a bug has resulted in an improper chess board.
"""
valid_board = ['1a','2a','3a','4a','5a','6a','7a','8a',
                '1b','2b','3b','4b','5b','6b','7b','8b',
                '1c','2c','3c','4c','5c','6c','7c','8c',
                '1d','2d','3d','4d','5d','6d','7d','8d',
                '1e','2e','3e','4e','5e','6e','7e','8e',
                '1f','2f','3f','4f','5f','6f','7f','8f',
                '1g','2g','3g','4g','5g','6g','7g','8g',
                '1h','2h','3h','4h','5h','6h','7h','8h']

valid_blk = ['bpawn','bknight','bbishop','brook','bqueen','bking',''] # pieces separated by color to ease checking for duplicate kings >16 pieces per player, and >8 pawns per player
valid_wht = ['wpawn','wknight','wbishop','wrook','wqueen','wking',''] # '' included to indicate blank spaces (just in case!)


test_real = {'1a': 'bpawn', '8h': 'bking', '5d': 'wking'}
test_false = {'1a': 'item', '8z': '2 item', '5d': '3 item'}
test_full = {'5a': 'wpawn', '8h': 'bking', '5d': 'wking', '1a': 'wpawn','2a': 'wpawn',
                '3c': 'bpawn','4c': 'wpawn','5h': 'wpawn','6a': 'brook','7e': 'bpawn',
                '8a': 'bpawn','1b': 'bpawn','2b': 'bpawn','3b': 'bbishop','4b': 'wpawn',
                '5f': 'bpawn','6d': 'bpawn','7b': 'bpawn'}                                                      

def isValidChessBoard(dict_arg):
    #test if keys are valid board spaces
    for key in dict_arg.keys():
        if key not in valid_board:
            return False
    
    #test if values are valid game pieces
    for value in dict_arg.values(): 
        if value not in valid_blk and value not in valid_wht:
            return False 

    #check for duplicate kings
    wht_kings = len([x for x in dict_arg if dict_arg[x] == 'wking']) #could also use dict_arg[x] for x in.... but since all we want is the number of occurrences, returning x or dict_arg[x] doesn't matter much.
    blk_kings = len([x for x in dict_arg if dict_arg[x] == 'bking'])
    if wht_kings > 1 or blk_kings > 1:
        return False

    #check for greater than 8 pawns
    wht_pawns = len([x for x in dict_arg if dict_arg[x] == 'wpawn'])
    blk_pawns = len([x for x in dict_arg if dict_arg[x] == 'bpawn'])
    if wht_pawns > 8 or blk_pawns > 8:
        return False

    #check for greater than 16 pieces per player.
    wht_pieces = len([x for x in dict_arg if dict_arg[x] in valid_wht])
    blk_pieces = len([x for x in dict_arg if dict_arg[x] in valid_blk])
    if wht_pieces > 16 or blk_pieces > 16:
        return False
    
    #if none of the above have caused problems, it should be valid.
    return True

print(isValidChessBoard(test_real))
print(isValidChessBoard(test_false))
print(isValidChessBoard(test_full))