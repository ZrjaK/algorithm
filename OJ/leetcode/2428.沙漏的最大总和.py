# 题目：2428.沙漏的最大总和
# 难度：MEDIUM
# 最后提交：2022-10-02 10:32:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                f = grid[i-1][j-1] +grid[i-1][j] + grid[i-1][j+1] + grid[i+1][j-1] + grid[i+1][j] +grid[i+1][j+1] + grid[i][j]
                ans = max(ans, f)
        return ans