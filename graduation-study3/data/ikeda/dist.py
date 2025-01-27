



import glob 
import numpy as np
from ordpy import ordinal_distribution, ordinal_sequence
from stats_func import *
# import os



paths = glob.glob("aaft/u090/**.npy")
print(paths)

for i, path in enumerate(paths):
    data = np.load(path)
    x = data[:, 0]
    pats, probs = ordinal_distribution(x, dx=6, return_missing=True)
    probs = probs*len(ordinal_sequence(x, dx=6)) #回数を出す
    
    probs[probs<100] = 0
    probs = sort_probs(pats, probs)
    np.save(f"dist2/aaft/dist_{i}", probs)