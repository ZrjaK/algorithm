# 题目：2349.设计数字容器系统
# 难度：MEDIUM
# 最后提交：2022-07-23 22:56:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.d = defaultdict(SortedList)
        self.arr = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        self.d[self.arr[index]].discard(index)
        self.d[number].add(index)
        self.arr[index] = number
        

    def find(self, number: int) -> int:
        if self.d[number]:
            return self.d[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)