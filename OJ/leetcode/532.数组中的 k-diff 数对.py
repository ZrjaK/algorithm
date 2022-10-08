# 题目：532.数组中的 k-diff 数对
# 难度：MEDIUM
# 最后提交：2022-05-01 20:00:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len([1 for i in Counter(nums).values() if i>1])
        nums = list(set(nums))
        nums.sort()
        ans = 0
        for i in nums:
            t = bisect_left(nums, i+k)
            ans += 1 if 0<=t<len(nums) and nums[t]==i+k else 0
        return ans