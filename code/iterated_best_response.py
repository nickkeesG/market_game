import random

#TODO find algebraic solution to replace this function
def find_best_strategy(agent, current_price):
    best_strategy = 0.5
    best_utility = agent.get_expected_utility(best_strategy, current_price)

    step = 0.1
    while abs(step) > 0.000000001:
        best_strategy += step
        new_util = agent.get_expected_utility(best_strategy, current_price)
        if best_utility >= new_util:
            best_strategy -= step
            step /= -10
        else:
            best_utility = new_util

    return min(max(best_strategy, 0), 1)

def run_ibr(game, verbose = True):
    order = [i for i in range(len(game.agents))]
    random.shuffle(order)

    converged = False
    while not converged:
        converged = True
        for idx in order:
            current_price = game.get_price()
            best_strategy = find_best_strategy(game.agents[idx], current_price)
            if abs(best_strategy - game.agents[idx].strategy) > 0.00001:
                converged = False
                if verbose:
                    print("Agent: ", idx, "\told_strat:", game.agents[idx].strategy, "\tnew_strat:" , best_strategy)
                game.agents[idx].strategy = best_strategy

    return converged
