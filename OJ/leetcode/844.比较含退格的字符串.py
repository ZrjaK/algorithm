# 题目：844.比较含退格的字符串
# 难度：EASY
# 最后提交：2021-10-25 15:18:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        b = []   
        for i in range(len(s)):
            if s[i] != '#':
                a.append(s[i])
            elif s[i] == '#' and a != []:
                a.pop()
        for i in range(len(t)):
            if t[i] != '#':
                b.append(t[i])
            elif t[i] == '#' and b != []:
                b.pop()
        return a == b
