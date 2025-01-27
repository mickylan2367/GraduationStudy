

import numpy as np
import matplotlib.pyplot as plt
from ordpy import complexity_entropy

n = 100
steps = 5000
x = np.array([np.random.random() for _ in range(n)])
# x = np.array([]*n)
X = []
X.append(x)

ep = 0.3
alpha = 1.7

def logistic(x):
    return 1-alpha*x**2

def global_mapping():
    return (1-ep)*logistic(x) + ep*np.sum(x)/n


for _ in range(steps):
    # print(x)
    x = global_mapping()
    X.append(x)

X = np.array(X)
# print(X[:, 1])

plt.figure(figsize=(12, 8))
time = np.arange(0, steps+1)
for i in range(n):
    plt.scatter(time, X[:, i])
    # plt.plot(time, X[:, i], label=str(i))
plt.title("global coupled map alpha=1.7, ep=0.3")
plt.legend()
plt.show()

np.save("global", X)

# HC = list()
# for i in range(n):
#     hc = complexity_entropy(X[:, i])
#     HC.append(hc)
# np.save(n