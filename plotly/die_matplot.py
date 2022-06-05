import matplotlib.pyplot as plt

from die import Die


# D6を作成する
die_1 = Die()
die_2 = Die()

# サイコロを転がし結果をリストに格納する
results = []
[results.append(die_1.roll() + die_2.roll()) for roll_num in range(50_000)]

# 結果を分析する
max_results = die_1.num_sides + die_2.num_sides

# X軸のデータ
input_value = list(range(2, max_results + 1))
# Y軸のデータ
frequencies = []
[frequencies.append(results.count(value)) for value in range(2, max_results + 1)]

# グラフのスタイルを設定
plt.style.use('seaborn')

# グラフ領域の生成
fig, ax = plt.subplots()
ax.scatter(input_value, frequencies, c=frequencies, cmap=plt.cm.Blues ,s=10)
# データを描画
ax.plot(input_value, frequencies, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("Die Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Die of Value", fontsize=14)

# 各軸の範囲を設定する
# axis([x軸の最小値, x軸の最大値, y軸の最小値, y軸の最大値])
ax.axis([2, 12, 0, 10_000])

# メモリのラベルのサイズを設定する
ax.tick_params(axis='both', labelsize=14)

# グラフを保存する
plt.show()