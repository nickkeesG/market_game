import random
import numpy as np

from parameters import *
from game import Game

#Endowment: How much does each agent have to spend in the market?
#Error:     How likely is it that the signal an agent receives does NOT match the true state (A/B)

#signal_diff: If signal_diff is set to None, then the signals will be sampled according to the distribution of each agent according to their error rate. If signal_diff is set to a number, this determines how many more agents will receive the signal 'a' to the signal 'b'. 

def init_game(true_state, signal_diff):
    if ENDOWMENT_GENERATOR == "CONSTANT":
        endowment_profile = [1/N_AGENTS for i in range(N_AGENTS)]
    elif ENDOWMENT_GENERATOR == "BINOMIAL":
        endowment_profile = [np.random.binomial(100, 0.5) for i in range(N_AGENTS)]
        endowment_profile = [e/sum(endowment_profile) for e in endowment_profile]
    elif ENDOWMENT_GENERATOR == "PARETO":
        endowment_profile = [np.random.pareto(1) for i in range(N_AGENTS)]
        endowment_profile = [e/sum(endowment_profile) for e in endowment_profile]
    else:
        endowment_profile = None #need to add different generators
    if ERROR_GENERATOR == "CONSTANT":
        error_profile = [ERROR_AVERAGE for i in range(N_AGENTS)]
    elif ERROR_GENERATOR == "PARETO":
        error_profile = [np.random.pareto(1) for i in range(N_AGENTS)]
        error_profile = [e/sum(error_profile) for e in error_profile]
    else:
        endowment_profile = None #need to add different generators
    
    game = Game(N_AGENTS, endowment_profile, error_profile, true_state)
    game.distribute_signals(signal_diff)
    game.init_strategy_profile()
    
    return game
