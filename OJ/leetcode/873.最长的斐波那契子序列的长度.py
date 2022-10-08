# 题目：873.最长的斐波那契子序列的长度
# 难度：MEDIUM
# 最后提交：2022-07-20 04:05:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        d = {x:i for i, x in enumerate(arr)}
        @cache
        def p(i, j):
            t = arr[j]-arr[i] 
            if t in d and d[t] < i:
                return 1 + p(d[t], i)
            return 0
        res = 2 + max(p(i, j) for i in range(n) for j in range(i+1, n))
        p.cache_clear()
        if res < 3:
            return 0
        return res