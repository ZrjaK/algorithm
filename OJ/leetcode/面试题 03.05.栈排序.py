# 题目：面试题 03.05.栈排序
# 难度：MEDIUM
# 最后提交：2022-10-18 16:52:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class SortedStack:

    def __init__(self):
        self.s = []
        self.t = []


    def push(self, val: int) -> None:
        while self.s and self.s[-1] < val:
            self.t.append(self.s.pop())
        self.s.append(val)
        while self.t:
            self.s.append(self.t.pop())

    def pop(self) -> None:
        if self.s:
            self.s.pop()


    def peek(self) -> int:
        if self.s:
            return self.s[-1]
        return -1


    def isEmpty(self) -> bool:
        return len(self.s) == 0


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()