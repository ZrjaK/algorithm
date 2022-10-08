# 题目：1706.球会落何处
# 难度：MEDIUM
# 最后提交：2022-07-20 00:53:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        @cache
        def p(i, j):
            if i == m:
                return j
            t = grid[i][j]
            if 0 <= j+t < n and t == grid[i][j+t]:
                return p(i+1, j+t)
            else:
                return -1
        res = []
        for i in range(n):
            res.append(p(0, i))
        return res