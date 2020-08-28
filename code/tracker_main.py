import random
import matplotlib.pyplot as plt
import numpy as np
import custom_math as cm
from simulator import run_simulation
import parameters as p

market_prices = []
complete_infos = []
tracker = []

for i in range(p.N_AGENTS*2 + 1):
    print(i, "/", p.N_AGENTS*2 + 1)
    signal_diff = p.N_AGENTS - i
    true_state = "A" if random.uniform(0,1) > 0.5 else "B"
    result = run_simulation(true_state, signal_diff, verbose = False)
    market_prices.append(result[1])
    complete_infos.append(result[2])
    tracker.append(result[2]*(1-p.ERROR_AVERAGE) + (1-result[2])*(p.ERROR_AVERAGE))

#what percentage of the total bits are retained by each aggregation method in our simulations?
#price_retention = []
#average_retention = []
#for i in range(len(complete_infos)):
#    if abs(complete_infos[i]) > 0.1: 
#        price_retention.append(market_prices[i] / complete_infos[i])
#        average_retention.append(average_beliefs[i] / complete_infos[i])
#
#print("Averaging: ", np.mean(average_retention), "(", np.std(average_retention), ")")
#print("Mkt_price: ", np.mean(price_retention), "(", np.std(price_retention), ")")
#
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(str(p.N_AGENTS)+ " agents, " + str(p.ERROR_AVERAGE) + ' error')

ax1.set(xlabel='complete information belief', ylabel='aggregated belief')
x = np.linspace(min(market_prices), max(market_prices),100)
ax1.plot(x, x, linestyle='dotted')
ax1.scatter(complete_infos, market_prices)
ax1.scatter(complete_infos, tracker, marker = "+")

market_prices = [cm.prob_to_evidence(p) for p in market_prices]
print(complete_infos)
complete_infos = [cm.prob_to_evidence(p) for p in complete_infos]
tracker = [cm.prob_to_evidence(p) for p in tracker]
ax2.set(xlabel='complete information belief (bits)', ylabel='aggregated belief (bits)')
x = np.linspace(min(market_prices), max(market_prices),100)
ax2.plot(x, x, linestyle='dotted')
ax2.scatter(complete_infos, market_prices)
ax2.scatter(complete_infos, tracker, marker = "+")

fig.legend(['x = y (perfect aggregation)', 'Equilibrium Market Price', 'Tracker'])
plt.show()

