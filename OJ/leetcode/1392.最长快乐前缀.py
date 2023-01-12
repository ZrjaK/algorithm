# 题目：1392.最长快乐前缀
# 难度：HARD
# 最后提交：2023-01-06 09:43:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestPrefix(self, s: str) -> str:
        nxt = prefix_function(s)
        return s[:nxt[-1]]

def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi