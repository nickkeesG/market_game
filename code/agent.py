import custom_math

class Agent:
    def __init__(self, endowment, error_rate):
        self.error_rate = error_rate
        self.belief = 0.5               #this is the agent's prior
        self.endowment = endowment
        self.strategy = None

    def get_expected_utility_function(self, current_price):
        old_strategy = self.strategy
        def f(new_strategy):
            new_price = current_price + self.endowment * (new_strategy - old_strategy)
            shares_a = new_strategy * self.endowment / new_price if new_strategy > 0 else 0
            shares_b = (1 - new_strategy) * self.endowment / (1 - new_price) if (1 - new_strategy) > 0 else 0

            expected_utility = shares_a * self.belief + shares_b * (1 - self.belief)
            return expected_utility * -1 #we are using scipy.optimize.minimize to maximize a function
        return f

    def get_expected_utility(self, new_strategy, current_price):
        new_price = current_price + self.endowment * (new_strategy - self.strategy)

        shares_a = new_strategy * self.endowment / new_price if new_strategy > 0 else 0
        shares_b = (1 - new_strategy) * self.endowment / (1 - new_price) if (1 - new_strategy) > 0 else 0

        return shares_a * self.belief + shares_b * (1 - self.belief)

    def update_belief(self, signal):
        evidence_size = custom_math.error_to_evidence(self.error_rate)
        if signal == 'a':
            new_evidence = evidence_size
        else:
            new_evidence = -1 * evidence_size

        current_evidence = custom_math.prob_to_evidence(self.belief)
        self.belief = custom_math.evidence_to_prob(current_evidence + new_evidence)
        
