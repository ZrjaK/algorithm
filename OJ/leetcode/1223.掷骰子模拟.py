# 题目：1223.掷骰子模拟
# 难度：HARD
# 最后提交：2022-09-14 20:31:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0] * max(rollMax) for _ in range(6)] for _ in range(n)]
        for i in range(6):
            dp[0][i][0] = 1
        for i in range(1, n):
            for j in range(6):
                for f in range(6):
                    for k in range(rollMax[f]):
                        if f != j:
                            dp[i][j][0] += dp[i-1][f][k]
                for k in range(1, rollMax[j]):
                    dp[i][j][k] = dp[i-1][j][k-1]
        return sum(sum(i) for i in dp[-1]) % int(1e9+7)
