# 题目：1278.分割回文串 III
# 难度：HARD
# 最后提交：2022-04-05 22:02:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        a = [[0] * len(s) for _ in s]
        for i in range(len(a)-2, -1, -1):
            for j in range(i+1, len(a)):
                a[i][j] = a[i+1][j-1]
                a[i][j] += 1 if s[i] != s[j] else 0
        @lru_cache(None)
        def f(index, c):
            if c == 0:
                if index == len(s):
                    return 0
                else:
                    return 1e99
            res = 1e99
            for i in range(index+1, len(s)+1):
                res = min(res, a[index][i-1]+f(i, c-1))
            return res
        
        return f(0, k)