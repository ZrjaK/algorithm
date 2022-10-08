# 题目：剑指 Offer 48.最长不含重复字符的子字符串
# 难度：MEDIUM
# 最后提交：2022-10-03 18:45:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        l = 0
        d = defaultdict(int)
        for r in range(n):
            d[s[r]] += 1
            if any(i > 1 for i in d.values()):
                d[s[l]] -= 1
                l += 1
        return r - l + 1
