import matplotlib.pyplot as plt

# X軸のデータ
input_value = [1, 2, 3, 4, 5]
# Y軸のデータ
squares = [1, 4, 9, 16, 25]

# 点を描画する場所を格納したリスト
x_values = range(0, 1001)
y_values = [x ** 2 for x in x_values]

# グラフのスタイルを設定
plt.style.use('seaborn')

# グラフ領域の生成
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues ,s=10)
# データを描画
ax.plot(input_value, squares, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 各軸の範囲を設定する
# axis([x軸の最小値, x軸の最大値, y軸の最小値, y軸の最大値])
ax.axis([0, 1100, 0, 1100000])

# メモリのラベルのサイズを設定する
ax.tick_params(axis='both', labelsize=14)

plt.show()