# 题目：856.括号的分数
# 难度：MEDIUM
# 最后提交：2022-09-02 14:09:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        cnt = 0
        for i, c in enumerate(s):
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
                if s[i-1] == '(': 
                    res += 1 << cnt
        return res