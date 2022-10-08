# 题目：150.逆波兰表达式求值
# 难度：MEDIUM
# 最后提交：2022-09-01 18:29:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d = {"+": lambda x, y: x + y, 
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
                "/": lambda x, y: int(x/y)}
        stack = []
        for i in tokens:
            if i in d:
                b = stack.pop()
                a = stack.pop()
                stack.append(d[i](a, b))
            else:
                stack.append(int(i))
        return stack.pop()