# 题目：70.爬楼梯
# 难度：EASY
# 最后提交：2021-10-20 20:02:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(3, n+1):
            temp = a
            a = b
            b = temp + b
        return b