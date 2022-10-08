# 题目：35.搜索插入位置
# 难度：EASY
# 最后提交：2021-10-20 17:09:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i >= target:
                return nums.index(i)
        return len(nums)