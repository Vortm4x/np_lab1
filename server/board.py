TILE_X      = 'X'
TILE_O      = 'O'
TILE_EMPTY  = ' '
BOARD_SIZE  = 100
WIN_COUNT   = 5



def board_create():
    board = [ 
        [
            TILE_EMPTY
            for _ in range(0, BOARD_SIZE)
        ] 
        for _ in range(0, BOARD_SIZE) 
    ]
    return board

def board_reset(board):
    for y in range (0, BOARD_SIZE):
        for x in range (0, BOARD_SIZE):
            board[y][x] = TILE_EMPTY


def board_check_hor(board):
    winner_tile = TILE_EMPTY
    tiles_in_row = 0

    for y in range (0, BOARD_SIZE):
        for x in range (0, BOARD_SIZE):

            if board[y][x] == TILE_EMPTY:
                tiles_in_row = 0

            elif board[y][x] == TILE_X:
                if winner_tile == TILE_X:
                    tiles_in_row += 1
                else:
                    tiles_in_row = 1

            elif board[y][x] == TILE_O:
                if winner_tile == TILE_X:
                    tiles_in_row += 1
                else:
                    tiles_in_row = 1

            winner_tile = board[y][x]

            if(tiles_in_row == WIN_COUNT):
                return winner_tile

        winner_tile = TILE_EMPTY
        tiles_in_row = 0


def board_check_vert(board):
    winner_tile = TILE_EMPTY
    tiles_in_row = 0

    for x in range (0, BOARD_SIZE):
        for y in range (0, BOARD_SIZE):

            if board[y][x] == TILE_EMPTY:
                tiles_in_row = 0

            elif board[y][x] == TILE_X:
                if winner_tile == TILE_X:
                    tiles_in_row += 1
                else:
                    tiles_in_row = 1

            elif board[y][x] == TILE_O:
                if winner_tile == TILE_X:
                    tiles_in_row += 1
                else:
                    tiles_in_row = 1

            winner_tile = board[y][x]

            if(tiles_in_row == WIN_COUNT):
                return winner_tile

        winner_tile = TILE_EMPTY
        tiles_in_row = 0

    return TILE_EMPTY


def board_check(board):
    tile = board_check_hor(board)

    if tile == TILE_X or tile == TILE_O:
        return tile
    
    tile = board_check_vert(board)

    if tile == TILE_X or tile == TILE_O:
        return tile
    
    return TILE_EMPTY

def board_set(board, x, y, val):
    board[y - 1][x - 1] = val