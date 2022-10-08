# 题目：1318.或运算的最小翻转次数
# 难度：MEDIUM
# 最后提交：2022-08-26 03:45:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            if c>>i & 1:
                if not a>>i & 1 | b>>i & 1:
                    ans += 1
            else:
                ans += a>>i & 1
                ans += b>>i & 1
        return ans