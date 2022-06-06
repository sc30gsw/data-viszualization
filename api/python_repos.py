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
print(f"ステータスコード: {r.status_code}")

# APIレスポンスを変数に格納する
response_dict = r.json()

# リポジトリに関する情報を調べる
repo_dicts = response_dict['items']

# リポジトリ名とスター数をリストに格納する
repo_names: List[str] = []
stars: List[int] = []

[
  (
    repo_names.append(repo_dict['name']),
    stars.append(repo_dict['stargazers_count'])
  )
  for repo_dict in repo_dicts
]

# データの可視化を行う
data = [{
  'type': 'bar',
  'x': repo_names,
  'y': stars,
}]

my_layout = {
  'title': 'GitHubで最も多くのスターがついているPythonプロジェクト',
  'xaxis': {'title': 'リポジトリ'},
  'yaxis': {'title': 'スターの数'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
