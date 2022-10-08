# 题目：394.字符串解码
# 难度：MEDIUM
# 最后提交：2022-09-02 13:18:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                st = ""
                while stack[-1] != '[':
                    st = stack.pop() + st
                stack.pop()
                
                num = ""
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num

                stack.append(int(num) * st)
        return "".join(stack)