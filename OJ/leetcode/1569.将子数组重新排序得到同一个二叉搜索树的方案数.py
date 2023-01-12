# 题目：1569.将子数组重新排序得到同一个二叉搜索树的方案数
# 难度：HARD
# 最后提交：2022-09-27 16:27:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def p(nums):
            if len(nums) < 3:
                return 1
            left = [num for num in nums if num < nums[0]]
            right = [num for num in nums if num > nums[0]]
            return comb(len(nums) - 1, len(left)) * p(left) * p(right)
        return (p(nums) - 1) % int(1e9+7)