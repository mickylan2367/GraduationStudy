

import colorednoise
import numpy as np
kk =  np.arange(0, 3.1, .25).round(decimals=2)
ent0 = list()
ent1 = list()

for k_ in kk:
    x = colorednoise.powerlaw_psd_gaussian(exponent=k_, size=2**15)
    np.save(f"knoise{k_*100}", x)