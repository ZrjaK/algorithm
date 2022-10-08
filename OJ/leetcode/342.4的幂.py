# 题目：342.4的幂
# 难度：EASY
# 最后提交：2021-10-21 18:07:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in range(n):
            if 4 ** i == n:
                return True
            if 4 ** i >= n:
                return False