import matplotlib.pyplot as plt

from random_walk import RandomWalk

# プログラムが動作している間、新しいランダムウォークを作成し続ける
while True:
# ランダムウォークを生成
  rw = RandomWalk(50_000)
  rw.fill_walk()

  # ランダムウォークの点を描画する
  plt.style.use('classic')
  # 描画する図のサイズを画面に合わせる(figsize=(縦, 横))
  fig, ax = plt.subplots(figsize=(15, 9))

  # ランダムウォークの点にカラーマップを適用
  point_numbers = range(rw.num_points)
  ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
  edgecolors='none', s=1)

  # 開始点と終了点を強調する
  ax.scatter(0, 0, c='green', edgecolors='none', s=100)
  ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)

  # 軸を削除する
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  
  plt.show()

  keep_runnning = input("別のランダムウォークを生成する?(y/n)")
  if keep_runnning == 'n':
    break