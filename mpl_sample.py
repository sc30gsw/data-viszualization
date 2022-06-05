import matplotlib.pyplot as plt

# X軸のデータ
input_value = [1, 2, 3, 4, 5]
# Y軸のデータ
squares = [1, 4, 9, 16, 25]

# 点を描画する場所を格納したリスト
x_values = input_value[:]
y_values = squares[:]

# グラフのスタイルを設定
plt.style.use('seaborn')

# グラフ領域の生成
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=200)
# データを描画
ax.plot(input_value, squares, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# メモリのラベルのサイズを設定する
ax.tick_params(axis='both', labelsize=14)

plt.show()