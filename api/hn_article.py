import json
from operator import itemgetter
import requests

# API予呼び出しを作成してそのレスポンスを格納する
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
# APIにリクエストを送信
r = requests.get(url)
print(f"ステータスコード: {r.status_code}")

# 各投稿についての情報を処理する
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
  # 投稿ごとに別々のAPI呼び出しを作成する
  url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
  r = requests.get(url)
  print(f"id: {submission_id}\tstatus: {r.status_code}")
  response_dict = r.json()

  # 各記事の辞書を作成する
  try: 
    submission_dict = {
      'title': response_dict['title'],
      'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
      'comments': response_dict['descendants'],
    }
  except KeyError:
    print("コメントが見つかりませんでした")
  else:
    submission_dicts.append(submission_dict)

# コメント数の順にソート
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

readable_file = './data/readable_hn_data.json'

with open(readable_file, 'w') as f:
  json.dump(submission_dicts, f, indent=4)
