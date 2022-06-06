from typing import Dict
import unittest
import requests
from python_repos import get_status_code

class StatusCodeTestCase(unittest.TestCase):
  """python_repos.pyをテストする"""

  def setUp(self):
    """テストデータのセットアップ"""
    # API予呼び出しを作成してそのレスポンスを格納する
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    # GitHubAPIのバージョンを指定
    headers: Dict[str, str] = {'Accept': 'application/vnd.github.v3+json'}
    # APIにリクエストを送信
    self.r = requests.get(url, headers=headers)

  def test_get_status_code(self):
    """ステータスコード200が返却されるか?"""
    self.assertEqual(get_status_code(self.r), 200)

if __name__ == '__main__':
  unittest.main()