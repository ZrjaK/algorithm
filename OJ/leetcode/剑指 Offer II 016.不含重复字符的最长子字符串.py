# 题目：剑指 Offer II 016.不含重复字符的最长子字符串
# 难度：MEDIUM
# 最后提交：2022-10-05 00:32:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        d = defaultdict(int)
        l = 0
        for r in range(len(s)):
            d[s[r]] += 1
            if any(i > 1 for i in d.values()):
                d[s[l]] -= 1
                l += 1
        return r-l+1