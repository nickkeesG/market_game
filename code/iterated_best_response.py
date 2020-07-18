import random

def find_best_strategy(agent, current_price):
    best_strategy = 0.5
    best_utility = agent.get_expected_utility(best_strategy, current_price)

    step = 0.1
    while abs(step) > 0.00000001:
        best_strategy += step
        new_util = agent.get_expected_utility(best_strategy, current_price)
        if best_utility >= new_util:
            best_strategy -= step
            step /= -2
        else:
            best_utility = new_util

    return min(max(best_strategy, 0), 1)

def run_ibr(game):
    order = [i for i in range(len(game.agents))]
    random.shuffle(order)

    converged = False
    while not converged:
        converged = True
        for idx in order:
            current_price = game.get_price()
            best_strategy = find_best_strategy(game.agents[idx], current_price)
            if not best_strategy == game.agents[idx].strategy:
                converged = False
                print(idx, "\t", game.agents[idx].strategy, "\t" , best_strategy)
                game.agents[idx].strategy = best_strategy

    return converged
