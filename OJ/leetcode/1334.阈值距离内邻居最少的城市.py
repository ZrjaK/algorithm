# 题目：1334.阈值距离内邻居最少的城市
# 难度：MEDIUM
# 最后提交：2022-07-14 19:17:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[1e99] * n for _ in range(n)]
        for i, j, w in edges:
            dp[i][j] = dp[j][i] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        res = 0
        mi = 1e99
        for i in range(n):
            c = 0
            for j in range(n):
                if i != j and dp[i][j] <= distanceThreshold:
                    c += 1
            if c <= mi:
                mi = c
                res = i
        return res
        