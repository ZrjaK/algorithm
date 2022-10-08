# 题目：1624.两个相同字符之间的最长子字符串
# 难度：EASY
# 最后提交：2022-09-17 10:11:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = [[] for _ in range(26)]
        for i in range(len(s)):
            d[ord(s[i])-97].append(i)
        ans = -1
        for l in d:
            if l:
                ans = max(ans, l[-1]-l[0]-1)
        return ans
