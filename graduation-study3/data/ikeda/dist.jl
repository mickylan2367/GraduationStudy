
# 制作途中
using Plots
using Printf
using TimeseriesSurrogates, CairoMakie
using PyCall

np = pyimport("numpy")
glob = pyimport("glob")
ordpy = pyimport("ordpy")
stats = pyimport("stats_func.py")
paths = glob.glob("original/u001/**.npy")
N = 100


for i in 1:N
    data = np.load(paths[1])
    x = data[:, 1]
    pats, probs = ordpy.ordinal_distribution(x, dx=6, return_missing=True)
    probs = sort_probs(pats, probs)
    np.save(f"dist/original/dist_{i}", probs)
end