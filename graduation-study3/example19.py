


import numpy as np
import glob
import matplotlib.pyplot as plt
from ordpy import ordinal_distribution, ordinal_sequence, ordinal_network, complexity_entropy
import tqdm
import random


###################
##  standard map ##
###################

paths = glob.glob("data/standard/dist/aaft/**.npy")
ent1 = list()
ent2 = list()

for path in paths:
    xx = complexity_entropy(np.load(path), dx=6, probs=True)
    ent1.append(xx[0])
    ent2.append(xx[1])


#############################################
# Diff between surrogate and surrogate #
#############################################

# entropy1
enn1 = ent1
ENT1 = list() # list of conseving data
for x in tqdm.tqdm(ent1):
    enn1.remove(x)
    for y in enn1:
        ENT1.append(x-y)
ENT1 = random.sample(ENT1, 100)

# entropy2
enn2 = ent2
ENT2 = list() # list of conseving data
for x in tqdm.tqdm(ent2):
    enn2.remove(x)
    for y in enn2:
        ENT2.append(x-y)
ENT2 = random.sample(ENT2, 100)


##################################################
# Diff between original chaos and surrogate #
##################################################
xx = complexity_entropy(np.load("data/standard/dist/original/dist_0.npy"), dx=6, probs=True)
diff1 = ent1 - xx[0]
diff2 = ent2 - xx[1]



########################
## ここから先描画の調整 ##
########################

# 軸の調整
bins0 = np.concatenate([diff1, ENT1])
bins0 = np.nan_to_num(bins0, nan=np.nanmean(bins0))
n_bin = 100
x_max = np.max(bins0)
x_min = np.min(bins0)
bins0 = np.linspace(x_min, x_max, n_bin)

bins1 = np.concatenate([diff2, ENT2])
bins1 = np.nan_to_num(bins1, nan=np.nanmean(bins1))
x_max = np.max(bins1)
x_min = np.min(bins1)
bins1 = np.linspace(x_min, x_max, n_bin)

# 描画
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
fig.suptitle("standard map")
axes[0].set_title("Shanonn Entropy")
axes[0].hist(diff1, bins=bins0, label="chaos-surrogate")
axes[0].hist(ENT1, bins=bins0, label="surrogate-surrogate")

axes[1].set_title("Statistical Complexity")
axes[1].hist(diff2, bins=bins1, label="chaos-surrogate")
axes[1].hist(ENT2, bins=bins1, label="surrogate-surrogate")

axes[0].legend()
axes[1].legend()
plt.show();