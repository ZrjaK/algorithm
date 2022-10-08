# 题目：1663.具有给定数值的最小字符串
# 难度：MEDIUM
# 最后提交：2022-09-07 11:38:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        while n:
            t = max(1, k-26*(n-1))
            ans.append(t)
            k -= t
            n -= 1
        return "".join([chr(i+96) for i in ans])