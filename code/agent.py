import custom_math
import parameters

class Agent:
    def __init__(self, endowment, error_rate, prior = parameters.PRIOR):
        self.error_rate = error_rate
        self.belief = prior             
        self.endowment = endowment
        self.strategy = None            #strategy will be set by the function game.init_strategy_profile()

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
        probability_signal_correct = 1 - self.error_rate
        
        if signal == 'a':
            probability_of_A_given_signal = probability_signal_correct
        else:
            probability_of_A_given_signal = 1 - probability_signal_correct
        
        new_evidence = custom_math.prob_to_evidence(probability_of_A_given_signal)
        prior_evidence = custom_math.prob_to_evidence(self.belief)
        posterior_evidence = prior_evidence + new_evidence
        self.belief = custom_math.evidence_to_prob(posterior_evidence)
        
