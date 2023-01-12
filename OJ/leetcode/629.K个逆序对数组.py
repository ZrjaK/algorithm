# 题目：629.K个逆序对数组
# 难度：HARD
# 最后提交：2023-01-05 11:28:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def p(i, j):
            if j == 0:
                return 1
            if i <= 0 or j < 0:
                return 0
            return (p(i-1, j) + p(i, j-1) - p(i-1, j-i)) % int(1e9+7)
        return p(n, k)

