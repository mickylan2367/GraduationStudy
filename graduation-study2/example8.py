

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

    return((7*scale*ncols, 7.*ratio*scale*nrows))


# 2D
hc_henon = np.load("hc/2D_hc_henon.npy")
hc_ikeda = np.load("hc/2D_hc_ikeda.npy")
hc_standard = np.load("hc/2D_hc_standard.npy")


hc_data = [
    hc_henon, hc_ikeda, hc_standard
]

hc_data = np.array(hc_data)

labels = [
    'Henon Map', 'Ikeda Map','Standard Map'
]

markers = [
    'o', '8', '^'
]

#palettable.cmocean.diverging.Balance_7_r.hex_colors
colors = [
    '#3C0912', '#ad39c9', '#10e1ab',
] 

# Draw
plt.rcParams['xtick.labelsize'] = 20 
plt.rcParams['ytick.labelsize'] = 20 
plt.rcParams['figure.labelsize'] = "x-large"

fig, axes = plt.subplots(1, 3, figsize=stdfigsize(nrows=1,ncols=3))
for i in range(3):
    for data_, marker_, color_, label_, cnt in zip(hc_data[:, i], markers, colors,
                                                labels, range(len(hc_data))):
        # print(data_.shape)
        #point plotting
        h_, c_ = data_.T
        axes[i].plot(h_,
                c_,
                marker_,
                markersize=13,
                markeredgecolor='#202020',
                color=color_,
                label=label_)
                
    axes[i].legend(frameon=False, loc=(0, .85), ncol=2, fontsize=15)
    axes[i].set_ylim(bottom=0, top=.51)
    axes[i].set_xlim(left=0, right=1.06)


    ddy = [2, 3, 4]
    #theoretical curves
    hc_max_curve = maximum_complexity_entropy(dx=2, dy=ddy[i]).T
    hc_min_curve = minimum_complexity_entropy(dx=2, dy=ddy[i], size=719).T
    #theoretical curves
    hmin, cmin = hc_min_curve  #(this variable is defined in the cell above)
    hmax, cmax = hc_max_curve  #(this variable is defined in the cell above)
    axes[i].plot(hmin, cmin, linewidth=1.5, color='#202020', zorder=0)
    axes[i].plot(hmax, cmax, linewidth=1.5, color='#202020', zorder=0)
    axes[i].annotate(f'$d_x = 2, d_y={i+2}$', (.5, .2),
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
# plt.tight_layout()

axes[2].set_xticks([0, 1.0])
axes[2].set_yticks([0, 0.6])
fig.supylabel('Statistical complexity, $C$')
fig.supxlabel('Entropy, $H$')
plt.tight_layout()
plt.show();
