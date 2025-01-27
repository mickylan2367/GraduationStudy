

from functions改2 import *
import numpy as np
from ordpy import complexity_entropy, ordinal_sequence

# data = np.load("data/ikeda/original/u090/ikeda_090_0.npy")

import numpy as np
import warnings
import os
import argparse

def ikeda_map(n=2**15+1000, u=0.9, kappa=0.4, alpha = 6.0, x0=0., y0=0.):
    """
    n:time series length
    kappa : 0.4
    alpha : 0.6

    u:0.8
    x0 : initial condition
    y0: initial condition
    =============================
    Returns the x and y variables of Ikeda map
    """
    with warnings.catch_warnings():
        warnings.simplefilter("error")

        bool_ = False
        while bool_ == False:
            try:
                x = np.zeros(n, dtype="f16")
                y = np.zeros(n, dtype="f16")

                x[0] = x0
                y[0] = y0

                for i in range(1, n):
                    theta = kappa - alpha/(1+x[i-1]**2 + y[i-1]**2)
                    x[i] = 1+u*(x[i-1]*np.cos(theta) - y[i-1]*np.sin(theta))
                    y[i] = u*(x[i-1] *np.sin(theta) + y[i-1]*np.cos(theta))

                bool_ = True
            
            except RuntimeError:
                x0 = np.random.uniform()
                y0 = np.random.uniform()
    return x, y


data = ikeda_map()
x = data[0]
y = data[1]
# x = x[1000:]

np.save("ikedamap", np.stack([x, y], axis=1))
# print(x.dtype)
# os = ordinal_sequence(x, dx=6)


# def make_label(pis):
#     label = []
#     for l in pis:
#         label.append(''.join(map(str, l)))
#     return label

# os = make_label(os)
# print(os[0])
# print(os.count('402315'))
