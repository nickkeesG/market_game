import random
import matplotlib.pyplot as plt
import numpy as np
import custom_math as cm

from simulator import run_simulation

market_prices = []
complete_infos = []

for i in range(81):
    print(i)
    signal_diff = i - 40
    true_state = "A" if random.uniform(0,1) > 0.5 else "B"
    result = run_simulation(true_state, signal_diff, verbose = False)
    market_prices.append(cm.prob_to_evidence(result[1]))
    complete_infos.append(cm.prob_to_evidence(result[2]))

x = np.linspace(-1.2, 1.2,100)
plt.plot(x, x, linestyle='dotted')
plt.legend(['x = y (perfect aggregation)'])
plt.scatter(complete_infos, market_prices)
plt.xlabel('complete information belief (bits of evidence)')
plt.ylabel('equilibrium price (bits of evidence)')
plt.title('40 agents, 0.35 error')
plt.show()

