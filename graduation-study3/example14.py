



import numpy as np
import matplotlib.pyplot as plt
from ordpy import ordinal_distribution
import glob
from stats_func import *
import tqdm
import random

# ikeda map u=0.9
ikeda = glob.glob("data/ikeda/dist/original/u090/**.npy")
surrogates = glob.glob("data/ikeda/dist/aaft/u090/**.npy")
surrogates2 = surrogates
data = []

for ss in tqdm.tqdm(surrogates):
    if len(surrogates2)==0:
        break

    probs1 = np.load(ss)
    surrogates2.remove(ss)
    for st in surrogates2:
        probs2 = np.load(st)
        data.append(chstwo(probs1, probs2))

#########################
## ここから先、描画のみ。##
#########################
n_bin = 100
x_max = np.max(data)
x_min = np.min(data)
bins = np.linspace(x_min, x_max, n_bin)



plt.rcParams["axes.labelsize"] = 20
plt.figure(figsize=(8, 5))
plt.ylabel("occurence")
plt.xlabel("$\chi^2$")
plt.hist(data, bins=bins, color="blue", label="surrogate", alpha=0.8)
plt.tight_layout()
plt.show();