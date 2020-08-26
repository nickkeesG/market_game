import random
import matplotlib.pyplot as plt
import numpy as np
import custom_math as cm
from simulator import run_simulation
import parameters as p

market_prices = []
complete_infos = []
average_beliefs = []

for i in range(200):
    print(i)
    true_state = "A" if random.uniform(0,1) > 0.5 else "B"
    result = run_simulation(true_state, verbose = False)
    market_prices.append(cm.prob_to_evidence(result[1]))
    complete_infos.append(cm.prob_to_evidence(result[2]))
    average_beliefs.append(cm.prob_to_evidence(result[3]))

#what percentage of the total bits are retained by each aggregation method in our simulations?
price_retention = []
average_retention = []
for i in range(len(complete_infos)):
    if abs(complete_infos[i]) > 0.1: 
        price_retention.append(market_prices[i] / complete_infos[i])
        average_retention.append(average_beliefs[i] / complete_infos[i])

print("Averaging: ", np.mean(average_retention), "(", np.std(average_retention), ")")
print("Mkt_price: ", np.mean(price_retention), "(", np.std(price_retention), ")")

#fig, (ax1, ax2) = plt.subplots(1, 2)
#fig.suptitle(str(p.N_AGENTS)+ " agents, " + str(p.ERROR_AVERAGE) + ' error')
#
#ax1.set(xlabel='complete information belief', ylabel='aggregated belief')
#x = np.linspace(min(market_prices), max(market_prices),100)
#ax1.plot(x, x, linestyle='dotted')
#ax1.scatter(complete_infos, market_prices)
#ax1.scatter(complete_infos, average_beliefs, marker = "+")
#
#market_prices = [cm.prob_to_evidence(p) for p in market_prices]
#complete_infos = [cm.prob_to_evidence(p) for p in complete_infos]
#average_beliefs = [cm.prob_to_evidence(p) for p in average_beliefs]
#ax2.set(xlabel='complete information belief (bits)', ylabel='aggregated belief (bits)')
#x = np.linspace(min(market_prices), max(market_prices),100)
#ax2.plot(x, x, linestyle='dotted')
#ax2.scatter(complete_infos, market_prices)
#ax2.scatter(complete_infos, average_beliefs, marker = "+")
#
#fig.legend(['x = y (perfect aggregation)', 'Equilibrium Market Price', 'Average Agent Belief'])
#plt.show()

