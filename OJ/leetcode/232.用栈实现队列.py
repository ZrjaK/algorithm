# 题目：232.用栈实现队列
# 难度：EASY
# 最后提交：2022-09-05 15:52:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MyQueue:

    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def push(self, x: int) -> None:
        self.pushStack.append(x)

    def pop(self) -> int:
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack.pop()
            

    def peek(self) -> int:
        if self.popStack:
            return self.popStack[-1]
        return self.pushStack[0]

    def empty(self) -> bool:
        return not self.pushStack and not self.popStack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()