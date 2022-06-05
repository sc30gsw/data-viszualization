import csv
from typing import Any, List

filename = './data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
  # 読み込みオブジェクトに指定したファイルオブジェクトを渡す
  reader: Any = csv.reader(f)
  # ファイルの最初の行を読み込む
  header_row: List[str] = next(reader)
  
  for index, column_header in enumerate(header_row):
    print(index, column_header)