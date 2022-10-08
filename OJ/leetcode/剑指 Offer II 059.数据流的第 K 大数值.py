# 题目：剑指 Offer II 059.数据流的第 K 大数值
# 难度：EASY
# 最后提交：2022-10-08 11:54:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        insort(self.nums, val)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)