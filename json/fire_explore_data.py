import csv
from datetime import datetime
from typing import List
from plotly.graph_objs import Layout
from plotly import offline

filename = './data/world_fires_1_day.csv'
with open(filename) as f:
  # 読み込みオブジェクトに指定したファイルオブジェクトを渡す
  reader = csv.reader(f)
  # ファイルの最初の行を読み込む
  header_row: List[str] = next(reader)

  # 火事の明るさ
  brights: List[float] = []
  # 経度
  lons: List[float] = []
  # 緯度
  lats: List[float] = []
  # ホバーテキストに設定する日付
  dates: List[datetime] = []

  [
    (
      brights.append(float(row[2])),
      lons.append(float(row[1])),
      lats.append(float(row[0])),
      dates.append(datetime.strptime(row[5], '%Y-%m-%d'))
    ) for row in reader
  ]

  # 地震の地図 → Scattergeoの引数に経度・緯度を渡すことで世界地図上にデータを点として描画する
  # Scattergeo自身は世界地図を作成する
  # データの作成
  data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': dates,
    'marker': {
      'size': [bright / 100 * 3 for bright in brights],
      'color': brights,
      'colorscale': 'Inferno',
      'reversescale': True,
      'colorbar': {'title': '火災の輝度'}
    }
  }]
  # レイアウトの作成
  my_layout = Layout(title='世界の火災')

  fig = {'data': data, 'layout': my_layout}
  # htmlファイルに出力する
  offline.plot(fig, filename='global_fire.html')