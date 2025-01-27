


import numpy as np
import matplotlib.pyplot as plt
from ordpy import complexity_entropy, maximum_complexity_entropy, minimum_complexity_entropy, ordinal_distribution
import warnings
import matplotlib as mpl
import matplotlib.image as mpimg

import string
import glob
import warnings
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
        # hc_henon_x, hc_henon_y = np.mean(
        # [
        #     [complexity_entropy(_, dx=6),complexity_entropy(y_, dx=6)]
        # for x_, y_ in [(henon_map(x0=np.random.uniform(), y0=np.random.uniform())) for _ in range(10)]],
        # axis=0)
        hcx = complexity_entropy(data[:, 0], dx=6)
        hcy = complexity_entropy(data[:, 1], dx=6)
        HCX.append(hcx)
        HCY.append(hcy)
    x_mean = np.mean(np.array(HCX), axis=0)
    y_mean = np.mean(np.array(HCY), axis=0)
    return x_mean, y_mean

# Additional Logistic Map
def hc_original_LM():
    print("calculating original logistic map hc")
    original_path = glob.glob("data/logistic/original/original_*.txt")
    data = []
    for path in original_path:
        hc = complexity_entropy(np.loadtxt(path), dx=6)
        data.append(hc)

    if np.isscalar(data):
        data = np.array([data])
    return np.mean(data, axis=0)

def hc_shuffle_LM():
    print("calculating shuffle logistic map hc")
    surrogate_path = glob.glob("data/logistic/shuffle/surrogate_*.txt")
    data = []
    for path in surrogate_path:
        hc = complexity_entropy(np.loadtxt(path), dx=6)
        data.append(hc)

    if np.isscalar(data):
        data = np.array([data])
    return np.mean(data, axis=0)

def hc_aaft_LM():
    print("calculating aaft logistic map hc")
    aaft_path = glob.glob("data/logistic/aaft/aaft_*.txt")
    data = []
    for path in aaft_path:
        hc = complexity_entropy(np.loadtxt(path), dx=6)
        data.append(hc)

    if np.isscalar(data):
        data = np.array([data])
    return np.mean(data, axis=0)


def hc_ikeda_original():
    print("calculating ikeda original")
    path = "data/ikeda/original/ikeda.npy"
    data = np.load(path)
    hcx = np.array(complexity_entropy(data[:, 0], dx=6))
    hcy = np.array(complexity_entropy(data[:, 1], dx=6))
    return hcx, hcy

def hc_ikeda_aaft():
    print("calculating ikeda aaft")
    px = "data/ikeda/aaft/ikeda_AAFT_x.npy"
    py = "data/ikeda/aaft/ikeda_AAFT_y.npy"
    hcx = np.array(complexity_entropy(np.load(px), dx=6))
    hcy = np.array(complexity_entropy(np.load(py), dx=6))
    return hcx, hcy


def hc_standard_original():
    print("calculating standard original")
    path = "data/standard/original/standard.npy"
    data = np.load(path)
    hcx = np.array(complexity_entropy(data[:, 0], dx=6))
    hcy = np.array(complexity_entropy(data[:, 1], dx=6))
    return hcx, hcy

def hc_standard_aaft():
    print("calculating standard aaft")
    px = "data/standard/aaft/standard_AAFT_x.npy"
    py = "data/standard/aaft/standard_AAFT_y.npy"
    hcx = np.array(complexity_entropy(np.load(px), dx=6))
    hcy = np.array(complexity_entropy(np.load(py), dx=6))
    return hcx, hcy


def hc_monet():
    data = np.array(Image.open("data/paper/fig3/monet_01322.jpg"))
    hcr = np.array(complexity_entropy(data[0], dx=2, dy=2))
    hcb = np.array(complexity_entropy(data[1], dx=2, dy=2))
    hcg = np.array(complexity_entropy(data[2], dx=2, dy=2))
    return (hcr, hcb, hcg)

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

    return((7*ratio*scale*ncols, 8.*scale*nrows))