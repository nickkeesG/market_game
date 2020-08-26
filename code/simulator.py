from set_up import init_game
from iterated_best_response import run_ibr
import custom_math as cm
import parameters

#currently this function assumes a prior shared by all agents
def get_total_evidence(game):
    #include the evidence all agents already have as part of the total evidence
    total = cm.prob_to_evidence(parameters.PRIOR)
    for agent in game.agents:
        #for each agent count what new evidence they have gained
        total += cm.prob_to_evidence(agent.belief)
        total -= cm.prob_to_evidence(parameters.PRIOR)
    return total

def run_simulation(true_state, signal_diff = None, verbose = True):
    game = init_game(true_state, signal_diff)
    converged = run_ibr(game, verbose)

    if verbose:
        print_equilibrium(game)

    if converged:
        total_evidence = get_total_evidence(game)
        complete_information_belief = cm.evidence_to_prob(total_evidence)
        weighted_average_belief = game.get_weighted_average_belief()
        return converged, game.get_price(), complete_information_belief, weighted_average_belief
    else:
        return False, None, None

def print_equilibrium(game):
    print("Strategy profile:")
    for a in game.agents:
        print(round(a.belief, 4), "\t", round(a.strategy, 5), "\t", round(a.get_expected_utility(a.strategy, game.get_price()), 4)) 
