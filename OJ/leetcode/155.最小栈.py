# 题目：155.最小栈
# 难度：MEDIUM
# 最后提交：2022-09-01 19:26:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MinStack:

    def __init__(self):
        self.m = [1e99]
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.m.append(min(self.m[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.m.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()