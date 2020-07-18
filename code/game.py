import random

from agent import Agent

class Game:
    def __init__(self, n_agents, endowment_profile, error_profile, true_state):
        self.agents = [Agent(endowment_profile[i], error_profile[i]) for i in range(n_agents)]
        self.true_state = true_state

    def distribute_signals(self):
        correct_signal = "a" if self.true_state == "A" else "b"
        incorrect_signal = "b" if self.true_state == "A" else "a"
        
        for i in range(len(self.agents)):
            e = self.agents[i].error_rate
            if random.uniform(0,1) > e:
                self.agents[i].update_belief(correct_signal)
            else:
                self.agents[i].update_belief(incorrect_signal)

    def get_price(self):
        demand_for_a = 0
        for a in self.agents:
            demand_for_a += a.strategy * a.endowment
        return demand_for_a

    def init_strategy_profile(self):
        for i in range(len(self.agents)):
            self.agents[i].strategy = self.agents[i].belief

    
