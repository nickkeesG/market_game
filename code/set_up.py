import random

from parameters import *
from game import Game

#Endowment: How much does each agent have to spend in the market?
#Error:     How likely is it that the signal an agent receives does NOT match the true state (A/B)

#signal_diff: If signal_diff is set to None, then the signals will be sampled according to the distribution of each agent according to their error rate. If signal_diff is set to a number, this determines how many more agents will receive the signal 'a' to the signal 'b'. 

def init_game(true_state, signal_diff):
    if ENDOWMENT_GENERATOR == "CONSTANT":
        endowment_profile = [1/N_AGENTS for i in range(N_AGENTS)]
    else:
        endowment_profile = None #need to add different generators
    if ERROR_GENERATOR == "CONSTANT":
        error_profile = [ERROR_AVERAGE for i in range(N_AGENTS)]
    else:
        endowment_profile = None #need to add different generators
        
    game = Game(N_AGENTS, endowment_profile, error_profile, true_state)
    game.distribute_signals(signal_diff)
    game.init_strategy_profile()
    
    return game
