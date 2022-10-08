# 题目：3.无重复字符的最长子串
# 难度：MEDIUM
# 最后提交：2022-01-06 02:42:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = {}
        i, ans = -1, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i)
            st[s[j]] = j
        return ans;

            