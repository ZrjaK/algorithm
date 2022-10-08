# 题目：2110.股票平滑下跌阶段的数目
# 难度：MEDIUM
# 最后提交：2022-07-23 20:46:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            if prices[i-1] - 1 == prices[i]:
                dp[i] = dp[i-1] + 1
            ans += dp[i]
        return ans