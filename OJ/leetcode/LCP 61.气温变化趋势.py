# 题目：LCP 61.气温变化趋势
# 难度：EASY
# 最后提交：2022-09-24 15:10:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        n = len(temperatureA)
        dp = [0] * n
        for i in range(1, n):
            p1 = temperatureA[i] - temperatureA[i-1]
            p2 = temperatureB[i] - temperatureB[i-1]
            if p1 * p2 > 0 or p1 == p2 == 0:
                dp[i] = dp[i-1] + 1
        return max(dp)