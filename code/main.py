import random
import matplotlib.pyplot as plt
import numpy as np
import custom_math as cm
from simulator import run_simulation
import parameters as p


true_state = "A"if random.uniform(0,1) > 0.5 else "B"
result = run_simulation(true_state)
print(result[1], result[2])
