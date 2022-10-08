# 题目：622.设计循环队列
# 难度：MEDIUM
# 最后提交：2022-04-19 06:35:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.count = 0
        self.maxsize = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.maxsize:
            return False
        self.queue[(self.head+self.count)%self.maxsize] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if not self.count:
            return False
        self.head = (self.head + 1) % self.maxsize
        self.count -= 1
        return True

    def Front(self) -> int:
        return self.queue[self.head] if self.count else -1

    def Rear(self) -> int:
        return self.queue[(self.head+self.count-1)%self.maxsize] if self.count else -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.maxsize

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()