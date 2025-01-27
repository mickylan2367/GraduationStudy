

from make import *
# import glob


count = 10

# ファイルへの書き出し
for cnt in range(count):
    path = f"u090/ikeda_090_{cnt}"
    x, y = ikeda_map(u=0.90, x0=np.random.uniform(), y0=np.random.uniform())
    data = np.stack([x, y], 1)
    # print(data)
    np.save(path, data)