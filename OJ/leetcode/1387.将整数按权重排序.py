# 题目：1387.将整数按权重排序
# 难度：MEDIUM
# 最后提交：2022-07-15 15:42:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def p(i):
            if i == 1:
                return 0
            if i % 2 == 0:
                return p(i//2) + 1
            else:
                return p(3*i+1) + 1
        return sorted([i for i in range(lo, hi+1)], key=p)[k-1]