For these experiments I'm using the following method to get each endowment profile:
1)Give each agent a number of shares sampled from Binomial(100,0.5)
2)Give each agent an endowment proportional to the number of shares such that the endowment profile sums to 1

Furthermore, for the weighted average aggregation, I take an average of all the agents' beliefs, weighted by their endowment.

Lastly, the signals are sampled using each agent's error rate.
