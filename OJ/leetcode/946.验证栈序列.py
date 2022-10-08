# 题目：946.验证栈序列
# 难度：MEDIUM
# 最后提交：2022-09-02 21:29:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped = popped[::-1]
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and popped and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
        return len(popped) == 0