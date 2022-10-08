# 题目：2336.无限集中的最小数字
# 难度：MEDIUM
# 最后提交：2022-07-10 10:37:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class SmallestInfiniteSet:

    def __init__(self):
        self.s = set([i for i in range(1, 1001)])
        self.m = min(self.s)

    def popSmallest(self) -> int:
        res = self.m
        self.s.remove(self.m)
        if self.s:
            self.m = min(self.s)
        return res

    def addBack(self, num: int) -> None:
        self.s.add(num)
        if num < self.m:
            self.m = num


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)