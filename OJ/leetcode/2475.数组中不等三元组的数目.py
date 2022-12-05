# 题目：2475.数组中不等三元组的数目
# 难度：EASY
# 最后提交：2022-11-20 10:31:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        ans += 1
        return ans