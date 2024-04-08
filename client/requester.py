import re
import json

TILE_X      = 'X'
TILE_O      = 'O'
TILE_EMPTY  = ' '
BOARD_SIZE  = 100


def prepare() -> bytes:
    x_pos = -1
    y_pos = -1
    tile = TILE_EMPTY

    while True:
        raw_input = input('Enter row: ')
        
        try:
            x_pos = int(raw_input)
        except ValueError:
            print('Not a number!')
        else:
            if 1 <= x_pos <= BOARD_SIZE:
                break
            else:
                print('From 1 to 100 required!')

    while True:
        raw_input = input('Enter col: ')
        
        try:
            y_pos = int(raw_input)
        except ValueError:
            print('Not a number!')
        else:
            if 1 <= x_pos <= BOARD_SIZE:
                break
            else:
                print('From 1 to 100 required!')

    while True:
        raw_input = input(f"Enter {TILE_O} or {TILE_X}: ")

        if raw_input == TILE_O or raw_input == TILE_X:
            tile = raw_input
            break
        else:
            print('Invalid tile value!')

    json_request = {
        'x': x_pos,
        'y': y_pos,
        'tile' : tile,
    }

    request_data = json.dumps(json_request).encode()
    
    return request_data


def handle(response_data : bytes) -> None:
    json_response = json.loads(response_data)
    
    result = json_response['result']

    if result == TILE_X or result == TILE_O:
        print(f"{result} WON!\n")
    elif result == TILE_EMPTY:
        print(f"Game is not over")