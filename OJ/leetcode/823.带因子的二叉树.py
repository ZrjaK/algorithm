# 题目：823.带因子的二叉树
# 难度：MEDIUM
# 最后提交：2022-07-08 01:28:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        s = set(arr)
        @cache
        def p(x):
            res = 1
            for i in s:
                t = x / i
                if t in s:
                    res += p(t) * p(i)
            return res
        return sum(p(i) for i in s) % int(1e9+7)