import json
from operator import itemgetter
from typing import List
import requests
from plotly.graph_objs import Bar
from plotly import offline

# API予呼び出しを作成してそのレスポンスを格納する
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
# APIにリクエストを送信
r = requests.get(url)
print(f"ステータスコード: {r.status_code}")

# 各投稿についての情報を処理する
submission_ids = r.json()
submission_dicts = []
submission_comments: List[int] = []
submission_labels: List[str] = []

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
    submission_label = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    submission_labels.append(submission_label)
    submission_comments.append(submission_dict['comments'])
    submission_dicts.append(submission_dict)

# コメント数の順にソート
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
submission_comments = sorted(submission_comments, reverse=True)

# データの可視化を行う
data = [{
  'type': 'bar',
  'x': submission_labels,
  'y': submission_comments,
  'marker': {
    'color': 'rgb(60, 100, 150)',
    'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
  },
  'opacity': 0.6,
}]

my_layout = {
  'title': 'Hacker Newsでコメントが多い投稿',
  'titlefont': {'size': 28},
  'xaxis': {
    'title': '投稿名',
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
  },
  'yaxis': {
    'title': 'コメント数',
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
  },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_repos.html')
