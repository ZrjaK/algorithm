# 题目：807.保持城市天际线
# 难度：MEDIUM
# 最后提交：2022-09-06 21:53:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                rmax = max(grid[i])
                cmax = max([grid[k][j] for k in range(m)])
                ans += min(rmax, cmax) - grid[i][j]
        return ans
                
