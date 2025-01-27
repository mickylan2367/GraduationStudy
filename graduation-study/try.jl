# script.jl

# 実行回数を保存するファイル名
counter_file = "counter.txt"

# ファイルが存在するかどうかをチェック
if isfile(counter_file)
    # ファイルが存在する場合、カウンターを読み込む
    open(counter_file, "r") do file
        counter = parse(Int, readline(file))
    end
else
    # ファイルが存在しない場合、カウンターを0に初期化
    counter = 0
end

# 実行回数をインクリメント
counter += 1

# 新しいカウンター値をファイルに保存
open(counter_file, "w") do file
    write(file, string(counter))
end

# 実行回数を表示
println("このスクリプトは $counter 回実行されました。")
