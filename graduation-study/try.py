import subprocess

def run_julia_script(script_path):
    result = subprocess.run(["julia", script_path], capture_output=True, text=True, encoding='utf-8')
    return result.stdout

julia_script_path = "script.jl"

for i in range(5):  # 5回実行
    output = run_julia_script(julia_script_path)
    print(f"Execution {i + 1}:\n{output}")

