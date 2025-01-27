

##########################################
## Calculate Shanon and Complexity Measur
##########################################

import numpy as np
import matplotlib.pyplot as plt
from ordpy import complexity_entropy, maximum_complexity_entropy, minimum_complexity_entropy, ordinal_distribution
import warnings
import matplotlib as mpl
import matplotlib.image as mpimg

import string
import glob
import warnings
from functions改 import *
# import seaborn as sns


hc_stentmap = np.mean([
    complexity_entropy(skew_tent_map(x0=np.random.uniform()), dx=6)
    for _ in range(10)
],axis=0)

hc_schuster = np.mean([[
    complexity_entropy(schuster_map(z=z_, x0=np.random.uniform()), dx=6)
    for _ in range(10)
] for z_ in [3 / 2, 2, 5 / 2]],axis=1)

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




# BASE_PATH = "data/paper/fig3"
hc_knoise = np.load('data/paper/fig3/hc_knoise.npy')
hc_fbm = np.load('data/paper/fig3/hc_fbm.npy')
hc_fgn = np.load('data/paper/fig3/hc_fgn.npy')

#theoretical curves
hc_max_curve = maximum_complexity_entropy(dx=6).T
hc_min_curve = minimum_complexity_entropy(dx=6, size=719).T


# henon map
# hc_henonX, hc_henonY = hc_henon()
# Julia Surrogate Data of Logistic Map

# hc_originalLM = np.load("hc/hc_logistic.npy")
# hc_originalLM = hc_originalLM[len(hc_originalLM)-1] # only hc
hc_logistic_aaft = np.load("hc/hc_logistic_aaft.npy")

# Julia Surrogate for Ikeda Map
# hc_ikeda_OX, hc_ikeda_OY = hc_ikeda_original()
# hc_ikeda_AX, hc_ikeda_AY = hc_ikeda_aaft()
hc_ikedaOX = np.load("hc/hc_ikeda.npy")
# hc_ikedaOX = hc_ikedaOX[len(hc_ikedaOX)-1]

# Julia Surrogate for Standard Map
hc_standard_OX, hc_standard_OY = hc_standard_original()

# # Monet
# hc_monetR, hc_monetG, hc_monetB = hc_monet()



# Draw
plt.rcParams['xtick.labelsize'] = 20 # 軸だけ変更されます。
plt.rcParams['ytick.labelsize'] = 20 # 軸だけ変更されます




hc_data = [
    hc_knoise, hc_fbm, hc_fgn, 
    hc_ikedaOX[::-1][1], hc_standard_OX,
    hc_logistic_aaft
]

labels = [
    'K-Noise', 'fBm', 'fGn', 
    'Ikeda Map','Standard Map',
    'AAFT Surrogate Logistic Map'
]

markers = [
    '*', 'p', '8',
    'P', 'o', 
    '^'
]

#palettable.cmocean.diverging.Balance_7_r.hex_colors
colors = [
    '#75AABE', '#0C5EBE', '#181C43', 
    '#ad39c9', '#10e1ab',
    '#02fb6f', 
] 

# marker_size = [13]*len(colors)
# marker_size[3] = 15;marker_size[4] = 15 #ikeda map and standard map


plt.figure(figsize=stdfigsize(nrows=1,ncols=1))
for data_, marker_, color_, label_, cnt in zip(hc_data, markers, colors,
                                               labels, range(len(hc_data))):
    
    #point plotting
    h_, c_ = data_.T
    plt.plot(h_,
               c_,
               marker_,
               markersize=18,
               markeredgecolor='#202020',
               color=color_,
               label=label_)
    
    #dotted #202020 line connecting dots
    if cnt in [0, 1, 2]:
        plt.plot(h_, c_, '--', linewidth=1, color='#202020', zorder=0)
        
        if cnt == 0:  #colored noise
            adjx_ = [0.015, 0.025, -.005, 0.0]
            adjy_ = [-0.00, -0.005, 0.015, .015]
            ncnt = 0
            for n_, x_, y_ in zip(
                    np.arange(0, 3.1, .25).round(decimals=2), h_, c_):
                if n_ in [0, 1, 2, 3]:
                    plt.annotate('$k = {}$'.format(int(n_)),
                                   xy=(x_ + adjx_[ncnt], y_ + adjy_[ncnt]),
                                   fontsize=15,
                                   color='#202020')
                    ncnt += 1
        if cnt == 1:  #fBm
            for tx_, x_, y_, adjx_, adjy_ in zip(['0.1', '0.5', '0.9'],
                                                 h_[[0, 4, 8]], c_[[0, 4, 8]],
                                                 [-.038, -.13, -.04],
                                                 [-0.005, -0.010, -0.03]):
                plt.annotate(r'$h = {}$'.format(tx_),
                               xy=(x_ + adjx_, y_ + adjy_),
                               fontsize=15,
                               color='#202020')
        
                


plt.legend(frameon=False, loc=(0, .99), ncol=2, fontsize=15)
plt.ylim(bottom=0, top=0.125)
plt.xlim(left=0.8, right=1.06)
plt.xticks([0.8, 0.9, 1.0, 1.05])
plt.yticks([0.0, 0.12])


#theoretical curves
hmin, cmin = hc_min_curve  #(this variable is defined in the cell above)
hmax, cmax = hc_max_curve  #(this variable is defined in the cell above)
plt.plot(hmin, cmin, linewidth=1.5, color='#202020', zorder=0)
plt.plot(hmax, cmax, linewidth=1.5, color='#202020', zorder=0)

plt.ylabel('Statistical complexity, $C$', fontsize=30)
plt.xlabel('Permutation entropy, $H$', fontsize=30)
plt.annotate('$d_x = 6$', (.3, .2),
               va='top',
               ha='right',
               xycoords='axes fraction',
               fontsize=30,
               bbox={
                   'boxstyle': 'round',
                   'fc': 'white',
                   'alpha': 1,
                   'ec': '#d9d9d9'
               })

plt.tight_layout(w_pad=1.2)
plt.savefig('fig5.pdf', dpi=300, bbox_inches='tight')
