# 题目：295.数据流的中位数
# 难度：HARD
# 最后提交：2022-10-03 11:25:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        from sortedcontainers import SortedList
        self.s = SortedList()


    def addNum(self, num: int) -> None:
        self.s.add(num)

    def findMedian(self) -> float:
        n = len(self.s)
        if n % 2:
            return self.s[n//2]
        return (self.s[n//2-1] + self.s[n//2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()