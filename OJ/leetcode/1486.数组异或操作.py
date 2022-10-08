# 题目：1486.数组异或操作
# 难度：EASY
# 最后提交：2022-08-26 21:14:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= (start + (i<<1))
        return ans