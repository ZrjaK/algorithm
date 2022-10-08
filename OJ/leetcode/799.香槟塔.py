# 题目：799.香槟塔
# 难度：MEDIUM
# 最后提交：2022-07-07 18:51:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (query_row+1) for _ in range(query_row+1)]
        dp[0][0] = poured
        for i in range(query_row):
            for j in range(i+1):
                if dp[i][j] > 1:
                    dp[i+1][j] += (dp[i][j] - 1) / 2
                    dp[i+1][j+1] += (dp[i][j] - 1) / 2
                    dp[i][j] = 1
        return min(1, dp[query_row][query_glass])
