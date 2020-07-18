import random

from simulator import run_simulation

true_state = "A" if random.uniform(0,1) > 0.5 else "B"
print(true_state)
result = run_simulation(true_state)
print(result)
