# 题目：263.丑数
# 难度：EASY
# 最后提交：2021-10-21 16:49:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        while(n % 5 == 0):
            n /= 5
        while(n % 3 == 0):
            n /= 3
        while(n % 2 == 0):
            n /= 2
        return n == 1