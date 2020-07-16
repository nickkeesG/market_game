import math

def error_to_evidence(error):
    prob_correct_signal = 1 - error
    prob_wrong_signal = error
    
    evidence = math.log(prob_correct_signal / prob_wrong_signal, 2)
    return evidence

def evidence_to_prob(w):
    update_factor = 2**w
    return update_factor / (update_factor + 1)

def prob_to_evidence(p):
    return math.log(p, 2) - math.log((1-p), 2)
