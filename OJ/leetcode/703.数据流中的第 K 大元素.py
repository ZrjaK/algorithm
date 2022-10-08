# 题目：703.数据流中的第 K 大元素
# 难度：EASY
# 最后提交：2021-10-23 20:48:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums


    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)