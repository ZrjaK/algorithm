# 题目：2008.出租车的最大盈利
# 难度：MEDIUM
# 最后提交：2022-05-17 18:03:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        back = defaultdict(list)
        for start, end, tip in rides:
            back[end].append((start, tip))
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i - 1]
            for start, tip in back[i]:
                dp[i] = max(dp[i], dp[start] + tip + i - start)
        return dp[n]