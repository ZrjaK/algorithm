# 题目：883.三维形体投影面积
# 难度：EASY
# 最后提交：2021-10-25 16:49:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum([sum(map(max, grid)), sum(map(max, zip(*grid))), sum(v > 0 for row in grid for v in row)])