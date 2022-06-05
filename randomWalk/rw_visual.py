import matplotlib.pyplot as plt

from random_walk import RandomWalk

# プログラムが動作している間、新しいランダムウォークを作成し続ける
while True:
# ランダムウォークを生成
  rw = RandomWalk()
  rw.fill_walk()

  # ランダムウォークの点を描画する
  plt.style.use('classic')
  fig, ax = plt.subplots()

  # ランダムウォークの点にカラーマップを適用
  point_numbers = range(rw.num_points)
  ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
  edgecolors='none', s=15)

  # 開始点と終了点を強調する
  ax.scatter(0, 0, c='green', edgecolors='none', s=100)
  ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)
  plt.show()

  keep_runnning = input("別のランダムウォークを生成する?(y/n)")
  if keep_runnning == 'n':
    break