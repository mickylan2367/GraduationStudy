

import numpy as np
import matplotlib.pyplot as plt


def sort_probs(pats, probs):

    def make_label(pis):
        label = []
        for l in pis:
            label.append(''.join(map(str, l)))
        return label
    
    probs = np.array(probs)
    probs = probs[np.argsort(make_label(pats))]
    return probs

def chstwo(bins1, bins2, knstrn = 1):
    """
    knstrn is equal, 
    because the data length N of original data is the same with of surrogate data
    """

    nbins = len(bins1)
    df = nbins - knstrn
    chsq = 0.0

    for j in range(nbins):
        if bins1[j] == 0 and bins2[j]==0:
            df = df-1
        else:
            chsq += (bins1[j] - bins2[j])**2 / (bins1[j] + bins2[j])
    return chsq