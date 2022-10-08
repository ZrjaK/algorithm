# 题目：1690.石子游戏 VII
# 难度：MEDIUM
# 最后提交：2022-07-20 00:44:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        h = list(accumulate(stones)) + [0]
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(h[j]-h[i]-dp[i+1][j], h[j-1]-h[i-1]-dp[i][j-1])
        return dp[0][n-1]