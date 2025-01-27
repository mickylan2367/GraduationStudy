




import numpy as np
import matplotlib.pyplot as plt
from ordpy import ordinal_distribution, complexity_entropy, permutation_entropy
import glob
from stats_func import *
import tqdm
import random

uniform_dist = [1/720]*720

# Unfiltered (original) data
origin = glob.glob("data/ikeda/dist/original/u090/**.npy")
surrogates = glob.glob("data/ikeda/dist/aaft/u090/**.npy")
surrogates2 = surrogates
originPER = []
originSUD = []

for ss in tqdm.tqdm(surrogates):
    probability = np.load(ss)
    originPER.append(permutation_entropy(probability, probs = True))


    
#########################
## ここから先、描画のみ。##
#########################

####################
# 1. 描画範囲の設定 #
####################
data = np.concatenate([
    np.array(originSUD), np.array(originSUD), [chstwo(originP, uniform_dist)],
    np.array(ikedaSUD), np.array(ikedaORD), [chstwo(ikedaP, uniform_dist)]
])
n_bin = 100
x_max = np.max(data)
x_min = np.min(data)
bins = np.linspace(x_min, x_max, n_bin)

###########
# 2. 描画 #
###########

data = [
    originSUD, originORD,
    # ikedaSUD, ikedaORD
]

labels = [
    "Unfiltered:surrogate-surrogate","Unfiltered:chaos-surrogate",
    "filtered:surrogate-surrogate","filtered:chaos-surrogate"
]

colormap = plt.cm.inferno  # 使用するカラーマップ
colors = [colormap(i) for i in np.linspace(0, 1, 6)]  # 0から1までの範囲で色を10個生成

plt.figure(figsize=(8, 5))
for d_, c_, l_ in zip(data, colors, labels):
    plt.hist(d_, bins=bins, color=c_, label=l_, alpha=0.8)

plt.vlines(chstwo(ikedaP, uniform_dist), 0, 101, color="red", linestyles='dotted')
plt.vlines(chstwo(originP, uniform_dist), 0, 101, color="blue", linestyles='dotted')
plt.legend()