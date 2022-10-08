# 题目：225.用队列实现栈
# 难度：EASY
# 最后提交：2022-03-21 03:55:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if self.queue1:
            self.queue1.append(x)
        elif self.queue2:
            self.queue2.append(x)
        else:
            self.queue1.append(x)

    def pop(self) -> int:
        if self.queue1:
            while(not len(self.queue1) == 1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        if self.queue2:
            while(not len(self.queue2) == 1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)
        return None

    def top(self) -> int:
        if self.queue1:
            while(not len(self.queue1) == 1):
                self.queue2.append(self.queue1.pop(0))
            t = self.queue1.pop(0)
            self.queue2.append(t)
            return t
        if self.queue2:
            while(not len(self.queue2) == 1):
                self.queue1.append(self.queue2.pop(0))
            t = self.queue2.pop(0)
            self.queue1.append(t)
            return t
        return None

    def empty(self) -> bool:
        if self.queue1 or self.queue2:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()