import json
import requests

# API予呼び出しを作成してそのレスポンスを格納する
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
# APIにリクエストを送信
r = requests.get(url)
print(f"ステータスコード: {r.status_code}")

# データ構造を調べる
response_dict = r.json()
readable_file = './data/readable_hn_data.json'

with open(readable_file, 'w') as f:
  json.dump(response_dict, f, indent=4)
