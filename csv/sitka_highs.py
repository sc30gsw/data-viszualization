import csv
from typing import Any, List
import matplotlib.pyplot as plt
from datetime import datetime

filename = './data/sitka_weather_2018_simple.csv'
with open(filename) as f:
  # 読み込みオブジェクトに指定したファイルオブジェクトを渡す
  reader: Any = csv.reader(f)
  # ファイルの最初の行を読み込む
  header_row: List[str] = next(reader)
  
  for index, column_header in enumerate(header_row):
    print(index, column_header)
  
  # ファイルから最高気温と日付を取得する
  hights: List[int] = []
  dates: List[datetime] = []
  # リスト内包表記の複数処理はタプルにする
  [
    (hights.append(int(row[5])), dates.append(datetime.strptime(row[2], '%Y-%m-%d')))
    for row in reader
  ]

  # 最高気温のグラフを描画する
  plt.style.use('seaborn')
  flg, ax = plt.subplots()
  ax.plot(dates, hights, c='red')

  # グラフにフォーマットを指定する
  plt.title("Daily high temperatures, - 2018", fontsize=24)
  plt.xlabel('', fontsize=16)
  flg.autofmt_xdate()
  plt.ylabel("Temperature (F)", fontsize=16)
  plt.tick_params(axis='both', which='major', labelsize=16)

  plt.show()