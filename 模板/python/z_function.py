class Solution:
    def sumScores(self, s: str) -> int:
        return sum(z_function(s)) + len(s)
        
def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

# https://oi-wiki.org/string/z-func/

# https://leetcode.cn/problems/sum-of-scores-of-built-strings/

# 2223. 构造字符串的总得分和