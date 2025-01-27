

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


def stdfigsize(scale=1, nrows=1, ncols=1, ratio=1.2):
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



#theoretical curves
hc_max_curve = maximum_complexity_entropy(dx=6).T
hc_min_curve = minimum_complexity_entropy(dx=6, size=719).T

hc_standard_aaft = np.load("hc/all_data/all_hc_standard_aaft.npy")
hc_standard_OX = np.load("hc/all_data/all_hc_standard.npy")

# Draw
plt.rcParams['xtick.labelsize'] = 20 
plt.rcParams['ytick.labelsize'] = 20
# plt.rcParams["axes."]




hc_data = [
    hc_standard_OX,
    hc_standard_aaft
]

labels = [
    'Standard Map',
    'Surrogate Standard Map'
]

markers = [
    '*', 'p'
]

#palettable.cmocean.diverging.Balance_7_r.hex_colors
colors = [
    '#75AABE', '#0C5EBE'
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
        
                

plt.legend(frameon=False, loc=(0, .99), ncol=2, fontsize=15)
plt.ylim(bottom=0, top=0.021)
plt.xlim(left=0.994, right=1.0)
plt.xticks([0.995, 1.0])
plt.yticks([0.0, 0.02])


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
