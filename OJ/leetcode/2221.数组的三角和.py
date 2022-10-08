# 题目：2221.数组的三角和
# 难度：MEDIUM
# 最后提交：2022-04-02 22:40:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                nums[j] = (nums[j] + nums[j+1]) % 10
        return nums[0]