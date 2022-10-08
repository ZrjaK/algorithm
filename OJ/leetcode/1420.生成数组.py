# 题目：1420.生成数组
# 难度：HARD
# 最后提交：2022-09-22 11:17:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @cache
        def p(i, j, f):
            if i == 1:
                if f == 1:
                    return 1
                return 0
            res = p(i-1, j, f) * j
            for x in range(1, j):
                res += p(i-1, x, f-1)
            return res
        return sum(p(n, j, k) for j in range(1, m+1)) % int(1e9+7)