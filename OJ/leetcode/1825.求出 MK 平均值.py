# 题目：1825.求出 MK 平均值
# 难度：HARD
# 最后提交：2023-01-18 00:21:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.s = SortedList()
        self.a = deque()
        self.m = m
        self.k = k
        self.sum = 0

    def addElement(self, num: int) -> None:
        self.a.append(num)
        m, k = self.m, self.k
        if len(self.a) > m:
            t = self.s.bisect_left(num)
            if t < k:
                self.sum += self.s[k-1]
                self.sum -= self.s[m-k-1]
            elif k <= t < m-k:
                self.sum += num
                self.sum -= self.s[m-k-1]
            self.s.add(num)

            v = self.a.popleft()
            t = self.s.bisect_left(v)
            if t < k:
                self.sum -= self.s[k]
                self.sum += self.s[m-k]
            elif k <= t < m-k:
                self.sum -= v
                self.sum += self.s[m-k]
            self.s.remove(v)
        elif len(self.a) == m:
            self.s = SortedList([i for i in self.a])
            self.sum = sum(self.s[k:m-k])



    def calculateMKAverage(self) -> int:
        m, k = self.m, self.k
        if len(self.a) < m:
            return -1
        return self.sum // (m-2*k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()