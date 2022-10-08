# 题目：2245.转角路径的乘积中最多能有几个尾随零
# 难度：MEDIUM
# 最后提交：2022-04-19 14:46:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def calc(a, b):
            res = 0
            while a % b == 0:
                a //= b
                res += 1
            return res
        m, n = len(grid), len(grid[0])
        h1 = [[0] * n for _ in range(m)]
        h2 = [[0] * n for _ in range(m)]
        h3 = [[0] * n for _ in range(m)]
        h4 = [[0] * n for _ in range(m)]
        for i in range(m):
            h1[i][0] = calc(grid[i][0], 2)
            h3[i][0] = calc(grid[i][0], 5)
        for j in range(n):
            h2[0][j] = calc(grid[0][j], 2)
            h4[0][j] = calc(grid[0][j], 5)
        for i in range(m):
            for j in range(1,n):
                h1[i][j] = h1[i][j-1] + calc(grid[i][j], 2)
                h3[i][j] = h3[i][j-1] + calc(grid[i][j], 5)
        for j in range(n):
            for i in range(1,m):
                h2[i][j] = h2[i-1][j] + calc(grid[i][j], 2)
                h4[i][j] = h4[i-1][j] + calc(grid[i][j], 5)
        # print(h1,h2,h3,h4)
        ans = -1e99
        for i in range(m):
            for j in range(n):
                p1 = min(h1[i][j]+h2[i][j]-calc(grid[i][j], 2),
                        h3[i][j]+h4[i][j]-calc(grid[i][j], 5))
                p2 = min(h1[i][-1]-h1[i][j]+h2[i][j],
                        h3[i][-1]-h3[i][j]+h4[i][j])
                p3 = min(h1[i][-1]-h1[i][j]+h2[-1][j]-h2[i][j]+calc(grid[i][j], 2),
                        h3[i][-1]-h3[i][j]+h4[-1][j]-h4[i][j]+calc(grid[i][j], 5))
                p4 = min(h1[i][j]+h2[-1][j]-h2[i][j],
                        h3[i][j]+h4[-1][j]-h4[i][j])
                ans = max(ans,p1,p2,p3,p4)
        return ans