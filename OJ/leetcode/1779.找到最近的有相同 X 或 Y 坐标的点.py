# 题目：1779.找到最近的有相同 X 或 Y 坐标的点
# 难度：EASY
# 最后提交：2022-12-01 15:12:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        n = len(points)
        best, bestid = float("inf"), -1
        for i, (px, py) in enumerate(points):
            if x == px:
                if (dist := abs(y - py)) < best:
                    best = dist
                    bestid = i
            elif y == py:
                if (dist := abs(x - px)) < best:
                    best = dist
                    bestid = i
        
        return bestid
