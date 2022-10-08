# 题目：剑指 Offer 62.圆圈中最后剩下的数字
# 难度：EASY
# 最后提交：2022-10-03 21:02:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ans = 0
        for i in range(2, n+1):
            ans = (ans + m) % i
        return ans