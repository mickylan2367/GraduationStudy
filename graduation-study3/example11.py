


import numpy as np
import matplotlib.pyplot as plt
from ordpy import ordinal_distribution
import glob
from stats_func import *

def make_label(pis):
    label = []
    for l in pis:
        label.append(''.join(map(str, l)))
    return label

def sort_probs(pats, probs):
    probs = np.array(probs)
    probs = probs[np.argsort(make_label(pats))]
    return probs

# henon map
originals = glob.glob("data/henon/original/**.npy")
surrogates = glob.glob("data/henon/aaft/try01/**.npy")

data1 = np.load(originals[0])
x1 = data1[:, 0]

data2 = np.load(surrogates[0])
x2 = data2[:, 0]


pats1, probs1 = ordinal_distribution(x1, dx=6,return_missing=True)
pats2, probs2  = ordinal_distribution(x2, dx=6, return_missing=True)

probs1 = sort_probs(pats1, probs1)
probs2 = sort_probs(pats2, probs2)

print(chstwo(probs1, probs2))