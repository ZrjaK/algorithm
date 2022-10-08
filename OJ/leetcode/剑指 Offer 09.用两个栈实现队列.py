# 题目：剑指 Offer 09.用两个栈实现队列
# 难度：EASY
# 最后提交：2022-09-30 11:10:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class CQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value: int) -> None:
        self.s1.append(value)

    def deleteHead(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return -1
        return self.s2.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()