from agent import Agent

class Game:
    def __init__(self, n_agents):
        self.agents = [Agent() for i in range(n_agents)]
