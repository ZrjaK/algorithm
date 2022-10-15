# 题目：2312.卖木头块
# 难度：HARD
# 最后提交：2022-10-11 11:21:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        d = {(i, j): c for i, j, c in prices}
        @cache
        def p(x, y):
            res = d.get((x, y), 0)
            for i in range(1, x):
                res = max(res, p(i, y) + p(x-i, y))
            for j in range(1, y):
                res = max(res, p(x, j) + p(x, y-j))
            return res
        return p(m, n)