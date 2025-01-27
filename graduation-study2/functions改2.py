

from ordpy import ordinal_distribution
import numpy as np
import math




def PE(data, dx=3, dy=1, taux=1, tauy=1, base=2, normalized=True, probs=False, tie_precision=None):
    """
    Calculates the Shannon entropy using an ordinal distribution obtained from
    data\\ [#bandt_pompe]_\\ :sup:`,`\\ [#ribeiro_2012]_.
    
    Parameters
    ----------
    data : array
           Array object in the format :math:`[x_{1}, x_{2}, x_{3}, \\ldots ,x_{n}]`
           or  :math:`[[x_{11}, x_{12}, x_{13}, \\ldots, x_{1m}],
           \\ldots, [x_{n1}, x_{n2}, x_{n3}, \\ldots, x_{nm}]]`
           or an ordinal probability distribution (such as the ones returned by 
           :func:`ordpy.ordinal_distribution`).
    dx : int
         Embedding dimension (horizontal axis) (default: 3).
    dy : int
         Embedding dimension (vertical axis); it must be 1 for time series 
         (default: 1).
    taux : int
           Embedding delay (horizontal axis) (default: 1).
    tauy : int
           Embedding delay (vertical axis) (default: 1).
    base : str, int
           Logarithm base in Shannon's entropy. Either 'e' or 2 (default: 2).
    normalized: boolean
                If `True`, permutation entropy is normalized by its maximum value 
                (default: `True`). If `False`, it is not.
    probs : boolean
            If `True`, it assumes **data** is an ordinal probability distribution.
            If `False`, **data** is expected to be a one- or two-dimensional array
            (default: `False`). 
    tie_precision : None, int
                    If not `None`, **data** is rounded with `tie_precision`
                    decimal numbers (default: `None`).

    Returns
    -------
     : float
       Value of permutation entropy.
    
    Examples
    --------
    >>> permutation_entropy([4,7,9,10,6,11,3], dx=2, base=2, normalized=True)
    0.9182958340544896
    >>>
    >>> permutation_entropy([.5,.5], dx=2, base=2, normalized=False, probs=True)
    1.0
    >>>
    >>> permutation_entropy([[1,2,1],[8,3,4],[6,7,5]], dx=2, dy=2, base=2, normalized=True)
    0.32715643797829735
    >>>
    >>> permutation_entropy([[1,2,1,4],[8,3,4,5],[6,7,5,6]], dx=2, dy=2, taux=2, base='e', normalized=False)
    1.0397207708399179
    """
    if not probs:
        patterns, probabilities = ordinal_distribution(data, dx, dy, taux, tauy, return_missing=False, tie_precision=tie_precision)
        dd = len(patterns)  
        print(dd)
    else:
        probabilities    = np.asarray(data)
        probabilities    = probabilities[probabilities>0]
        dd = len(probabilities)

    logfunc = np.log if base=='e' else np.log2
    s       = -np.sum(probabilities*logfunc(probabilities))

    if normalized==True:      
        smax = logfunc(float(dd))
        return s/smax
    else:
        return s 


def CE(data, dx=3, dy=1, taux=1, tauy=1, probs=False, tie_precision=None, base=2):
    """
    Calculates permutation entropy\\ [#bandt_pompe]_ and statistical
    complexity\\ [#lopezruiz]_\\ :sup:`,`\\ [#rosso]_ using an ordinal 
    distribution obtained from data.
    
    Parameters
    ----------
    data : array
           Array object in the format :math:`[x_{1}, x_{2}, x_{3}, \\ldots ,x_{n}]`
           or  :math:`[[x_{11}, x_{12}, x_{13}, \\ldots, x_{1m}],
           \\ldots, [x_{n1}, x_{n2}, x_{n3}, \\ldots, x_{nm}]]`
           or an ordinal probability distribution (such as the ones returned by 
           :func:`ordpy.ordinal_distribution`).
    dx : int
         Embedding dimension (horizontal axis) (default: 3).
    dy : int
         Embedding dimension (vertical axis); it must be 1 for time series 
         (default: 1).
    taux : int
           Embedding delay (horizontal axis) (default: 1).
    tauy : int
           Embedding delay (vertical axis) (default: 1).
    probs : boolean
            If `True`, it assumes **data** is an ordinal probability distribution.
            If `False`, **data** is expected to be a one- or two-dimensional array
            (default: `False`). 
    tie_precision : None, int
                    If not `None`, **data** is rounded with `tie_precision`
                    decimal numbers (default: `None`).

    Returns
    -------
     : tuple
       Values of normalized permutation entropy and statistical complexity.
    
    Examples
    --------
    >>> complexity_entropy([4,7,9,10,6,11,3], dx=2)
    (0.9182958340544894, 0.06112816548804511)
    >>>
    >>> p = ordinal_distribution([4,7,9,10,6,11,3], dx=2, return_missing=True)[1]
    >>> complexity_entropy(p, dx=2, probs=True)
    (0.9182958340544894, 0.06112816548804511)
    >>> 
    >>> complexity_entropy([[1,2,1],[8,3,4],[6,7,5]], dx=2, dy=2)
    (0.3271564379782973, 0.2701200547320647)
    >>>
    >>> complexity_entropy([1/3, 1/15, 4/15, 2/15, 1/5, 0], dx=3, probs=True)
    (0.8314454838586238, 0.16576716623440763)
    >>>
    >>> complexity_entropy([[1,2,1,4],[8,3,4,5],[6,7,5,6]],dx=3, dy=2)
    (0.21070701155008006, 0.20704765093242872)
    """


    logfunc = np.log if base=='e' else np.log2
    # n = float(dx*dy)
    if probs==False:
        patterns, probabilities = ordinal_distribution(data, dx, dy, taux, tauy, return_missing=False, tie_precision=tie_precision)   
        h                = PE(probabilities, dx, dy, taux, tauy, probs=True, tie_precision=tie_precision)
        dd = len(patterns)
    else:
        probabilities = np.asarray(data)
        probabilities = probabilities[probabilities>0]
        h = PE(probabilities, dx, dy, taux, tauy, probs=True, tie_precision=tie_precision)
        dd = len(probabilities)

    uniform_dist          = 1/dd
    print(dd)
    p_plus_u_over_2      = (uniform_dist + probabilities)/2  
    s_of_p_plus_u_over_2 = -np.sum(p_plus_u_over_2*logfunc(p_plus_u_over_2)) 

    s_of_p_over_2 = -np.sum(probabilities*logfunc(probabilities))/2
    s_of_u_over_2 = logfunc(dd)/2.

    js_div_max_new = -0.5*(((dd+1)/dd)*logfunc(dd+1) + logfunc(dd) - 2*logfunc(2*dd))
    js_div     = s_of_p_plus_u_over_2 - s_of_p_over_2 - s_of_u_over_2

    return h, h*js_div/js_div_max_new