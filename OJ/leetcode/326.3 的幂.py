# 题目：326.3 的幂
# 难度：EASY
# 最后提交：2021-10-21 17:52:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in range(n):
            if 3 ** i == n:
                return True
            if 3 ** i >= n:
                return False