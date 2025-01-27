


import numpy as np

#if you have not installed the package, you can run the line below instead of importing ordpy.
from ordpy import *

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import string
import glob
import warnings


def stdfigsize(scale=1, nrows=1, ncols=1, ratio=1.3):
    """
    Returns a tuple to be used as figure size.

    Parameters
    ----------
    returns (7*ratio*scale*nrows, 7.*scale*ncols)
    By default: ratio=1.3
    ----------
    Returns (7*ratio*scale*nrows, 7.*scale*ncols).
    """

    return((7*ratio*scale*ncols, 7.*scale*nrows))



#Logistic map
def logistic_map(n=2**15, r=4, x0=0.4):
    """
    Iterates the logistic map.
    
    Parameters
    ----------
    n  : number of map iterations (length of the series).
    x0 : initial population ([0,1] interval)
    r  : intrinsic growth rate (r >= 0; interesting in [0,4] because then, it 
         maps the orbit to the [0,1] interval to itself.)
    ----------
    Returns a logistic map orbit.
    """
    x    = np.zeros(n)
    x[0] = x0
    
    for i in range(n-1):
        x[i+1] = r*x[i]*(1-x[i])
        
    return x


#Henon's map
def henon_map(n=2**15, a=1.4, b=0.3, x0=.5, y0=.5):
    """
    Paramenters
    -----------
    n  : time series length.
    a  : map parameter.
    b  : map parameter.
    x0 : initial condition.
    y0 : initial condition.
    -----------
    
    Returns the x and y variables of Henón's map.
    """
    with warnings.catch_warnings():
        warnings.simplefilter("error")
            
        bool_ = False
        while bool_==False:        
            try:
                x    = np.zeros(n)
                y    = np.zeros(n)

                x[0] = x0
                y[0] = y0

                for i in range(1, n):
                    x[i] = 1 - a*x[i-1]**2 + y[i-1]
                    y[i] = b*x[i-1]

                bool_ = True

            except RuntimeWarning: #changes the random inital condition
                x0 = np.random.uniform()
                y0 = np.random.uniform()

    return x, y


hc_henon_x, hc_henon_y = np.mean(
    [[complexity_entropy(x_, dx=6),
      complexity_entropy(y_, dx=6)]
     for x_, y_ in [(henon_map(x0=np.random.uniform(), y0=np.random.uniform()))
                    for _ in range(10)]],
    axis=0)

hc_logistic = np.mean([
    complexity_entropy(logistic_map(x0=np.random.uniform()), dx=6)
    for _ in range(10)
],
                      axis=0)

#theoretical curves
hc_max_curve = maximum_complexity_entropy(dx=6).T
hc_min_curve = minimum_complexity_entropy(dx=6, size=719).T



plt.figure(figsize=stdfigsize(nrows=1,ncols=1))

hc_data = [
    hc_henon_x, hc_logistic
]
labels = [
    'Henon Map', 'Logistic Map'
]
markers = ['o', 's']

#palettable.cmocean.diverging.Balance_7_r.hex_colors
colors = ['#3C0912', '#A72424'] 


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

plt.legend(frameon=False, loc=(0, 1),ncol=2, fontsize=15)
plt.ylim(bottom=0, top=.51)
plt.xlim(left=0, right=1.06)
plt.xticks([0, 1.0], fontsize=20)
plt.yticks([0, 0.5], fontsize=20)
plt.xlabel("Shanon Entropy")
plt.ylabel("Statistical Complexity")


#theoretical curves
hmin, cmin = hc_min_curve  #(this variable is defined in the cell above)
hmax, cmax = hc_max_curve  #(this variable is defined in the cell above)
plt.plot(hmin, cmin, linewidth=1.5, color='#202020', zorder=0)
plt.plot(hmax, cmax, linewidth=1.5, color='#202020', zorder=0)

plt.ylabel('Statistical complexity, $C$', fontsize=20)
plt.xlabel('Permutation entropy, $H$', fontsize=20)
plt.annotate('$d_x = 6$', (.5, .2),
               va='center',
               ha='center',
               xycoords='axes fraction',
               fontsize=20,
               bbox={
                   'boxstyle': 'round',
                   'fc': 'white',
                   'alpha': 1,
                   'ec': '#d9d9d9'
               })

plt.tight_layout()
plt.show();



