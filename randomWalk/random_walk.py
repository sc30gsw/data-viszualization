from typing import List
from random import choice

class RandomWalk:
  """ランダムウォークを生成するためのクラス"""

  def __init__(self, num_points=5000):
    """ランダムウォークの属性を初期化する"""
    self.num_points: int = num_points
    
    # すべてのランダムウォークは(0, 0)から開始する
    self.x_values: List[int] = [0]
    self.y_values: List[int] = [0]

  def fill_walk(self):
    """ランダムウォークのすべての点を計算する"""

    # ステップ数が指定した数になるまでランダムウォークを続ける
    while len(self.x_values) < self.num_points:

      # 移動する方向と距離を決定する
      x_step: int = self.get_step()
      y_step: int = self.get_step()

      # どこにも移動しない場合は結果を破棄する
      if x_step == 0 and y_step == 0:
        continue

      # 新しい位置を計算する
      x: int = self.x_values[-1] + x_step
      y: int = self.y_values[-1] + y_step

      self.x_values.append(x)
      self.y_values.append(y)
    
  def get_step(self) -> int:
    """移動する方向と距離を計算する"""
    direction: int = choice([1, -1])
    distance:int  = choice([0, 1, 2, 3, 4])
    step: int = direction * distance
    return step