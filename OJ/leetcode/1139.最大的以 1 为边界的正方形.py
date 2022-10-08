# 题目：1139.最大的以 1 为边界的正方形
# 难度：MEDIUM
# 最后提交：2022-07-13 13:44:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0] * 2 for _ in range(n)] for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                dp[i][j][0] = dp[i-1][j][0] + 1
                dp[i][j][1] = dp[i][j-1][1] + 1
                mi = min(dp[i][j])
                for k in range(mi):
                    if dp[i-k][j][1] >= k+1 and dp[i][j-k][0] >= k+1:
                        ans = max(ans, k+1)
        return ans ** 2