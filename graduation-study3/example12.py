




import numpy as np
import matplotlib.pyplot as plt
from ordpy import ordinal_distribution
import glob
from stats_func import *
import tqdm
import random


# henon map
henon = glob.glob("data/henon/dist/original/**.npy")
surrogates = glob.glob("data/henon/dist/aaft/00/**.npy")
surrogates = surrogates[:20]
surrogates2 = surrogates
henonSUD = []
henonORD = []

for ss in tqdm.tqdm(surrogates):
    probs1 = np.load(ss)
    surrogates2.remove(ss)
    
    for st in surrogates2:
        probs2 = np.load(st)
        henonSUD.append(chstwo(probs1, probs2))

henonSUD = random.sample(henonSUD, 10)


probs = np.load(henon[0])

for ss in tqdm.tqdm(surrogates):
    probs1 = np.load(ss)
    henonORD.append(chstwo(probs1, probs))

uniform_dist = [1/720]*720


data = np.concatenate([np.array(henonSUD), np.array(henonORD), [chstwo(probs, uniform_dist)]])
n_bin = 100
x_max = np.max(data)
x_min = np.min(data)
bins = np.linspace(x_min, x_max, n_bin)

plt.figure(figsize=(8, 5))
plt.hist(henonSUD, bins=bins, color="blue")
plt.hist(henonORD, bins=bins, color="red")
plt.hist(chstwo(probs, uniform_dist),  bins =bins, color="green")




