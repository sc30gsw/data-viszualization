import json

# データの構造を調査する
filename = './data/eq_data_1_day_m1.json'
# ファイルを読み込む
with open(filename) as f:
  # jsonを読み込む
  all_eq_data = json.load(f)

readable_file = './data/readable_eq_data.json'
# ファイルに書き込む
with open(readable_file, 'w') as f:
  # jsonを出力する
  json.dump(all_eq_data, f, indent=4)