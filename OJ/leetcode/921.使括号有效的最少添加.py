# 题目：921.使括号有效的最少添加
# 难度：MEDIUM
# 最后提交：2022-10-04 00:00:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in s:
            if i == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
        return len(stack)