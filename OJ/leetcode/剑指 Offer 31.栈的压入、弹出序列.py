# 题目：剑指 Offer 31.栈的压入、弹出序列
# 难度：MEDIUM
# 最后提交：2022-10-02 22:36:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped = popped[::-1]
        stack = []
        for i in pushed:
            stack.append(i)
            while popped and stack and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
        return len(popped) == 0