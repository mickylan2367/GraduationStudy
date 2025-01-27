

# AAFT
# the explanation about AAFT SURROGATE is here:
# https://juliadynamics.github.io/TimeseriesSurrogates.jl/stable/methods/fourier_surrogates/#Amplitude-adjusted-Fourier-transform-(AAFT)

using Printf
using Plots
using TimeseriesSurrogates, CairoMakie

crd = pwd()*"\\original"
files = readdir(crd)

n = 2^15


for (cnt, file) in enumerate(files)
    filepath = crd*"\\"*file
    println("processing "*filepath*" NOW!")
    lines = readlines(filepath)
    data = zeros(Float64, n)
    for (index, line) in enumerate(lines)
        data[index] = parse.(Float64, line)
    end

    # ファイルへの書き込み
    surrogate_data = surrogate(data, AAFT())
    open("fft/aaft_$cnt.txt", "w") do file
        for value in surrogate_data
            @printf(file, "%.5f\n", value)
        end
    end
end
