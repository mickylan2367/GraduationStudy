

import numpy as np
import warnings
import os
import argparse

def ikeda_map(n=2**15, u=[0.1, 0.1], kappa=0.4, alpha = 6.0, x0=0.6, y0=0.1):
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

    ux = u[0]
    uy = u[1]

    with warnings.catch_warnings():
        warnings.simplefilter("error")

        bool_ = False
        while bool_ == False:
            try:
                x = np.zeros(n)
                y = np.zeros(n)

                x[0] = x0
                y[0] = y0

                for i in range(1, n):
                    theta = kappa - alpha/(1+x[i-1]**2 + y[i-1]**2)
                    x[i] = 1+ux*(x[i-1]*np.cos(theta) - y[i-1]*np.sin(theta))
                    y[i] = uy*(x[i-1] *np.sin(theta) + y[i-1]*np.cos(theta))

                bool_ = True
            
            except RuntimeError:
                x0 = np.random.uniform()
                y0 = np.random.uniform()
    return x, y

