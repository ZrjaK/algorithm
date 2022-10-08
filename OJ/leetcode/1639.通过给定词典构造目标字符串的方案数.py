# 题目：1639.通过给定词典构造目标字符串的方案数
# 难度：HARD
# 最后提交：2022-09-18 15:33:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, m = len(words[0]), len(target)
        d = [[0] * 26 for _ in range(n)]
        for i in range(n):
            for s in words:
                d[i][ord(s[i])-97] += 1
        @cache
        def p(i, j):
            if j == m:
                return 1
            if i == n:
                return 0
            res = p(i+1, j) + p(i+1, j+1) * d[i][ord(target[j])-97]
            return res
        return p(0, 0) % int(1e9+7)