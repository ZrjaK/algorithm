# 题目：面试题 08.09.括号
# 难度：MEDIUM
# 最后提交：2022-12-11 19:48:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def p(l, r, s):
            if l > r or l < 0 or r < 0:
                return
            if l == r == 0:
                ans.append(s)
            p(l-1, r, s+"(")
            p(l, r-1, s+")")
        p(n, n, "")
        return ans