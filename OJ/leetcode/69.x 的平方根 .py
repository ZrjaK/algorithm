# 题目：69.x 的平方根 
# 难度：EASY
# 最后提交：2021-10-20 19:57:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for i in range(x+2):
            if i * i > x:
                return i-1