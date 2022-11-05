# 题目：1106.解析布尔表达式
# 难度：HARD
# 最后提交：2022-11-05 13:55:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c == ',':
                continue
            if c != ')':
                stk.append(c)
                continue
            t = f = 0
            while stk[-1] != '(':
                if stk.pop() == 't':
                    t += 1
                else:
                    f += 1
            stk.pop()
            op = stk.pop()
            if op == '!':
                stk.append('t' if f == 1 else 'f')
            elif op == '&':
                stk.append('t' if f == 0 else 'f')
            elif op == '|':
                stk.append('t' if t else 'f')
        return stk[-1] == 't'