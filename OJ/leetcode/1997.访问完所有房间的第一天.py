# 题目：1997.访问完所有房间的第一天
# 难度：MEDIUM
# 最后提交：2022-07-22 16:44:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = dp[i-1] + 2 + dp[i-1] - dp[nextVisit[i-1]]
        return dp[-1] % int(1e9+7)