# 题目：303.区域和检索 - 数组不可变
# 难度：EASY
# 最后提交：2021-10-21 17:48:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)