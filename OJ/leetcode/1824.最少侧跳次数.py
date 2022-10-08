# 题目：1824.最少侧跳次数
# 难度：MEDIUM
# 最后提交：2022-07-21 01:27:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[0] * 4 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(1, 4):
                dp[i][j] = 1e99
                if j == obstacles[i]:
                    continue
                dp[i][j] = dp[i+1][j]
                for k in range(1, 4):
                    if k != j and k != obstacles[i]:
                        dp[i][j] = min(dp[i][j], dp[i+1][k] + 1)
        return dp[0][2]