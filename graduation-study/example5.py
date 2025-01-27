import numpy as np
# import matplotlib.pyplot as plt
from ordpy import complexity_entropy
# import warnings
# import matplotlib as mpl
# import matplotlib.image as mpimg

import string
import glob
import warnings
import os

# 特定のディレクトリのパス
directory_path = 'julia/data'

# すべてのファイル名を検出
file_names = glob.glob(os.path.join(directory_path, 'surrogate_*.txt'))
hc_surrogate = []
# ファイル名を表示
for file_name in file_names:
    print(file_name)
    surrogate_data = np.loadtxt(file_name)
    hc = complexity_entropy(surrogate_data, dx=6)
    hc_surrogate.append(hc)
    # print(hc_surrogate)

hc_surrogate= np.array(hc_surrogate)
print(np.mean(hc_surrogate, axis=0))
print(type(hc_surrogate))
