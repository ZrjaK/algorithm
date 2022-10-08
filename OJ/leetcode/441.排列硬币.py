# 题目：441.排列硬币
# 难度：EASY
# 最后提交：2021-10-22 00:01:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(1, n + 2):
            n -= i
            if n < 0:
                return i - 1