# 题目：395.至少有 K 个重复字符的最长子串
# 难度：MEDIUM
# 最后提交：2022-05-20 11:54:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)