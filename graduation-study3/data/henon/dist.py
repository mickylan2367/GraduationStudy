



import glob 
import numpy as np
from ordpy import ordinal_distribution
from stats_func import *
# import os

paths = glob.glob("aaft/try00/**.npy")

for i, path in enumerate(paths):
    data = np.load(path)
    x = data[:, 0]
    pats, probs = ordinal_distribution(x, dx=6, return_missing=True)

    probs = sort_probs(pats, probs)
    np.save(f"dist/aaft/00/dist_{i}", probs)