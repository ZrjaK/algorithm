# 题目：821.字符的最短距离
# 难度：EASY
# 最后提交：2021-10-24 14:09:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        s = list(s)
        for i in range(len(s)):
            if s[i] == c:
                s[i] = 0
            else:
                s[i] = 1000
        for i in range(1, len(s)-1):
            if s[i] != 0:
                s[i] = min(s[i-1], s[i+1]) + 1
        for i in range(len(s)-2, 0, -1):
            if s[i] != 0:
                s[i] = min(s[i-1], s[i+1]) + 1
        if s[0] != 0:
            s[0] = s[1] + 1
        if s[-1] != 0:
            s[-1] = s[-2] + 1
        return s