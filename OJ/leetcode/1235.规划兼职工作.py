# 题目：1235.规划兼职工作
# 难度：HARD
# 最后提交：2022-10-22 00:08:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        h = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(h)
        endTime.sort()
        dp = [0] * n
        for i in range(n):
            t = bisect_right(endTime, h[i][0])
            dp[i] = max(dp[i-1], dp[t-1]+h[i][2])
        return dp[-1]