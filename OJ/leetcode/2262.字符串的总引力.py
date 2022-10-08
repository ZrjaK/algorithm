# 题目：2262.字符串的总引力
# 难度：HARD
# 最后提交：2022-05-01 12:13:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        d = [-1] * 26
        for i, n in enumerate(s):
            t = ord(n)-ord('a')
            dp[i+1] = dp[i] + i - d[t]
            d[t] = i
        return sum(dp)