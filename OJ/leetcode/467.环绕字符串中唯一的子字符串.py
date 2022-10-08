# 题目：467.环绕字符串中唯一的子字符串
# 难度：MEDIUM
# 最后提交：2022-07-22 19:47:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        n = len(p)
        dp = [1] * n
        v = [0] * 26
        for i in p:
            v[ord(i)-97] = 1
        for i in range(1, n):
            if (ord(p[i-1])-97+1) % 26 == ord(p[i])-97:
                dp[i] = dp[i-1] + 1
            v[ord(p[i])-97] = max(v[ord(p[i])-97], dp[i])
        return sum(v)