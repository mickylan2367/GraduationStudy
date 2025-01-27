

import numpy as np
import matplotlib.pyplot as plt
from ordpy import ordinal_distribution
import glob
from stats_func import *
import tqdm
import random

uniform_dist = [1/720]*720

# ikeda map u=0.9
ikeda = glob.glob("data/ikeda/dist/original/u090/**.npy")
surrogates = glob.glob("data/ikeda/dist/aaft/u090/**.npy")
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
        ikedaSUD.append(chstwo(probs1, probs2))
    

ikedaSUD = random.sample(ikedaSUD, 100)
ikedaP = np.load(ikeda[0])

# 一旦パス読み直し
del surrogates
surrogates = glob.glob("data/ikeda/dist/aaft/u090/**.npy")
for ss in tqdm.tqdm(surrogates):
    probs1 = np.load(ss)
    ikedaORD.append(chstwo(probs1, ikedaP))


# ikeda map u=0.8
# originals = glob.glob("data/ikeda/dist/original/u008/**.npy")
# surrogates = glob.glob("data/ikeda/dist/aaft/u008/**.npy")
# surrogates2 = surrogates
# ikedaSUD2 = []
# ikedaORD2 = []

# for ss in tqdm.tqdm(surrogates):
#     probs1 = np.load(ss)
#     surrogates2.remove(ss)
    
#     for st in surrogates2:
#         probs2 = np.load(st)
#         ikedaSUD2.append(chstwo(probs1, probs2))

# ikedaSUD2 = random.sample(ikedaSUD2, 100)
# ikedaP2 = np.load(originals[0])
# for ss in tqdm.tqdm(surrogates):
#     probs1 = np.load(ss)
#     ikedaORD2.append(chstwo(probs1, ikedaP2))



# henon map
henon = glob.glob("data/henon/dist/original/**.npy")
surrogates = glob.glob("data/henon/dist/aaft/00/**.npy")
surrogates2 = surrogates
henonSUD = []
henonORD = []

for ss in tqdm.tqdm(surrogates):
    probs1 = np.load(ss)
    surrogates2.remove(ss)
    
    for st in surrogates2:
        probs2 = np.load(st)
        henonSUD.append(chstwo(probs1, probs2))

henonSUD = random.sample(henonSUD, 100)
henonP = np.load(henon[0])

del surrogates
surrogates = glob.glob("data/henon/dist/aaft/00/**.npy")
for ss in tqdm.tqdm(surrogates):
    probs1 = np.load(ss)
    henonORD.append(chstwo(probs1, henonP))



# standard
standard = glob.glob("data/standard/dist/original/**.npy")
surrogates = glob.glob("data/standard/dist/aaft/**.npy")
surrogates2 = surrogates
stdSUD = []
stdORD = []

for ss in tqdm.tqdm(surrogates):
    probs1 = np.load(ss)
    surrogates2.remove(ss)
    
    for st in surrogates2:
        probs2 = np.load(st)
        stdSUD.append(chstwo(probs1, probs2))

stdSUD = random.sample(stdSUD, 100)
stdP = np.load(standard[0])

del surrogates
surrogates = glob.glob("data/standard/dist/aaft/**.npy")
for ss in tqdm.tqdm(surrogates):
    probs1 = np.load(ss)
    stdORD.append(chstwo(probs1, stdP))
print(len(stdORD), len(henonORD), len(ikedaORD))



plt.rcParams["axes.labelsize"] = 20
#########################
## ここから先、描画のみ。##
#########################
data = np.concatenate([
    np.array(ikedaSUD), np.array(ikedaORD), [chstwo(ikedaP, uniform_dist)],
    # np.array(ikedaSUD2), np.array(ikedaORD2), [chstwo(ikedaP2, uniform_dist)],
    np.array(henonSUD), np.array(henonORD), [chstwo(henonP, uniform_dist)],
    np.array(stdSUD), np.array(stdORD), [chstwo(stdP, uniform_dist)]
])
n_bin = 100
x_max = np.max(data)
x_min = np.min(data)
bins = np.linspace(x_min, x_max, n_bin)


data = [
    ikedaSUD, ikedaORD,
    henonSUD, henonORD,
    stdSUD, stdORD
]

labels = [
    "ikeda:surrogate-surrogate","ikeda:chaos-surrogate",
    "henon:surrogate-surrogate","henon:chaos-surrogate",
    "standard:surrogate-surrogate","standard:chaos-surrogate"
]

colormap = plt.cm.inferno  # 使用するカラーマップ
colors = [colormap(i) for i in np.linspace(0, 1, 10)]  # 0から1までの範囲で色を10個生成

plt.figure(figsize=(8, 5))
for d_, c_, l_ in zip(data, colors, labels):
    plt.hist(d_, bins=bins, color=c_, label=l_, alpha=0.8)

data = [
    chstwo(ikedaP, uniform_dist), chstwo(henonP, uniform_dist), chstwo(stdP, uniform_dist)
]

colormap = plt.cm.viridis
colors2 = [colormap(i) for i in np.linspace(0, 2, 5)]

for d_, c_ in zip(data, colors2):
    plt.vlines(d_, 0, 101, color=c_, linestyles='dotted')

plt.ylabel("occurence")
plt.xlabel("$\chi^2$")
plt.legend()

