# 题目：剑指 Offer II 092.翻转字符
# 难度：MEDIUM
# 最后提交：2022-10-09 18:45:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        h = [int(i) for i in s]
        n = len(s)
        @cache
        def p(i, pre):
            if i == n:
                return 0
            if pre == 1:
                return p(i+1, 1) + (1-h[i])
            return min(p(i+1, h[i]), 1 + p(i+1, 1-h[i]))
        return p(0, 0)