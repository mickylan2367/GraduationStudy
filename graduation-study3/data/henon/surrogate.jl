

using Plots
using Printf
using TimeseriesSurrogates, CairoMakie
using PyCall

np = pyimport("numpy")
glob = pyimport("glob")
paths = glob.glob("original/**.npy")
N = 100
file_number = 1

data = np.load(paths[file_number])
x = data[:, 1]
y = data[:, 2]

for i in 1:N
    sx = surrogate(x, AAFT())
    sy = surrogate(y, AAFT())

    ss = np.stack([sx, sy], axis=1)
    np.save("aaft/try0$file_number/henon_$i.npy", ss)
end