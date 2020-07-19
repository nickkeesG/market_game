from set_up import init_game
from iterated_best_response import run_ibr
import custom_math as cm

def get_total_evidence(game):
    total = 0
    for agent in game.agents:
        total += cm.prob_to_evidence(agent.belief)
    return total

def run_simulation(true_state, signal_diff = None, verbose = True):
    game = init_game(true_state, signal_diff)
    converged = run_ibr(game, verbose)

    if verbose:
        print_equilibrium(game)

    if converged:
        total_evidence = get_total_evidence(game)
        complete_information_belief = cm.evidence_to_prob(total_evidence)
        return converged, game.get_price(), complete_information_belief
    else:
        return False, None, None

def print_equilibrium(game):
    print("Strategy profile:")
    for a in game.agents:
        print(round(a.belief, 4), "\t", round(a.strategy, 5), "\t", round(a.get_expected_utility(a.strategy, game.get_price()), 4)) 
