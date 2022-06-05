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
  point_numbers = range(rw.num_points)
  ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
  edgecolors='none', s=15)
  plt.show()

  keep_runnning = input("別のランダムウォークを生成する?(y/n)")
  if keep_runnning == 'n':
    break