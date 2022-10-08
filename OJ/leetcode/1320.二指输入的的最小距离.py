# 题目：1320.二指输入的的最小距离
# 难度：HARD
# 最后提交：2022-09-15 21:27:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumDistance(self, word: str) -> int:
        h = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(26):
                h[i][j] = abs(i//6-j//6) + abs(i%6-j%6)
        n = len(word)
        @cache
        def p(i, a, b):
            if i == n:
                return 0
            return min(h[a][ord(word[i])-65] + p(i+1, ord(word[i])-65, b), 
                        h[b][ord(word[i])-65] + p(i+1, a, ord(word[i])-65))
        res = 1e99
        for i in range(26):
            for j in range(26):
                res = min(res, p(0, i, j))
        return res