


import numpy as np
import matplotlib.pyplot as plt


data = np.load("ikedamap_complex.npy") #include transient(first 1000 data)
tec = np.loadtxt("ikeda.txt")
fis = np.load("ikedamap.npy")
tec = tec[:, 1:] 
data = data[:, :1000].T
fis = fis[:1000]

x = data-tec
y = fis-tec
z = data-fis

plt.figure(figsize=(12, 8))
plt.title("difference between values calculated by Professor and ones of my program")
plt.plot(np.arange(0, len(data[:, 0])), x[:, 0], label="prof and complex", c="blue", markersize=0.2, linewidth=0.3)
plt.plot(np.arange(0, len(data[:, 1])), y[:, 0], label="prof and x-y", c="red", markersize=0.2, linewidth=0.3)
plt.plot(np.arange(0, len(data[:, 1])), z[:, 0], label="x-y and complex", c="green", markersize=0.2, linewidth=0.3)
plt.xlim([0, 200])
plt.legend()
plt.show()