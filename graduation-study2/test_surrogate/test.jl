

using TimeseriesSurrogates # for surrogate tests
using DynamicalSystemsBase # to simulate logistic map
using ComplexityMeasures   # to compute permutation entropy
using Random: Xoshiro      # for reproducibility
using CairoMakie           # for plotting
using PyCall


# cd("C:/Users/Owner/study/graduation-study2/data/ikeda/original")
np = pyimport("numpy")
rng = Xoshiro(1234567)
# x = TimeseriesSurrogates.AR1(; n_steps = 400, k = 0.25, rng)
x = np.load(``)
y = np.load("standard.npy")
y = y[:, 1]

perment(x) = entropy_normalized(SymbolicPermutation(; m = 6), x)
method = RandomFourier()

test = SurrogateTest(perment, y, method; n = 1000, rng)
p = pvalue(test)
println(p < 0.001)  # 99.9-th quantile confidence