


import numpy as np
import matplotlib.pyplot as plt
from ordpy import ordinal_distribution
import glob
from stats_func import *
import tqdm
import random

uniform_dist = [1/720]*720
N = 2**15 - 5

# Unfiltered (original) data
origin = glob.glob("data/ikeda/dist/original/u090/**.npy")
surrogates = glob.glob("data/ikeda/dist/aaft/u090/**.npy")
surrogates2 = surrogates
originSUD = []
originORD = []

for ss in tqdm.tqdm(surrogates):
    if len(surrogates2) == 0:
        break

    probs1 = np.load(ss)
    surrogates2.remove(ss)
    for st in surrogates2:
        probs2 = np.load(st)
        originSUD.append(chstwo(probs1, probs2))

originSUD = random.sample(originSUD, 100)
originP = np.load(origin[0])

# 一旦パス読み直し
del surrogates
surrogates = glob.glob("data/ikeda/dist/aaft/u090/**.npy")
for ss in tqdm.tqdm(surrogates):
    probs1 = np.load(ss)
    originORD.append(chstwo(probs1, originP))


# removed data
ikeda = glob.glob("data/ikeda/dist2/original/**.npy")
surrogates = glob.glob("data/ikeda/dist2/aaft/**.npy")
surrogates2 = surrogates
ikedaSUD = []
ikedaORD = []

for ss in tqdm.tqdm(surrogates):
    if len(surrogates2)==0:
        break

    probs1 = np.load(ss)
    surrogates2.remove(ss)
    for st in surrogates2:
        probs2 = np.load(st)
        ikedaSUD.append(chstwo(probs1/N, probs2/N))
    

ikedaSUD = random.sample(ikedaSUD, 100)
ikedaP = np.load(ikeda[0])

# 一旦パス読み直し
del surrogates
surrogates = glob.glob("data/ikeda/dist2/aaft/**.npy")
for ss in tqdm.tqdm(surrogates):
    probs1 = np.load(ss)
    ikedaORD.append(chstwo(probs1/N, ikedaP/N))

#########################
## ここから先、描画のみ。##
#########################

####################
# 1. 描画範囲の設定 #
####################
data = np.concatenate([
    np.array(originSUD), np.array(originORD), [chstwo(originP, uniform_dist)],
    np.array(ikedaSUD), np.array(ikedaORD), [chstwo(ikedaP/N, uniform_dist)]
])

data = np.nan_to_num(data, nan=np.nanmean(data))
n_bin = 100
x_max = np.max(data)
x_min = np.min(data)
bins = np.linspace(x_min, x_max, n_bin)

print(x_min, x_max)
###########
# 2. 描画 #
###########

data = [
    originSUD, originORD,
    ikedaSUD, ikedaORD
]

labels = [
    "Unfiltered:surrogate-surrogate","Unfiltered:chaos-surrogate",
    "Filtered:surrogate-surrogate","Filtered:chaos-surrogate"
]

colormap = plt.cm.inferno  # 使用するカラーマップ
colors = [colormap(i) for i in np.linspace(0, 1, 6)]  # 0から1までの範囲で色を10個生成

plt.figure(figsize=(8, 5))
for d_, c_, l_ in zip(data, colors, labels):
    plt.hist(d_, bins=bins, color=c_, label=l_, alpha=0.8)

plt.vlines(chstwo(originP, uniform_dist), 0, 101, color="blue", linestyles='dotted')
plt.vlines(chstwo(ikedaP/N, uniform_dist), 0, 101, color="red", linestyles='dotted')
plt.xlabel("chi-square statistic")
plt.legend()

