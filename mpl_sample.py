import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

# グラフ領域の生成
fig, ax = plt.subplots()
# データを描画
ax.plot(squares)

plt.show()