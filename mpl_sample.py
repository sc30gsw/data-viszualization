import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

# グラフ領域の生成
fig, ax = plt.subplots()
# データを描画
ax.plot(squares, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# メモリのラベルのサイズを設定する
ax.tick_params(axis='both', labelsize=14)

plt.show()