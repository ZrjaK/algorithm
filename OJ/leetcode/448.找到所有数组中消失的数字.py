# 题目：448.找到所有数组中消失的数字
# 难度：EASY
# 最后提交：2021-10-22 00:23:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num)-1])
        print(nums)
        return [i+1 for i,num in enumerate(nums) if num>0]
