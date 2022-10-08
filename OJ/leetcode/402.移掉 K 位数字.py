# 题目：402.移掉 K 位数字
# 难度：MEDIUM
# 最后提交：2022-09-02 13:24:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and k and stack[-1] > int(i):
                stack.pop()
                k -= 1
            stack.append(int(i))
        while stack and k:
            stack.pop()
            k -= 1
        if not stack:
            return "0"
        return str(int("".join(str(i) for i in stack)))