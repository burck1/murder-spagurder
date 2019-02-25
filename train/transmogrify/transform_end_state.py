import numpy as np

def transform_end_state(snek_end):
    '''
    TODO: Joel
    snek_end: response from /end
        https://docs.battlesnake.io/snake-api.html#tag/endpoints/paths/~1end/post
    returns a numpy array
    '''
    w = snek_end['board']['width']
    h = snek_end['board']['height']

    board_state = np.zeros((w, h))
    return np.reshape(board_state, [1, w * h])
