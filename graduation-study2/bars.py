
import glob
import numpy as np
import matplotlib.pyplot as plt
from ordpy import ordinal_distribution

paths0 = glob.glob("data/ikeda/original/u090/**.npy")
paths1 = glob.glob("data/henon/original/**.npy")
ikeda = np.load(paths0[0])
henon = np.load(paths1[0])

def make_label(pis):
    label = []
    for l in pis:
        label.append(''.join(map(str, l)))
    return label

ikeda_PATTERNS = []
ikeda_PROBS = []
henon_PATTERNS = []
henon_PROBS = []
for i in range(3, 7):
    patterns, probs = ordinal_distribution(ikeda[:, 0], dx=i, return_missing=True)
    
    probs = np.array(probs)
    probs = probs[np.argsort(make_label(patterns))]
    patterns = np.sort(make_label(patterns))
    
    ikeda_PATTERNS.append(patterns)
    ikeda_PROBS.append(probs)

    patterns, probs = ordinal_distribution(henon[:, 0], dx=i, return_missing=True)
    
    probs = np.array(probs)
    probs = probs[np.argsort(make_label(patterns))]
    patterns = np.sort(make_label(patterns))
    
    henon_PATTERNS.append(patterns)
    henon_PROBS.append(probs)

# ip = [int(x) for x in patterns for patterns in ikeda_PATTERNS]
# hp = [int(x) for x in patterns for patterns in henon_PATTERNS]

# np.save("ikeda_ordinal_bars", np.stack([ip, ikeda_PROBS], axis=1))
# np.save("henon_ordinal_bars", np.stack([henon_PATTERNS, henon_PROBS], axis=1))
# print(len(henon_PROBS), len(ikeda_PROBS))

# Draw
plt.rcParams['xtick.labelsize'] = 10 # 軸だけ変更されます。
plt.rcParams['ytick.labelsize'] = 10 # 軸だけ変更されます

# 描画
fig, axes = plt.subplots(4, 2, figsize=(10, 14.5))
# fig.suptitle("Ordinal distribution of Ikeda map and Henon map", fontsize=30)
for i in range(0, 4):

    if i ==0:
        axes[i, 0].bar(ikeda_PATTERNS[i], ikeda_PROBS[i])
        axes[i, 0].set_title("$d_x={}$".format(i+3), fontsize=30)
        axes[i, 0].set_ylabel("probability", fontsize=15)
        axes[i, 0].set_xlabel("ordinal sequences", fontsize=15)

        axes[i, 1].bar(henon_PATTERNS[i], henon_PROBS[i])
        axes[i, 1].set_title("$d_x={}$".format(i+3), fontsize=30)
        axes[i, 1].set_xlabel("ordinal sequences", fontsize=15)
    else:
        labels = [int(x) for x in range(1, len(ikeda_PATTERNS[i])+1, int(len(ikeda_PATTERNS[i])/4))]
        labels.append(len(ikeda_PATTERNS[i]))
        print(labels)
        
        axes[i, 0].bar(np.arange(0, len(ikeda_PATTERNS[i]), 1), ikeda_PROBS[i])
        axes[i, 0].set_title("$d_x={}$".format(i+3), fontsize=30)
        axes[i, 0].set_xticks(labels)
        axes[i, 0].set_ylabel("probability", fontsize=15)
        axes[i, 0].set_xlabel("bin numbers", fontsize=15)
        
        axes[i, 1].bar(np.arange(0, len(henon_PATTERNS[i]), 1), henon_PROBS[i])
        axes[i, 1].set_title("$d_x={}$".format(i+3), fontsize=30)
        axes[i, 1].set_xticks(labels)
        axes[i, 1].set_xlabel("bin numbers", fontsize=15)


plt.tight_layout(rect=[0,0,1,0.99], h_pad=1.2, w_pad=1.5)

    