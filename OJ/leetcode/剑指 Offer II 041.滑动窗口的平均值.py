# 题目：剑指 Offer II 041.滑动窗口的平均值
# 难度：EASY
# 最后提交：2022-10-06 21:21:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.s = 0
        self.size = size

    def next(self, val: int) -> float:
        self.s += val
        self.q.append(val)
        if len(self.q) > self.size:
            self.s -= self.q.popleft()
        return self.s / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)