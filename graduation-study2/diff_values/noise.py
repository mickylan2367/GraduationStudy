

# Stochastic processes (filled markers)
# either run or load, to get the k-noise data. 
# To run, you have to install the colorednoise module - 
# https://github.com/felixpatzelt/colorednoise

# import colorednoise
# hc_knoise = np.mean([[
#     complexity_entropy(
#         colorednoise.powerlaw_psd_gaussian(exponent=k_, size=2**15), dx=6)
#     for _ in range(10)
# ] for k_ in np.arange(0, 3.1, .25).round(decimals=2)],
#                     axis=1)
# np.save('data/fig3/hc_knoise.npy', hc_knoise)


# This time series was generated using the C code available in:
# http://www.columbia.edu/~ad3217/fbm/hosking.c
# fbm_ordnet8 = fbm(16,0.8,seed=15)
# np.save('data/fig6/fbm_series_to_ordnets0.8.npy', fbm_ordnet8)

import colorednoise as cn
from ordpy import complexity_entropy
import numpy as np


# 自分のやっている計算が合っているか確認した。結果は同じだった。
# [[0.99825818 0.00417572]
#  [0.99671015 0.00783606]
#  [0.99208838 0.01857215]
#  [0.98292668 0.03896619]
#  [0.9704207  0.06519264]
#  [0.95257517 0.09946052]
#  [0.92829285 0.14127745]
#  [0.89880287 0.18390018]
#  [0.85696693 0.23303561]
#  [0.8034797  0.27716056]
#  [0.72910984 0.31299612]
#  [0.6104713  0.32926127]
#  [0.4693372  0.30606372]]
DATA = []
for k_ in np.arange(0, 3.1, .25).round(decimals=2):
    HC = []
    for op in range(10):
        x = cn.powerlaw_psd_gaussian(exponent=k_, size=2**15)
        hc = complexity_entropy(x, dx=6)
        HC.append(hc)
    DATA.append(np.mean(HC,axis=0))
print(np.array(DATA))    

'''
.round(decimals=2)：確実に小数点以下2桁に収める。
'''

# np.save('data/fig3/hc_knoise.npy', hc_knoise)

