# 题目：331.验证二叉树的前序序列化
# 难度：MEDIUM
# 最后提交：2022-09-02 03:08:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        s = preorder.split(",")
        stack = []
        for i in s:
            stack.append(i)
            while len(stack) >= 3 and stack[-1] == stack[-2] == "#" and stack[-3] != "#":
                stack = stack[:-3] + ["#"]
        return len(stack) == 1 and stack[0] == "#"
