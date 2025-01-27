

import numpy as np
import warnings

# standard map
def standard_map(n=2**20, k=6.908745, theta0=np.random.random(), p0=np.random.random()):
    """
    Parameters
    ----------
    n: time series length
    z: map parameter
    ----------
    Returns an orbit of an iterated standard map
    """

    with warnings.catch_warnings():
        warnings.simplefilter("error")

        bool_ = False
        while bool_ == False:
            try:
                theta = np.zeros(n)
                p = np.zeros(n)
    
                theta[0] = np.remainder(theta0, 2*np.pi)
                p[0] = np.remainder(p0, 2*np.pi)
                
                for i in range(1, n):
                    p[i] = np.remainder(p[i-1] + k*np.sin(theta[i-1]), 2*np.pi)
                    theta[i] = np.remainder(theta[i-1] + p[i], 2*np.pi)
                    

                bool_ = True
            
            except RuntimeError: # change the initial condition
                theta0 = np.random.uniform()
                p0 = np.random.uniform()
    
    return np.stack([theta, p], axis=1)
