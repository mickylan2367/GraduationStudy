

from make import *
# import glob


count = 10

# ファイルへの書き出し
for cnt in range(count):
    path = f"original2/u008/ikeda_008_{cnt}"
    x, y = ikeda_map2(u=0.80, x0=np.random.uniform(), y0=np.random.uniform())
    data = np.stack([x, y], 1)
    # print(data)
    np.save(path, data)