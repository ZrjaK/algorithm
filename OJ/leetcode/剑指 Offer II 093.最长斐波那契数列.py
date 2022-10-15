# 题目：剑指 Offer II 093.最长斐波那契数列
# 难度：MEDIUM
# 最后提交：2022-10-09 19:04:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        import gc;gc.disable()
        n = len(arr)
        d = {v: i for i, v in enumerate(arr)}
        @cache
        def p(i, j):
            if arr[i] + arr[j] in d:
                return 1 + p(j, d[arr[i] + arr[j]])
            return 0
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, p(i, j))
        p.cache_clear()
        return ans + 2 if ans else 0