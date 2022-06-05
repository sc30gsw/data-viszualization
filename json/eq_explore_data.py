import json
from typing import Dict, List
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# データの構造を調査する
filename = './data/eq_data_30_day_m1.json'
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
# 地震のタイトル情報
hover_texts: List[str] = []
[
  (
    mags.append(eq_dict['properties']['mag']),
    lons.append(eq_dict['geometry']['coordinates'][0]),
    lats.append(eq_dict['geometry']['coordinates'][1]),
    hover_texts.append(eq_dict['properties']['title'])
  ) 
  for eq_dict in all_eq_dicts
]

# 地震の地図 → Scattergeoの引数に経度・緯度を渡すことで世界地図上にデータを点として描画する
# Scattergeo自身は世界地図を作成する
# データの作成
# data = [Scattergeo(lon=lons, lat=lats)]
data: List[Dict[str, str | float]] = [{
  'type': 'scattergeo',
  'lon': lons,
  'lat': lats,
  'text': hover_texts,
  'marker': {
    'size': [5 * mag for mag in mags],
    'color': mags,
    'colorscale': 'Viridis',
    'reversescale': True,
    'colorbar': {'title': 'マグニチュード'}
  }
}]
# レイアウトの作成
title: str = all_eq_data['metadata']['title']
my_layout = Layout(title=title)

fig: Dict[str, Dict[str, str | float]] = {'data': data, 'layout': my_layout}
# htmlファイルに出力する
offline.plot(fig, filename='global_earthquakes.html')

readable_file = './data/readable_eq_data.json'
# ファイルに書き込む
with open(readable_file, 'w') as f:
  # jsonを出力する
  json.dump(all_eq_data, f, indent=4)