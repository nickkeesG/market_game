import math

#These functions convert between the two scales: Probability and bits of evidence. Probability ranges from 0 to 1, while evidence ranges from -inf to +inf. Positive evidence is evidence for A and evidence against B, while negative evidence evidence is evidence for B, against A. 

def evidence_to_prob(w):
    update_factor = 2**w
    return update_factor / (update_factor + 1)

def prob_to_evidence(p):
    # Updated the conversion to tackle p>=1 
    return (math.log(p, 2) - math.log((1-p), 2)) if 0<p<1 else 0
