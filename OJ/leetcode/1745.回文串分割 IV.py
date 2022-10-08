# 题目：1745.回文串分割 IV
# 难度：HARD
# 最后提交：2022-04-05 21:42:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        a = [[True] * len(s) for _ in s]
        for i in range(len(a)-1, -1, -1):
            for j in range(i+1, len(a)):
                if s[i] == s[j]:
                    a[i][j] = a[i+1][j-1]
                else:
                    a[i][j] = False
        @lru_cache(None)
        def f(index, c):
            k = s[index:]
            if c == 0:
                if k == k[::-1]:
                    return True
                else:
                    return False
            res = False
            for i in range(index+1, len(s)):
                k = s[index:i]
                if a[index][i-1]:
                    res = res or f(i, c-1)
            return res
        
        return f(0, 2)
