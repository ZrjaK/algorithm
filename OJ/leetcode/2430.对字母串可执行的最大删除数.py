# 题目：2430.对字母串可执行的最大删除数
# 难度：HARD
# 最后提交：2022-10-02 10:58:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return len(s)
        @cache
        def check(f, t):
            return f == t
        h = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(1, (n-i)//2+1):
                if s[i:i+j] == s[i+j:i+j+j]:
                    h[i][j] = 1
        @cache
        def p(i):
            res = 1
            for j in range(1, (n-i)//2+1):
                if h[i][j]:
                    res = max(res, 1 + p(i+j))
            return res
        return p(0)