

import numpy as np
import matplotlib.pyplot as plt
from ordpy import complexity_entropy, maximum_complexity_entropy, minimum_complexity_entropy, ordinal_distribution, permutation_entropy
import warnings
import matplotlib as mpl
import matplotlib.image as mpimg

import string
import glob
import warnings
import math
from PIL import Image
# import seaborn as sns


def make_label(pis):
    label = []
    for l in pis:
        label.append(''.join(map(str, l)))
    return label


#Skew tent map
def skew_tent_map(n=2**15, omega=0.1847, x0=.5):
    """
    Iterates the Skew tent map.
    
    Parameters
    ----------
    n     : time series length.
    omega : map parameter.
    x0    : initial condition.
    ----------
    Returns an array corresponding to a 
    time series.
    """
    x    = np.zeros(n)
    x[0] = x0
    
    for i in range(1, len(x)):
        if x[i-1] < omega:
            x[i] = x[i-1]/omega
        else:
            x[i] = (1-x[i-1])/(1-omega)
    
    return x


#Schuster's map
def schuster_map(n=2**15, z=2, x0=.5):
    """
    
    Parameters
    ----------
    n : time series length
    z :  map parameter
    ----------
    Returns an orbit of an iterated Schuster map.
    """
    z    = float(z)
    x    = np.zeros(n)
    x[0] = x0
    
    for i in range(1, n):
        x[i], _ = np.modf(x[i-1] + x[i-1]**z)
    
    return x

# Download things
# Henon map
def hc_henon():
    print("calculating henon hc")
    paths = glob.glob("data/henon/original/henon_*.npy")
    HCX=list()
    HCY = list()
    for path in paths:
        data = np.load(path)
        hcx = complexity_entropy(data[:, 0], dx=6)
        hcy = complexity_entropy(data[:, 1], dx=6)
        HCX.append(hcx)
        HCY.append(hcy)
    x_mean = np.mean(np.array(HCX), axis=0)
    y_mean = np.mean(np.array(HCY), axis=0)
    return x_mean, y_mean

# Additional Logistic Map
def hc_logistic():
    data = np.load("data/hc/hc_logistic.npy")
    return data

def hc_ikeda_original():
    data = np.load("data/hc/hc_ikeda.npy")
    return data

def hc_ikeda_aaft():
    data = np.load("data/hc/hc_ikeda_aaft_dx6.npy")
    return data

def hc_ikeda_short():
    data = np.load("data/hc/hc_ikeda_short_dx6.npy")
    return data

def hc_standard_original():
    print("calculating hc of standard original")
    path = "data/standard/original/standard.npy"
    data = np.load(path)
    hcx = np.array(complexity_entropy(data[:, 0], dx=6))
    return hcx

def hc_standard_aaft():
    print("calculating hc of surrodate data of standard map")
    return np.load("hc/hc_standard_aaft_dx6.npy")


def stdfigsize(scale=1, nrows=1, ncols=1, ratio=1.5):
    """
    Returns a tuple to be used as figure size.

    Parameters
    ----------
    returns (7*ratio*scale*nrows, 7.*scale*ncols)
    By default: ratio=1.3
    ----------
    Returns (7*ratio*scale*nrows, 7.*scale*ncols).
    """

    return((7*ratio*scale*ncols, 15.*scale*nrows))
