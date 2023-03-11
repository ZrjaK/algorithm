# 题目：2373.矩阵中的局部最大值
# 难度：EASY
# 最后提交：2023-03-01 07:37:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = []
        for i in range(1, m-1):
            t = []
            for j in range(1, n-1):
                a = grid[i][j]
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        a = max(a, grid[i-x][j-y])
                t.append(a)
            res.append(t)
        return res