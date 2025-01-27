# 計算を行う関数を定義
function calculate(a, b)
    return a + b
end

# 計算結果をファイルに書き込む関数を定義
function write_to_file(filename, content)
    open(filename, "w") do file
        write(file, content)
    end
end

# 計算を実行
result = calculate(3, 5)

# 結果をファイルに保存
write_to_file("result.txt", "計算結果: $result")

println("計算結果が result.txt に保存されました。")
