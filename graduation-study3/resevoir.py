

import numpy as np
import matplotlib.pyplot as plt

# カオス信号の生成 (例: ロジスティック写像)
def generate_chaotic_data(length, r=3.9, x0=0.5):
    data = np.zeros(length)
    data[0] = x0
    for i in range(1, length):
        data[i] = r * data[i - 1] * (1 - data[i - 1])
    return data

# エコーステートネットワーク (ESN) の実装
class EchoStateNetwork:
    def __init__(self, input_size, reservoir_size, output_size, spectral_radius=0.95, sparsity=0.1, seed=None):
        np.random.seed(seed)
        self.input_size = input_size
        self.reservoir_size = reservoir_size
        self.output_size = output_size

        # 入力重み行列
        self.W_in = np.random.uniform(-1, 1, (reservoir_size, input_size))
        
        # リザバー重み行列
        W = np.random.uniform(-0.5, 0.5, (reservoir_size, reservoir_size))
        W[np.random.rand(*W.shape) > sparsity] = 0  # スパース性を適用
        spectral_radius_current = max(abs(np.linalg.eigvals(W)))
        self.W = W * (spectral_radius / spectral_radius_current)  # スペクトル半径のスケーリング

        # 出力重み行列（学習によって決定）
        self.W_out = None

        # リザバー状態
        self.state = np.zeros(reservoir_size)

    def update(self, u):
        # 状態の更新
        self.state = np.tanh(np.dot(self.W_in, u) + np.dot(self.W, self.state))

    def train(self, inputs, outputs, ridge_lambda=1e-6):
        # リザバー状態を収集
        states = []
        for u in inputs:
            self.update(u)
            states.append(self.state.copy())
        states = np.array(states)

        # リッジ回帰で出力重みを学習
        self.W_out = np.dot(
            np.linalg.inv(np.dot(states.T, states) + ridge_lambda * np.eye(self.reservoir_size)),
            np.dot(states.T, outputs)
        )

    def predict(self, inputs):
        # 学習済みモデルで予測
        predictions = []
        for u in inputs:
            self.update(u)
            y = np.dot(self.W_out, self.state)
            predictions.append(y)
        return np.array(predictions)

# メイン処理
if __name__ == "__main__":
    # カオス信号を生成
    # data_length = 1000
    # chaotic_data = generate_chaotic_data(data_length)
    chaotic_data = np.load("data/henon/ikeda/original/u090/ikeda_090_0.npy")
    chaotic_data = chaotic_data[:, 0]

    # 学習データとテストデータに分割
    train_length = 800
    train_data = chaotic_data[:train_length]
    test_data = chaotic_data[train_length:]

    # 入力と出力を準備（1ステップ予測）
    input_data = train_data[:-1].reshape(-1, 1)
    output_data = train_data[1:]

    # ESNの構築と学習
    esn = EchoStateNetwork(input_size=1, reservoir_size=200, output_size=1, seed=42)
    esn.train(input_data, output_data)

    # テストデータで予測
    test_input = test_data[:-1].reshape(-1, 1)
    predictions = esn.predict(test_input)
    # np.save("out_weight", esn.W_out)

    # 結果をプロット
    plt.figure(figsize=(12, 6))
    plt.plot(test_data[1:], label="True Signal", alpha=0.7)
    plt.plot(predictions, label="ESN Prediction", linestyle="--")
    plt.xlim(9000, len(predictions))
    plt.legend()
    plt.title("ESN Predicting Chaotic Signal")
    plt.xlabel("Time Step")
    plt.ylabel("Value")
    plt.show()
