

import numpy as np
import matplotlib.pyplot as plt
from make import *

# ファイルへの書き出し
# N = 10

# for n in range(N):
#     x, y = standard_map(theta0=np.random.uniform(), p0=np.random.uniform())
#     data = np.stack([x, y], 1)
#     np.save(f"original/standard_{n}", data)


data = standard_map()
np.save("standard", data)

plt.scatter(data[:, 0],data[:, 1], s=0.0005)
# plt.title("Standard map with parameter k=6.908745", fontsize=20)
plt.xlabel("x")
plt.ylabel("y")
# plt.yticks([-np.pi, np.pi])
plt.tight_layout(pad=0.5)
plt.show()

