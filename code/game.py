import random

from agent import Agent

class Game:
    def __init__(self, n_agents, endowment_profile, error_profile, true_state):
        self.agents = [Agent(endowment_profile[i], error_profile[i]) for i in range(n_agents)]
        self.true_state = true_state

    def distribute_signals(self, signal_diff = None):
        sample_signals = True if signal_diff == None else False
        
        #In this case, sample signals(not predetermined)
        if sample_signals:
            correct_signal = "a" if self.true_state == "A" else "b"
            incorrect_signal = "b" if self.true_state == "A" else "a"
            
            for i in range(len(self.agents)):
                e = self.agents[i].error_rate                
                if random.uniform(0,1) > e:
                    self.agents[i].update_belief(correct_signal)
                else:
                    self.agents[i].update_belief(incorrect_signal)

        else:
            for i in range(len(self.agents)):
                if i + signal_diff < len(self.agents)/2:
                    self.agents[i].update_belief("a")
                else:
                    self.agents[i].update_belief("b")

    def get_weighted_average_belief(self):
        return sum([a.belief*a.endowment for a in self.agents])

    def get_average_belief(self):
        return sum([a.belief for a in self.agents]) / len(self.agents)

    def get_price(self):
        demand_for_a = 0
        for a in self.agents:
            demand_for_a += a.strategy * a.endowment
        return demand_for_a

    def init_strategy_profile(self):
        for i in range(len(self.agents)):
            self.agents[i].strategy = self.agents[i].belief

    
