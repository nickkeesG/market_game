from parameters import *
from game import Game

def init_game()
    if ENDOWMENT_GENERATOR = "CONSTANT":
        endowment_profile = [ENDOWMENT_AVERAGE for i in range(N_AGENTS)]
    else:
        endowment_profile = None #need to add different generators
    if ERROR_GENERATOR = "CONSTANT":
        error_profile = [ERROR_AVERAGE for i in range(N_AGENTS)]
    else:
        endowment_profile = None #need to add different generators
    game = Game(N_AGENTS, endowment_profile, error_profile)



    return game
