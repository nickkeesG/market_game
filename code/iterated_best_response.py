import random

def run_ibr(game):
    order = [i for i in range(len(game.agents))]
    random.shuffle(order)

    converged = False
    while not converged:
        for idx in order:
            a = 1
            #assign best strategy for agent idx
