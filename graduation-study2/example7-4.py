

##########################################
## Calculate Shanon and Complexity Measur
##########################################

import numpy as np
import matplotlib.pyplot as plt
from ordpy import complexity_entropy, maximum_complexity_entropy, minimum_complexity_entropy, ordinal_distribution
import glob


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

    return((9*ratio*scale*ncols, 8.5*ratio*scale*nrows))

#theoretical curves
hc_max_curve = maximum_complexity_entropy(dx=6).T
hc_min_curve = minimum_complexity_entropy(dx=6, size=719).T

hc_ikeda = np.load("hc/all_data/all_hc_ikeda.npy")
hc_ikeda_aaft = np.load("hc/all_data/all_hc_ikeda_aaft.npy")
hc_ikeda_short = np.load("hc/hc_ikeda_short_dx6.npy")

hc_standard_aaft = np.load("hc/all_data/all_hc_standard_aaft.npy")
hc_standard_OX = np.load("hc/all_data/all_hc_standard.npy")





# Draw
plt.rcParams['xtick.labelsize'] = 20 # 軸だけ変更されます。
plt.rcParams['ytick.labelsize'] = 20 # 軸だけ変更されます


hc_data = [
    hc_ikeda, hc_standard_OX,
    hc_ikeda_aaft, 
    hc_standard_aaft,
    hc_ikeda_short
]

labels = [
    'Ikeda Map','Standard Map',
    'Surrogate of Ikeda Map',
    'Surrogate of Standard Map',
    'Ikeda map for a shorter-length of data'
]

markers = [
    'P', '*', 
    'P',
    'o',
    'P'
]

#palettable.cmocean.diverging.Balance_7_r.hex_colors
colors = [
    '#ad39c9', '#10e1ab',
    '#c71585', 
    '#02fb6f', 
    '#ffb6c1'
] 



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
                


plt.legend(frameon=False, loc=(0, 1.), ncol=2, fontsize=15)
plt.ylim(bottom=0, top=0.51)
plt.xlim(left=0.8, right=1.06)
plt.xticks([0.7, 0.8, 0.9, 1.0, 1.05])
plt.yticks([0.0, 0.5])


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
