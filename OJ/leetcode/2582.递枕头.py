# 题目：2582.递枕头
# 难度：EASY
# 最后提交：2023-03-05 10:31:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t = 1
        f = -1
        for _ in range(time):
            if t == n or t == 1:
                f *= -1
            if f:
                t += f
        return t