from set_up import init_game
from iterated_best_response import run_ibr
import custom_math as cm

def get_total_evidence(game):
    total = 0
    for agent in game.agents:
        total += cm.prob_to_evidence(agent.belief)
    return total

def run_simulation():
    game = init_game()
    converged = run_ibr(game)
    if converged:
        total_evidence = get_total_evidence(game)
        complete_information_belief = cm.evidence_to_prob(total_evidence)
        return converged, game.price, complete_information_belief
    else:
        return False, None, None
