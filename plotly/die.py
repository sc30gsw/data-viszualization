from random import randint


class Die:
  """1個のサイコロを表すクラス"""

  def __init__(self, num_sides=6) -> None:
    """6面のサイコロをデフォルトとする"""
    self.num_sides = num_sides

  def roll(self):
    """1から面の数の間のランダムな数値を返す"""
    return randint(1, self.num_sides)
