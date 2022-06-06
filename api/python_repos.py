from urllib import response
import requests

# API予呼び出しを作成してそのレスポンスを格納する
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# GitHubAPIのバージョンを指定
headers = {'Accept': 'application/vnd.github.v3+json'}
# APIにリクエストを送信
r = requests.get(url, headers=headers)
print(f"ステータスコード: {r.status_code}")

# APIレスポンスを変数に格納する
response_dict = r.json()

# 結果を処理する
print(response_dict.keys())
