# 题目：1021.删除最外层的括号
# 难度：EASY
# 最后提交：2022-09-01 18:58:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        c = 0
        l = r = 0
        for i, v in enumerate(s):
            if v == "(":
                l += 1
            else:
                r += 1
            if l == r:
                ans += s[c+1:i]
                l = r = 0
                c = i + 1
        return ans