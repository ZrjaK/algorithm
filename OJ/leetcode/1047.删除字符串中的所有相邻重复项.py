# 题目：1047.删除字符串中的所有相邻重复项
# 难度：EASY
# 最后提交：2021-11-06 14:06:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)