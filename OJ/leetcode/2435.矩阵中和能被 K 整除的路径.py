# 题目：2435.矩阵中和能被 K 整除的路径
# 难度：HARD
# 最后提交：2022-10-09 12:15:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

import gc;gc.disable()
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def p(i, j, c):
            if i == m-1 and j == n-1:
                return int((c + grid[m-1][n-1]) % k == 0)
            res = 0
            for nx, ny in [[i+1, j], [i, j+1]]:
                if nx<m and ny<n:
                    res += p(nx, ny, (c+grid[i][j]) % k)
            return res % int(1e9+7)
        res = p(0, 0, 0)
        p.cache_clear()
        return res % int(1e9+7)