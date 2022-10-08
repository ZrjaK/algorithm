# 题目：2413.最小偶倍数
# 难度：EASY
# 最后提交：2022-09-18 10:30:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return lcm(2, n)