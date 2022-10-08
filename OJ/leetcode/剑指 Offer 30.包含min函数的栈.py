# 题目：剑指 Offer 30.包含min函数的栈
# 难度：EASY
# 最后提交：2022-10-02 22:33:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        if not self.s2:
            self.s2.append(x)
            return
        if x < self.s2[-1]:
            self.s2.append(x)
        else:
            self.s2.append(self.s2[-1])

    def pop(self) -> None:
        self.s1.pop()
        self.s2.pop()

    def top(self) -> int:
        return self.s1[-1]

    def min(self) -> int:
        return self.s2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()