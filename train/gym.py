import transmogrify.transform_start_state
import transmogrify.transform_move_state
import transmogrify.transform_end_state

def make(game):
    print(game)
    return GameEnvironment()

class GameEnvironment:
    def __init__(self):
        self.observation_space = ObservationSpace()
        self.action_space = ActionSpace()
    def reset(self):
        # response from /start
        # https://docs.battlesnake.io/snake-api.html#tag/endpoints/paths/~1start/post
        return transmogrify.transform_start_state.transform_start_state({
            'game': {
                'id': 'game-id-string'
            },
            'turn': 4,
            'board': {
                'height': 15,
                'width': 15,
                'food': [
                    {
                        'x': 1,
                        'y': 3
                    }
                ],
                'snakes': [
                    {
                        'id': 'snake-id-string',
                        'name': 'Sneky Snek',
                        'health': 90,
                        'body': [
                            {
                                'x': 1,
                                'y': 3
                            }
                        ]
                    }
                ]
            },
            'you': {
                'id': 'snake-id-string',
                'name': 'Sneky Snek',
                'health': 90,
                'body': [
                    {
                        'x': 1,
                        'y': 3
                    }
                ]
            }
        })

    def step(self, action):
        end = False # todo
        if end:
            response = {
                'game': {
                    'id': 'game-id-string'
                },
                'turn': 4,
                'board': {
                    'height': 15,
                    'width': 15,
                    'food': [
                        {
                            'x': 1,
                            'y': 3
                        }
                    ],
                    'snakes': [
                        {
                            'id': 'snake-id-string',
                            'name': 'Sneky Snek',
                            'health': 90,
                            'body': [
                                {
                                    'x': 1,
                                    'y': 3
                                }
                            ]
                        }
                    ]
                },
                'you': {
                    'id': 'snake-id-string',
                    'name': 'Sneky Snek',
                    'health': 90,
                    'body': [
                        {
                            'x': 1,
                            'y': 3
                        }
                    ]
                }
            }
            next_state = transmogrify.transform_end_state.transform_end_state(response)
            reward = response['turn']
            done = True
        else:
            response = {
                'game': {
                    'id': 'game-id-string'
                },
                'turn': 4,
                'board': {
                    'height': 15,
                    'width': 15,
                    'food': [
                        {
                            'x': 1,
                            'y': 3
                        }
                    ],
                    'snakes': [
                        {
                            'id': 'snake-id-string',
                            'name': 'Sneky Snek',
                            'health': 90,
                            'body': [
                                {
                                    'x': 1,
                                    'y': 3
                                }
                            ]
                        }
                    ]
                },
                'you': {
                    'id': 'snake-id-string',
                    'name': 'Sneky Snek',
                    'health': 90,
                    'body': [
                        {
                            'x': 1,
                            'y': 3
                        }
                    ]
                }
            }
            next_state = transmogrify.transform_move_state.transform_move_state(response)
            reward = response['turn']
            done = False
        return next_state, reward, done, None

class ObservationSpace:
    def __init__(self):
        self.width = 7
        self.height = 7
        self.shape = [(self.width * self.height),]

class ActionSpace:
    def __init__(self):
        self.n = 4 # number of moves
