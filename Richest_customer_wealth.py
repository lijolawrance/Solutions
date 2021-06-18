import numpy as np


def maximumWealth(accounts):
    result = list(map(sum, accounts))
    print(max(np.sum(accounts, axis=1)))
    return max(result)


ac = [[2, 8, 7], [7, 1, 2], [1, 9, 5]]

d = maximumWealth(ac)
print(d)
