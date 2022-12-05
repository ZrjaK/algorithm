# 题目：2478.完美分割的方案数
# 难度：HARD
# 最后提交：2022-11-20 11:42:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        f = set(["2", "3", "5", "7"])
        if s[-1] in f:
            return 0
        dp = [[0] * n for _ in range(k+1)]
        h = [[0] * n for _ in range(k+1)]
        for j in range(n-2, -1, -1):
            if s[j] in f and s[j-1] not in f and n - j >= minLength:
                dp[1][j] = 1
            h[1][j] = h[1][j+1] + dp[1][j]
        for i in range(2, k+1):
            for j in range(n-2, -1, -1):
                if s[j] in f and s[j-1] not in f and j + minLength < n:
                    dp[i][j] = h[i-1][j+minLength]
                    dp[i][j] %= int(1e9+7)
                h[i][j] = h[i][j+1] + dp[i][j]
                h[i][j] %= int(1e9+7)
        return dp[k][0] % int(1e9+7)