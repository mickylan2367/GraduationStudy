

import numpy as np
import matplotlib.pyplot as plt

x = np.array([9, 4, 5, 6, 7])


plt.figure(figsize=(8, 5))
plt.xlabel("data X")
plt.plot(np.arange(0, len(x), 1), x, markersize=10, marker="o")
plt.xticks(np.arange(0, len(x), 1))
