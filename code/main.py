import random
import matplotlib.pyplot as plt
import numpy as np
import custom_math as cm
from parameters import ERROR_AVERAGE, N_AGENTS 
from simulator import run_simulation

market_prices = []
complete_infos = []
average_beliefs = []

for i in range(N_AGENTS*2 + 1):
    print(i, " /", N_AGENTS*2 + 1) 
    signal_diff = i - N_AGENTS
    true_state = "A" if random.uniform(0,1) > 0.5 else "B"
    result = run_simulation(true_state, signal_diff, verbose = False)
    market_prices.append(cm.prob_to_evidence(result[1]))
    complete_infos.append(cm.prob_to_evidence(result[2]))
    average_beliefs.append(cm.prob_to_evidence(result[3]))

x = np.linspace(min(market_prices)*1.5, max(market_prices)*1.5,100)
plt.plot(x, x, linestyle='dotted')
plt.scatter(complete_infos, market_prices)
plt.scatter(complete_infos, average_beliefs, marker = "+")
plt.legend(['x = y (perfect aggregation)', 'Equilibrium Market Price', 'Average Agent Belief'])
plt.xlabel('complete information belief (bits of evidence)')
plt.title(str(N_AGENTS)+ " agents, " + str(ERROR_AVERAGE) + ' error')
plt.show()

