import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# グラフのスタイルを設定
plt.style.use('seaborn')

# グラフ領域の生成
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)
# データを描画
ax.plot(input_value, squares, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# メモリのラベルのサイズを設定する
ax.tick_params(axis='both', labelsize=14)

plt.show()