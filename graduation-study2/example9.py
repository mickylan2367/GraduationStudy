

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
# from functions改 import *
# import seaborn as sns


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



#theoretical curves
hc_max_curve = maximum_complexity_entropy(dx=2, dy=3).T
hc_min_curve = minimum_complexity_entropy(dx=2,dy=3, size=719).T


# BASE_PATH = "data/paper/fig3"
hc_knoise = np.load('data/paper/fig3/hc_knoise.npy')
hc_fbm = np.load('data/paper/fig3/hc_fbm.npy')
hc_fgn = np.load('data/paper/fig3/hc_fgn.npy')

# 2D
hc_henon = np.load("hc/2D_hc_henon.npy")
# hc_ikeda = np.load("hc/2D_hc_ikeda.npy")
hc_ikeda = np.load("hc/2d_hc_ikeda_dx2dy3.npy")
hc_standard = np.load("hc/2D_hc_standard.npy")
hc_aaft_standard = np.load("hc/each_data/each_hc_standard_dx6.npy")


# Draw
# plt.rcParams['xtick.labelsize'] = 30 # 軸だけ変更されます。
# plt.rcParams['ytick.labelsize'] = 30 # 軸だけ変更されます


hc_data = [
    hc_henon[1], hc_ikeda, hc_standard[1], hc_aaft_standard,
    hc_knoise, hc_fbm, hc_fgn
]

# hc_data = np.array(hc_data)

labels = [
    'Henon Map', 'Ikeda Map','Standard Map', 'AAFT fot Standard Map',
    "knoise", "fbm", "fgn"
]

markers = [
    'o', '8', '^', '.', 
    'v', '*', 'p'
]

#palettable.cmocean.diverging.Balance_7_r.hex_colors
colors = [
    '#3C0912', '#ad39c9', '#10e1ab', 
    '#F1ECEB', '#75AABE', '#0C5EBE', '#181C43'
] 


plt.figure(figsize=stdfigsize(nrows=1,ncols=1))
for data_, marker_, color_, label_, cnt in zip(hc_data, markers, colors,
                                               labels, range(len(hc_data))):
    #point plotting
    h_, c_ = data_.T
    plt.plot(h_,
               c_,
               marker_,
               markersize=13,
               markeredgecolor='#202020',
               color=color_,
               label=label_)
    
    if cnt == 1:  #ikeda
        labels = [0.1, 0.3, 0.6, 0.8, 0.85, 0.9, 0.92]
        labels = [str(label) for label in labels]
        indices = [0,1,2,3, 4, 5, 6]
        toriaezu = [0]*len(indices) #とりあえずの位置

        for tx_, x_, y_, adjx_, adjy_ in zip(
            [labels[i] for i in indices],
                h_[indices], 
                    c_[indices],
                        toriaezu,
                        toriaezu):
            
            plt.annotate(r'$u = {}$'.format(tx_),
                         xy=(x_ + adjx_, y_ + adjy_),
                         fontsize=10,color='#202020')
    
    #dotted #202020 line connecting dots
    if cnt in [4, 5]:
        plt.plot(h_, c_, '--', linewidth=1, color='#202020', zorder=0)
        
        if cnt == 4:  #colored noise
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
        if cnt == 5:  #fBm
            for tx_, x_, y_, adjx_, adjy_ in zip(['0.1', '0.5', '0.9'],
                                                 h_[[0, 4, 8]], c_[[0, 4, 8]],
                                                 [-.14, -.13, -.04],
                                                 [-0.008, -0.010, -0.03]):
                plt.annotate(r'$h = {}$'.format(tx_),
                               xy=(x_ + adjx_, y_ + adjy_),
                               fontsize=15,
                               color='#202020')
        
                


plt.legend(frameon=False, loc=(0, .85), ncol=2, fontsize=15)
plt.ylim(bottom=0, top=.51)
plt.xlim(left=0, right=1.06)
plt.xticks([0, 1.0])
plt.yticks([0, 0.5])


#theoretical curves
hmin, cmin = hc_min_curve  #(this variable is defined in the cell above)
hmax, cmax = hc_max_curve  #(this variable is defined in the cell above)
plt.plot(hmin, cmin, linewidth=1.5, color='#202020', zorder=0)
plt.plot(hmax, cmax, linewidth=1.5, color='#202020', zorder=0)

plt.ylabel('Statistical complexity, $C$')
plt.xlabel('Permutation entropy, $H$')
plt.annotate('$d_x = 2, d_y=3$', (.5, .2),
               va='center',
               ha='center',
               xycoords='axes fraction',
               fontsize=30,
               bbox={
                   'boxstyle': 'round',
                   'fc': 'white',
                   'alpha': 1,
                   'ec': '#d9d9d9'
               })

plt.tight_layout()
# plt.savefig('fig5.', dpi=300, bbox_inches='tight')

