# 题目：463.岛屿的周长
# 难度：EASY
# 最后提交：2021-10-22 12:41:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

from scipy.signal import convolve2d
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return int(abs(convolve2d(grid,[[-2,1],[1,0]])).sum())