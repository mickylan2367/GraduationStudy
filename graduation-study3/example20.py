
import numpy as np
import glob
import matplotlib.pyplot as plt
from ordpy import ordinal_distribution, ordinal_sequence, ordinal_network, complexity_entropy
import tqdm
import random


###################
##  standard map ##
###################

paths_standard = glob.glob("data/standard/dist/aaft/**.npy")
ent1_standard = list()
ent2_standard = list()

for path in paths_standard:
    xx = complexity_entropy(np.load(path), dx=6, probs=True)
    ent1_standard.append(xx[0])
    ent2_standard.append(xx[1])


#############################################
# Diff between surrogate and surrogate #
#############################################

# entropy1
enn1_standard = ent1_standard
ENT1_standard = list() # list of conserving data
for x in tqdm.tqdm(ent1_standard):
    enn1_standard.remove(x)
    for y in enn1_standard:
        ENT1_standard.append(x-y)
ENT1_standard = random.sample(ENT1_standard, 100)

# entropy2
enn2_standard = ent2_standard
ENT2_standard = list() # list of conserving data
for x in tqdm.tqdm(ent2_standard):
    enn2_standard.remove(x)
    for y in enn2_standard:
        ENT2_standard.append(x-y)
ENT2_standard = random.sample(ENT2_standard, 100)


##################################################
# Diff between original chaos and surrogate #
##################################################
xx_standard = complexity_entropy(np.load("data/standard/dist/original/dist_0.npy"), dx=6, probs=True)

paths_standard = glob.glob("data/standard/dist/aaft/**.npy")
ent1_standard = list()
ent2_standard = list()

for path in paths_standard:
    xx = complexity_entropy(np.load(path), dx=6, probs=True)
    ent1_standard.append(xx[0])
    ent2_standard.append(xx[1])

diff1_standard = ent1_standard - xx_standard[0]
diff2_standard = ent2_standard - xx_standard[1]
print(len(ent1_standard))
print(len(diff1_standard))

###################
##  ikeda map ##
###################

paths_ikeda = glob.glob("data/ikeda/dist/aaft/u090/**.npy")
ent1_ikeda = list()
ent2_ikeda = list()

for path in paths_ikeda:
    xx = complexity_entropy(np.load(path), dx=6, probs=True)
    ent1_ikeda.append(xx[0])
    ent2_ikeda.append(xx[1])


#############################################
# Diff between surrogate and surrogate #
#############################################

# entropy1
print(len(ent1_ikeda))
enn1_ikeda = ent1_ikeda
ENT1_ikeda = list() # list of conserving data
for x in tqdm.tqdm(ent1_ikeda):
    enn1_ikeda.remove(x)
    for y in enn1_ikeda:
        ENT1_ikeda.append(x-y)
ENT1_ikeda = random.sample(ENT1_ikeda, 100)

# entropy2
enn2_ikeda = ent2_ikeda
ENT2_ikeda = list() # list of conserving data
for x in tqdm.tqdm(ent2_ikeda):
    enn2_ikeda.remove(x)
    for y in enn2_ikeda:
        ENT2_ikeda.append(x-y)
ENT2_ikeda = random.sample(ENT2_ikeda, 100)


##################################################
# Diff between original chaos and surrogate #
##################################################
xx_ikeda = complexity_entropy(np.load("data/ikeda/dist/original/u090/dist_0.npy"), dx=6, probs=True)

paths_ikeda = glob.glob("data/ikeda/dist/aaft/u090/**.npy")
ent1_ikeda = list()
ent2_ikeda = list()

for path in paths_ikeda:
    xx = complexity_entropy(np.load(path), dx=6, probs=True)
    ent1_ikeda.append(xx[0])
    ent2_ikeda.append(xx[1])

diff1_ikeda = ent1_ikeda - xx_ikeda[0]
diff2_ikeda = ent2_ikeda - xx_ikeda[1]


########################
## ここから先描画の調整 ##
########################

# 軸の調整
bins0 = np.concatenate([diff1_standard, ENT1_standard, diff1_ikeda, ENT1_ikeda])
bins0 = np.nan_to_num(bins0, nan=np.nanmean(bins0))
n_bin = 100
x_max = np.max(bins0)
x_min = np.min(bins0)
bins0 = np.linspace(x_min, x_max, n_bin)

bins1 = np.concatenate([diff2_standard, ENT2_standard, diff2_ikeda, ENT2_ikeda])
bins1 = np.nan_to_num(bins1, nan=np.nanmean(bins1))
x_max = np.max(bins1)
x_min = np.min(bins1)
bins1 = np.linspace(x_min, x_max, n_bin)

# 描画
plt.rcParams['axes.titlesize'] = 23
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['legend.fontsize'] = "x-large"
plt.rcParams['xtick.labelsize'] = "x-large"  # font size of the tick labels
fig, axes = plt.subplots(2, 1, figsize=(10, 14))

# Shannon Entropy
axes[0].set_title("Shannon Entropy")
axes[0].set_xlabel("Difference of Shanon Entropy, $D_h$")
axes[0].set_ylabel("Occurance")
axes[0].hist(diff1_standard, bins=bins0, label=" Standard map : $H_{surrogate} - H_{chaos}$", alpha=0.5)
axes[0].hist(ENT1_standard, bins=bins0, label=" Standard Map: $H_{surrogate} -H_{surrogate}$", alpha=0.5)
axes[0].hist(diff1_ikeda, bins=bins0, label=" Ikeda Map : $H_{surrogate} - H_{chaos}$", alpha=0.5)
axes[0].hist(ENT1_ikeda, bins=bins0, label=" Ikeda Map : $H_{surrogate} - H_{surrogate}$", alpha=0.5)

# Statistical Complexity
axes[1].set_title("Statistical Complexity")
axes[1].set_xlabel("Difference of Statistical Complexity, $D_c$")
axes[1].set_ylabel("Occurance")
axes[1].hist(diff2_standard, bins=bins1, label=" Standard Map : $C_{surrogate} - C_{chaos}$", alpha=0.5)
axes[1].hist(ENT2_standard, bins=bins1, label=" Standard Map : $C_{surrogate} - C_{surrogate}$", alpha=0.5)
axes[1].hist(diff2_ikeda, bins=bins1, label=" Ikeda Map : $C_{surrogate} - C_{chaos}$", alpha=0.5)
axes[1].hist(ENT2_ikeda, bins=bins1, label=" Ikeda Map : $C_{surrogate} - C_{surrogate}$", alpha=0.5)

for ax in axes:
    ax.legend()

plt.subplots_adjust(hspace=1.1)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show();
