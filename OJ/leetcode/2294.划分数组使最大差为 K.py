# 题目：2294.划分数组使最大差为 K
# 难度：MEDIUM
# 最后提交：2022-06-05 10:36:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        i = 0
        while i < len(nums):
            t = bisect_right(nums, nums[i] + k)
            i = t
            ans += 1
        return ans