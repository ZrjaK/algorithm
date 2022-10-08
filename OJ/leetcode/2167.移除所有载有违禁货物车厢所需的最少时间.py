# 题目：2167.移除所有载有违禁货物车厢所需的最少时间
# 难度：HARD
# 最后提交：2022-09-26 08:52:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        h1 = [0] * n
        h2 = [0] * (n+1)
        for i in range(n):
            if s[i] == "1":
                h1[i] = min(h1[i-1]+2, i+1)
            else:
                h1[i] = h1[i-1]
        for i in range(n-1, -1, -1):
            if s[i] == "1":
                h2[i] = min(h2[i+1]+2, n-i)
            else:
                h2[i] = h2[i+1]
        ans = 1e99
        for i in range(n):
            ans = min(ans, h1[i]+h2[i+1])
        return ans