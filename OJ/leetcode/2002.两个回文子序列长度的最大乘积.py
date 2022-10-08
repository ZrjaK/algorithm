# 题目：2002.两个回文子序列长度的最大乘积
# 难度：MEDIUM
# 最后提交：2022-07-22 17:47:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        h = [0] * (1<<n)
        def check(t):
            i, j = 0, n-1
            while i < j:
                if not 1<<i & t:
                    i += 1
                    continue
                if not 1<<j & t:
                    j -= 1
                    continue
                if s[i] != s[j]:
                    return 0
                i += 1
                j -= 1
            return [bool(1<<i&t) for i in range(n)].count(True)
        for i in range(1<<n):
            h[i] = check(i)
        res = 1
        for i in range(1<<n):
            for j in range(i+1, 1<<n):
                if h[i] and h[j] and not i & j:
                    res = max(res, h[i] * h[j])
        return res