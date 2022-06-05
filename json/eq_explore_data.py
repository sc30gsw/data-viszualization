import json
from typing import List
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# データの構造を調査する
filename = './data/eq_data_1_day_m1.json'
# ファイルを読み込む
with open(filename) as f:
  # jsonを読み込む
  all_eq_data = json.load(f)

# 地震情報の特徴を取得
all_eq_dicts = all_eq_data['features']

# マグニチュード
mags: List[float] = []
# 経度
lons: List[float] = []
# 緯度
lats: List[float] = []
[
  (
    mags.append(eq_dict['properties']['mag']),
    lons.append(eq_dict['geometry']['coordinates'][0]),
    lats.append(eq_dict['geometry']['coordinates'][1])  
  ) 
  for eq_dict in all_eq_dicts
]

# 地震の地図 → Scattergeoの引数に経度・緯度を渡すことで世界地図上にデータを点として描画する
# Scattergeo自身は世界地図を作成する
# データの作成
data = [Scattergeo(lon=lons, lat=lats)]
# レイアウトの作成
my_layout = Layout(title='世界の地震')

fig = {'data': data, 'layout': my_layout}
# htmlファイルに出力する
offline.plot(fig, filename='global_earthquakes.html')

readable_file = './data/readable_eq_data.json'
# ファイルに書き込む
with open(readable_file, 'w') as f:
  # jsonを出力する
  json.dump(all_eq_data, f, indent=4)