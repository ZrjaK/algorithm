# 题目：剑指 Offer II 085.生成匹配的括号
# 难度：MEDIUM
# 最后提交：2022-10-08 15:03:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def p(s, l, r):
            if not l and not r:
                res.append(s)
                return
            if l == r:
                p(s+"(", l-1, r)
            elif l < r:
                if l:
                    p(s+"(", l-1, r)
                p(s+")", l, r-1)
        p("", n, n)
        return res