# 题目：910.最小差值 II
# 难度：MEDIUM
# 最后提交：2022-08-29 16:34:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]
        a, b = nums[0]+k, nums[-1]-k
        for i in range(n-1):
            ans = min(ans, max(b, nums[i]+k) - min(a, nums[i+1]-k))
        return ans