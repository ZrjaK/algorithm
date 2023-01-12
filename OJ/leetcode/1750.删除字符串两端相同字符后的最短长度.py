# 题目：1750.删除字符串两端相同字符后的最短长度
# 难度：MEDIUM
# 最后提交：2022-12-28 00:20:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l, r = 0, n-1
        while l < r and s[l] == s[r]:
            while l < r and s[l] == s[l+1]:
                l += 1
            while l < r and s[r] == s[r-1]:
                r -= 1
            l += 1
            r -= 1
        return max(0, r-l+1)