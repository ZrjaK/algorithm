# 题目：172.阶乘后的零
# 难度：MEDIUM
# 最后提交：2022-03-25 00:09:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def trailingZeroes(self, n: int) -> int:
        r = int(n / 5)
        if n >= 25:
            r += self.trailingZeroes(r)
        return r