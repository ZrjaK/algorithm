# 题目：1227.飞机座位分配概率
# 难度：MEDIUM
# 最后提交：2022-07-14 01:57:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        def p(i):
            if i == 1:
                return 1
            return 1/i + p(i-1) * (i-2) / i
        return p(n)