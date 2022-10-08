# 题目：2319.判断矩阵是否是一个 X 矩阵
# 难度：EASY
# 最后提交：2022-06-26 10:35:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        l = []
        for i in range(n):
            for j in range(n):
                if j == i or j == n-1-i:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True