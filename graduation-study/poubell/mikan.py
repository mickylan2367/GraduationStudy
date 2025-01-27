import numpy as np
from pyunicorn.timeseries import Surrogates

# ロジスティック写像のデータを生成
def logistic_map(n=2**15, r=4, x0=0.4):
    x = np.zeros(n)
    x[0] = x0
    for i in range(n - 1):
        x[i + 1] = r * x[i] * (1 - x[i])
    return x

# ロジスティック写像の時系列データを生成
n = 2**15
r = 4
x0 = 0.4
time_series = logistic_map(n=n, r=r, x0=x0)

# Surrogates クラスのインスタンスを作成
surrogate = Surrogates(original_data=time_series)

# サロゲートデータを生成 (例: AAFT サロゲート)
surrogate_data = surrogate.construct_surrogates(original_data=time_series, method='AAFT')

# 結果をファイルに保存
np.savetxt('surrogate_data.txt', surrogate_data)

print("サロゲートデータが surrogate_data.txt に保存されました。")
