from typing import Dict, List
import requests

from plotly.graph_objs import Bar
from plotly import offline

# API予呼び出しを作成してそのレスポンスを格納する
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# GitHubAPIのバージョンを指定
headers: Dict[str, str] = {'Accept': 'application/vnd.github.v3+json'}

# APIにリクエストを送信
r = requests.get(url, headers=headers)

def get_status_code(r):
  """ステータスコードを返却する関数"""
  return r.status_code

# APIレスポンスを変数に格納する
response_dict = r.json()

# リポジトリに関する情報を調べる
repo_dicts = response_dict['items']

# リポジトリ名とスター数をリストに格納する
repo_links: List[str] = []
stars: List[int] = []
labels: List[str] = []

for repo_dict in repo_dicts:
  repo_name = repo_dict['name']
  repo_url = repo_dict['html_url']
  repo_link = f"<a href='{repo_url}'>{repo_name}</a>"

  repo_links.append(repo_link)
  stars.append(repo_dict['stargazers_count'])

  owner = repo_dict['owner']['login']
  description = repo_dict['description']
  label = f"{owner}<br />{description}"
  labels.append(label)


# データの可視化を行う
data = [{
  'type': 'bar',
  'x': repo_links,
  'y': stars,
  'hovertext': labels,
  'marker': {
    'color': 'rgb(60, 100, 150)',
    'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
  },
  'opacity': 0.6,
}]

my_layout = {
  'title': 'GitHubで最も多くのスターがついているPythonプロジェクト',
  'titlefont': {'size': 28},
  'xaxis': {
    'title': 'リポジトリ',
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
  },
  'yaxis': {
    'title': 'スターの数',
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
  },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
