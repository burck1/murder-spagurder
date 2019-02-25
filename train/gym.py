import numpy as np

def make(game):
    print(game)
    return GameEnvironment()

class GameEnvironment:
    def __init__(self):
        self.observation_space = ObservationSpace()
        self.action_space = ActionSpace()
    def reset(self):
        return np.zeros((self.observation_space.width, self.observation_space.height))
    def step(self, action):
        next_state = np.zeros((self.observation_space.width, self.observation_space.height))
        reward = 10
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
