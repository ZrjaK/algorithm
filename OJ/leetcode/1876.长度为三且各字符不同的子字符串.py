# 题目：1876.长度为三且各字符不同的子字符串
# 难度：EASY
# 最后提交：2022-03-31 21:37:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        ans = 0
        while i < len(s) - 2:
            t = s[i:i+3]
            if len(t) == len(set(list(t))):
                ans += 1
            i += 1
        return ans