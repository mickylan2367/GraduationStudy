

import numpy as np
import glob

def Logistic(n=2**15, a=4.0, x0=np.random.random()):
    x = np.zeros(n)
    x[0] = x0
    
    for i in range(1, n):
        x[i] = a*x[i-1]*(1-x[i-1])
    return x


count = 10

for cnt in range(count):
    data = Logistic(a=3.85555)
    path = f"original/a38555/data38555_{cnt}"
    np.save(path, data)