# 题目：1190.反转每对括号间的子串
# 难度：MEDIUM
# 最后提交：2022-04-20 13:16:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reverseParentheses(self, s: str) -> str:
        def p(i):
            res = ""
            while i < len(s):
                if s[i] == "(":
                    t = p(i+1)
                    res += t[0]
                    i = t[1] + 1
                elif s[i] == ")":
                    break
                else:
                    res += s[i]
                    i += 1
            return [res[::-1], i]
        return p(0)[0][::-1]