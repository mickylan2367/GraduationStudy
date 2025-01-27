

using Plots
using Printf
using TimeseriesSurrogates, CairoMakie
using PyCall

np = pyimport("numpy")
data = np.load("C:\\Users\\Owner\\study\\graduation-study2\\python_data\\data\\standard.npy")
x = data[:, 1]
y = data[:, 2]


sx = surrogate(x, AAFT())
sy = surrogate(y, AAFT())


np.save("standard_AAFT_x.npy")
np.save("standard_AAFT_y.npy")
