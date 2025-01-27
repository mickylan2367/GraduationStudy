
using Printf
using Plots
using TimeseriesSurrogates, CairoMakie


# # ファイルの実行回数
cnt = 4
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

function logistic_map(n::Int=2^15, r::Float64=4.0, x0::Float64=random_number)
    x = zeros(Float64, n)
    x[1] = x0
    
    for i in 1:n-1
        x[i+1] = r * x[i] * (1 - x[i])
    end
    
    # サロゲートデータを生成
    s = surrogate(x, RandomShuffle())
    
    return (x, s)
end

# 計算を実行
original, surrogate_data = logistic_map()

# 結果をファイルに保存
open("data/original_$cnt.txt", "w") do file
    for value in original
        @printf(file, "%.5f\n", value)
    end
end

open("data/surrogate_$cnt.txt", "w") do file
    for value in surrogate_data
        @printf(file, "%.5f\n", value)
    end
end

println("計算結果が original_$cnt.txt と surrogate_$cnt.txt に保存されました。")

# surroplot(original, surrogate_data)
# savefig("pics_$cnt.png")


# # store counter
# open(counter_file, "w") do file
#     write(file, string(cnt))
# end
# println("このスクリプトは $cnt 回実行されました。")



