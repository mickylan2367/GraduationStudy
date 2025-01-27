


import numpy as np
import matplotlib.pyplot as plt
import glob

filepath = glob.glob("original/**/")
filepath = filepath[:len(filepath)-1]
datapath = []

# Search Whether Chaos or not : Lyapunov
def diff_ikeda(data, u):
    # x: array
    # y:array
    x = data[:, 0]
    y = data[:, 1]
    theta = [0.4 - 6/(1+x[n-1]**2+y[n-1]**2) for n in range(1, len(x)+1)]
    diff = -u * np.cos(theta) * 12*x/(1+x**2 + y**2)
    return diff

def Lyapunov_exponent(u, data):
    y = np.array([np.log(np.abs(diff_ikeda(data, u)))])
    sum_y = np.nansum(y)
    sum_y /= len(data[:, 0])
    return sum_y

lyapnov_exponent = []


for fp in filepath:
    dp = glob.glob(fp+"**.npy")
    datapath.append(dp[0])

u = [0.1, 0.3, 0.6, 0.8, 0.85, 0.9, 0.92]
fig, axes=plt.subplots(4, 2, figsize=(10, 20))
# lyap = []
for i, dp in enumerate(datapath):
    data = np.load(dp)
    # lyap.append(Lyapunov_exponent(data))
    axes[i//2, i%2].scatter(data[:, 0], data[:, 1], s=0.8)
    axes[i//2, i%2].set_title("u="+str(u[i]))
    lyapnov_exponent.append(Lyapunov_exponent(data=data, u=u[i]))
axes[3, 1].plot(u, lyapnov_exponent)
axes[3, 1].set_title("Lyapnov Exponent")
plt.savefig("ikedamap.png")