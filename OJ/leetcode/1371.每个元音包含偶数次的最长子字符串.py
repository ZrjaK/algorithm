# 题目：1371.每个元音包含偶数次的最长子字符串
# 难度：MEDIUM
# 最后提交：2022-08-26 04:25:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d = {"a": 0,"e": 1, "i": 2, "o": 3, "u": 4}
        h = {0:-1}
        t = ans = 0
        for i in range(len(s)):
            if s[i] in d:
                t ^= 1<<d[s[i]]
            if t in h:
                ans = max(ans, i-h[t])
            else:
                h[t] = i
        return ans