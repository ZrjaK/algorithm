# 题目：2414.最长的字母序连续子字符串的长度
# 难度：MEDIUM
# 最后提交：2022-09-18 10:33:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        h = [ord(i)-97 for i in s]
        ans = 0
        c = 1
        for i in range(1, len(h)):
            if h[i] == h[i-1] + 1:
                c += 1
            else:
                ans = max(ans, c)
                c = 1
        ans = max(ans, c)
        return ans