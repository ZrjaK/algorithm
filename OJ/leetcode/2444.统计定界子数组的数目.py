# 题目：2444.统计定界子数组的数目
# 难度：HARD
# 最后提交：2022-10-16 12:04:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        ans = l = 0
        pos1, pos2 = -1, -1
        for r in range(n):
            if nums[r] == minK:
                pos1 = r
            if nums[r] == maxK:
                pos2 = r
            if nums[r] < minK or nums[r] > maxK:
                l = r + 1
            ans += max(0, min(pos1, pos2) - l + 1)

        return ans