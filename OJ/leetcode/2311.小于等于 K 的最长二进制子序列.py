# 题目：2311.小于等于 K 的最长二进制子序列
# 难度：MEDIUM
# 最后提交：2022-06-19 10:57:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        while s:
            if int(s, 2) <= k:
                return len(s)
            t = s.index("1")
            s = s[:t] + s[t+1:]
        return 0
            