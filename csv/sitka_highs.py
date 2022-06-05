import csv

filename = './data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
  # 読み込みオブジェクトに指定したファイルオブジェクトを渡す
  reader = csv.reader(f)
  # ファイルの最初の行を読み込む
  header_row = next(reader)
  print(header_row)