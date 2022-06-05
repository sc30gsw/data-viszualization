import plotly.graph_objects as go
import numpy as np

from random_walk import RandomWalk

while True:
  # ランダムウォークを生成
  rw: RandomWalk = RandomWalk(10_000)
  rw.fill_walk()

  # スケールの大きさ
  l = rw.num_points

  fig = go.Figure(data=go.Scatter(
    # x座標
    x=rw.x_values,
    # y座標
    y=rw.y_values,
    mode='markers',
    name='Random Walk',
    marker=dict(
        color=np.arange(l),
        # 点のサイズ
        size=3,
        colorscale='Greens',
        # スケールの表示
        showscale=True
    )
  ))

  fig.show()

  keep_runnning: str = input("別のランダムウォークを生成する?(y/n)")
  if keep_runnning == 'n':
    break