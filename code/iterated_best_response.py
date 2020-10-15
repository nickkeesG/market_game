import random
from scipy.optimize import minimize
import math

EPSILON = 0.000001

def find_best_strategy(agent, current_price):
    #TODO: Update the temporary division by zero fix in the next line
    p_hat = current_price - agent.endowment*agent.strategy
    q_hat = (1-current_price) - agent.endowment*(1-agent.strategy)
    b = agent.belief
    optimal_p = 1 / (1+ math.sqrt(((1-b)*q_hat)/(b*p_hat))) if p_hat>0 else 0
    best_strategy = (optimal_p - p_hat)/agent.endowment
    return min(max(best_strategy, 0), 1)
    
def run_ibr(game, verbose = True):
    order = [i for i in range(len(game.agents))]
    random.shuffle(order)

    converged = False
    while not converged:
        random.shuffle(order)
        converged = True
        for idx in order:
            current_price = game.get_price()
            best_strategy = find_best_strategy(game.agents[idx], current_price)
            if abs(best_strategy - game.agents[idx].strategy) > EPSILON:
                converged = False
                if verbose:
                    print("Agent: ", idx, "\told_strat:", game.agents[idx].strategy, "\tnew_strat:" , best_strategy)
                game.agents[idx].strategy = best_strategy

    return converged
