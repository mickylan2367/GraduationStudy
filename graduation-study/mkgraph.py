

import matplotlib.pyplot as plt
import numpy as np
import ordpy as ord


# def logistic(a):  
#     x = [np.random.rand()]
#     for i in range(10000):
#         x.append(a * x[-1] * (1 - x[-1]))
#     return x # 後ろから100番目以降の配列を取得（収束済みと踏んでいる）


# #calculate entropy
# ent = []
# dx = 4
pa = np.linspace(3.5, 4.0, 4000) #stepsize 10^(-4)
# print("calculating...")
# for a in pa:
#     x = logistic(a)
#     ent.append(ord.permutation_entropy(x, dx=dx, taux=1)) 

ent = np.load("ent.npy")
print("drawing...")

# 描画
plt.figure(figsize=(8, 6))
# plt.title("Permutation Entropy", fontsize=30, loc="left")
plt.scatter(pa, ent, s=1.7)
# plt.ylabel("Permutation entropy", fontsize=30)
# plt.xlabel("Parameter r of the Logistic map", fontsize=30)
plt.grid()
plt.tight_layout(pad=0.5)
plt.show()
plt.savefig("mkgraph.png")
ent = []
    
    