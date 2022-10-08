# 题目：1003.检查替换后的词是否有效
# 难度：MEDIUM
# 最后提交：2022-09-03 13:19:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "c" and len(stack) >= 2 and stack[-2] == "a" and stack[-1] == "b":
                stack.pop()
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0