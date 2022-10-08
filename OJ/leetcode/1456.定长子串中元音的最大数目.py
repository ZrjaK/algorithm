# 题目：1456.定长子串中元音的最大数目
# 难度：MEDIUM
# 最后提交：2022-05-24 12:52:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d = {"a", "e", "i", "o", "u"}
        l = r = 0
        c = 0
        while r < k:
            if s[r] in d:
                c += 1
            r += 1
        ans = c
        while r < len(s):
            if s[r] in d:
                c += 1
            if s[l] in d:
                c -= 1
            r += 1
            l += 1
            ans = max(ans, c)
        return ans