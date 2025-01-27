

# from functions改2 import *
import numpy as np
# from ordpy import complexity_entropy, ordinal_sequence
import cmath


# data = np.load("data/ikeda/original/u090/ikeda_090_0.npy")
import warnings
import os

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
                z = np.zeros(n, dtype = 'complex_')
                z0 = complex(x0, y0)

                for i in range(1, n):
                    z2 = z[i-1].real**2 + z[i-1].imag**2
                    z[i] = 1+u*z[i-1]*np.exp(complex(0, 1)*(kappa-alpha/(1+z2)))
                bool_ = True
            
            except RuntimeError:
                x0 = np.random.uniform()
                y0 = np.random.uniform()

    # discard first 1000
    z = z[1000:]
    return z


z = ikeda_map()
np.save("ikedamap_complex", [z.real, z.imag])


