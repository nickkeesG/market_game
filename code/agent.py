import custom_math

class Agent:
    def __init__(self):
        self.error_rate = 0.5
        self.belief = 0.5

    def update_belief(self, signal):
        evidence_size = custom_math.error_to_evidence(self.error_rate)
        if signal == 'a':
            new_evidence = evidence_size
        else:
            new_evidence = -1 * evidence_size

        current_evidence = custom_math.prob_to_evidence(self.belief)
        self.belief = custom_math.evidence_to_prob(current_evidence + new_evidence)
        
