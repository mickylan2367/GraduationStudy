

import numpy as np
import matplotlib.pyplot as plt


data = np.load("ikedamap_complex.npy") #include transient(first 1000 data)
tec = np.loadtxt("ikeda.txt")
fis = np.load("ikedamap.npy")
tec = tec[:, 1:] 
data = data[:, :1000].T
fis = fis[:, :1000]
# data = data.T-tec

plt.figure(figsize=(12, 8))
plt.scatter(data[:, 0], data[:, 1], label="python", s=0.3)
plt.scatter(tec[:, 0], tec[:, 1], label="teacher", s=0.3)
plt.scatter(fis[:, 0], fis[:, 1], label="wikipedia one", s=0.3)
plt.title("scatter plots calculated by Professor and ME")
# plt.title("difference between values calculated by Professor and ones of my program")
# plt.plot(np.arange(0, len(data[:, 0])), data[:, 0], label="x cordinate", c="blue", markersize=0.2, linewidth=0.3)
# plt.plot(np.arange(0, len(data[:, 1])), data[:, 1], label="y cordinate", c="red", markersize=0.2, linewidth=0.3)
# plt.xlim([0, 200])
plt.legend()
plt.show()