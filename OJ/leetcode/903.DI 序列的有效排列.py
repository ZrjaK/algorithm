# 题目：903.DI 序列的有效排列
# 难度：HARD
# 最后提交：2022-10-17 16:22:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for j in range(n+1):
            dp[0][j] = 1
        for i in range(1, n+1):
            for j in range(i+1):
                if s[i-1] == "D":
                    for k in range(j, i):
                        dp[i][j] += dp[i-1][k]
                else:
                    for k in range(j):
                        dp[i][j] += dp[i-1][k]
        return sum(dp[n]) % int(1e9+7)