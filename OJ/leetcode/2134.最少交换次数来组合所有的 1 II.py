# 题目：2134.最少交换次数来组合所有的 1 II
# 难度：MEDIUM
# 最后提交：2022-05-25 22:29:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        nums *= 2
        l = r = c = 0
        while r < k:
            if not nums[r]:
                c += 1
            r += 1
        ans = c
        for r in range(k, len(nums)):
            if not nums[r]:
                c += 1
            if not nums[l]:
                c -= 1
            l += 1
            ans = min(ans, c)
        return ans