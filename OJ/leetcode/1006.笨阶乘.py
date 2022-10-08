# 题目：1006.笨阶乘
# 难度：MEDIUM
# 最后提交：2022-09-03 13:27:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def clumsy(self, n: int) -> int:
        l = ["*", "/", "+", "-"]
        d = {"*": lambda x, y: x * y,
                "/": lambda x, y: x // y,
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y}
        stack = []
        k = 0
        for i in range(n, 0, -1):
            if stack and stack[-1] in ["*", "/"]:
                stack.append(d[stack.pop()](stack.pop(), i))
            else:
                stack.append(i)
            stack.append(l[k%4])
            k += 1
        stack.pop()
        ans = stack[0]
        for i in range(1, len(stack), 2):
            ans = d[stack[i]](ans, stack[i+1])
        return ans