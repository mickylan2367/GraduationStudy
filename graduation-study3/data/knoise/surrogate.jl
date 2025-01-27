

using Plots
using Printf
using TimeseriesSurrogates, CairoMakie
using PyCall

np = pyimport("numpy")
glob = pyimport("glob")
paths = glob.glob("original/**.npy")
N = 100


paths = glob.glob("")
data = np.load(paths[1])
x = data[:, 1]
y = data[:, 2]

for i in 1:N
    sx = surrogate(x, AAFT())
    sy = surrogate(y, AAFT())

    ss = np.stack([sx, sy], axis=1)
    np.save("aaft/knoise_$i.npy", ss)
end