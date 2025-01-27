
using Printf
using Plots
using TimeseriesSurrogates, CairoMakie
using PyCall

np = pyimport("numpy")
# ordpy = pyimport("complexity_e")

# # ファイルの実行回数
cnt = 0
# counter_file = "cnt.txt"
# if isfile(counter_file)
#     open(counter_file, "r") do file
#         cnt = parse(Int, readline(file))
#     end
# else
#     cnt = 0
# end
# cnt += 1

"""
    logistic_map(n::Int=2^15, r::Float64=4.0, x0::Float64=0.4)

Iterates the logistic map.

# Parameters
- `n`  : number of map iterations (length of the series).
- `x0` : initial population ([0,1] interval)
- `r`  : intrinsic growth rate (r >= 0; interesting in [0,4] because then, it maps the orbit to the [0,1] interval to itself.)

# Returns
A tuple of the logistic map orbit and its surrogate.

"""
# 0から1の一様乱数
random_number = rand()
println(random_number)

function logistic_map(n::Int=2^15, r::Float64=3.8555, x0::Float64=random_number)
    x = zeros(Float64, n)
    x[1] = x0
    
    for i in 1:n-1
        x[i+1] = r * x[i] * (1 - x[i])
    end
    
    # サロゲートデータを生成
    # s = surrogate(x, RandomShuffle())
    
    # return (x, s)
    return x
end

# 計算を実行
# original, surrogate_data = logistic_map()
original = logistic_map()
np.save("38555_original/original_$cnt", original)

println("計算結果が original_$cnt.npyに保存されました。")




