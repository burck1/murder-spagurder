import numpy as np

def transform_move_state(snek_move):
    '''
    TODO: Joel
    snek_start: response from /move
        https://docs.battlesnake.io/snake-api.html#tag/endpoints/paths/~1move/post
    returns a numpy array
    '''
    w = snek_move['board']['width']
    h = snek_move['board']['height']

    board_state = np.zeros((w, h))
    return np.reshape(board_state, [1, w * h])
