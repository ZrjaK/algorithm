# 题目：1208.尽可能使字符串相等
# 难度：MEDIUM
# 最后提交：2022-05-04 14:35:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = r = c = 0
        while r < len(s):
            c += abs(ord(s[r]) - ord(t[r]))
            r += 1
            if c > maxCost:
                c -= abs(ord(s[l]) - ord(t[l]))
                l += 1
        return len(s) - l