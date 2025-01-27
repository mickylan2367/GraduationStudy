


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

ikedaP = np.load(ikeda[0])
for ss in tqdm.tqdm(surrogates):
    probs1 = np.load(ss)
    data.append(chstwo(probs1, ikedaP))

#########################
## ここから先、描画のみ。##
#########################
n_bin = 100
x_max = np.max(data)
x_min = np.min(data)
bins = np.linspace(x_min, x_max, n_bin)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=bins, color="blue", label="surrogates", alpha=0.8)