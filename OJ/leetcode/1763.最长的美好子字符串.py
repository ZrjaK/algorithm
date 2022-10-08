# 题目：1763.最长的美好子字符串
# 难度：EASY
# 最后提交：2022-08-26 21:25:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
            for j in range(i, n):
                t = s[i:j+1]
                if len(set(list(t))) == len(set(list(t.lower()))) * 2 and len(t) > len(ans):
                    ans = t
        return ans