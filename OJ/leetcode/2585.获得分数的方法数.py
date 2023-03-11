# 题目：2585.获得分数的方法数
# 难度：HARD
# 最后提交：2023-03-05 14:44:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        n = len(types)
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            count, mark = types[i-1]
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if j - mark >= 0:
                    dp[i][j] += dp[i][j - mark]
                if j - (count + 1) * mark >= 0:
                    dp[i][j] -= dp[i-1][j - (count + 1) * mark]
                dp[i][j] %= int(1e9+7)
        return dp[n][target]