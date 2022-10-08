# 题目：1866.恰有 K 根木棍可以看到的排列数目
# 难度：HARD
# 最后提交：2022-09-28 15:58:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

dp = [[0] * 1001 for _ in range(1001)]
dp[0][0] = 1
for i in range(1, 1001):
    for j in range(1, i+1):
        dp[i][j] = (dp[i-1][j-1] + (i-1) * dp[i-1][j]) % int(1e9+7)

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        return dp[n][k]