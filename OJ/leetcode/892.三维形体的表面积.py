# 题目：892.三维形体的表面积
# 难度：EASY
# 最后提交：2021-11-01 22:31:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    res += 4*grid[i][j] + 2
                if i :
                    res -= min(grid[i][j],grid[i-1][j]) * 2
                if j :
                    res -= min(grid[i][j],grid[i][j-1]) * 2
        return res