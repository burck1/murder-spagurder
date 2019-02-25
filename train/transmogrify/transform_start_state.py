import numpy as np

def transform_start_state(snek_start):
    '''
    TODO: Joel
    snek_start: response from /start
        https://docs.battlesnake.io/snake-api.html#tag/endpoints/paths/~1start/post
    returns a numpy array
    '''
    w = snek_start['board']['width']
    h = snek_start['board']['height']

    board_state = np.zeros((w, h))
    return np.reshape(board_state, [1, w * h])
