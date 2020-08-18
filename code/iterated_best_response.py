import random
from scipy.optimize import minimize 

#TODO find algebraic solution to replace this function
def find_best_strategy(agent, current_price):
    x0 = 0.5
    f = agent.get_expected_utility_function(current_price)
    result = minimize(f, x0, tol = 0.00000000000001) #Note that minimize will maximize, as the result is multiplied by -1
    best_strategy = result.x[0]
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
            if abs(best_strategy - game.agents[idx].strategy) > 0.0000001:
                converged = False
                if verbose:
                    print("Agent: ", idx, "\told_strat:", game.agents[idx].strategy, "\tnew_strat:" , best_strategy)
                game.agents[idx].strategy = best_strategy

    return converged
