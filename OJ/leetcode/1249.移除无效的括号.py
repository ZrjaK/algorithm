# 题目：1249.移除无效的括号
# 难度：MEDIUM
# 最后提交：2022-09-04 18:23:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        v = set(stack)
        return "".join(s[i] for i in range(n) if i not in v)