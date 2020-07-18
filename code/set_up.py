import random

from parameters import *
from game import Game

#Endowment: How much does each agent have to spend in the market?
#Error:     How likely is it that the signal an agent receives does NOT match the true state (A/B)

def init_game(true_state):
    if ENDOWMENT_GENERATOR == "CONSTANT":
        endowment_profile = [1/N_AGENTS for i in range(N_AGENTS)]
    else:
        endowment_profile = None #need to add different generators
    if ERROR_GENERATOR == "CONSTANT":
        error_profile = [ERROR_AVERAGE for i in range(N_AGENTS)]
    else:
        endowment_profile = None #need to add different generators
        
    game = Game(N_AGENTS, endowment_profile, error_profile, true_state)

    game.distribute_signals()
    game.init_strategy_profile()
    
    return game
