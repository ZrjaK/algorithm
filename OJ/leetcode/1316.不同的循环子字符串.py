# 题目：1316.不同的循环子字符串
# 难度：HARD
# 最后提交：2022-12-11 20:07:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

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

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        ans = {}
        for i in range(len(text)):
            z = z_function(text[i:])
            for j in range(len(z)):
                if j and z[j] >= j:
                    ans[text[i:i+j]] = 1
        return sum(ans.values())
