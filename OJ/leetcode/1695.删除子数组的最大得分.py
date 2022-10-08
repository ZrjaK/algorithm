# 题目：1695.删除子数组的最大得分
# 难度：MEDIUM
# 最后提交：2022-05-24 13:47:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = defaultdict(int)
        l = 0
        s = 0
        ans = 0
        for r in range(len(nums)):
            s += nums[r]
            if nums[r] in d:
                while l <= d[nums[r]]:
                    s -= nums[l]
                    l += 1
            d[nums[r]] = r
            ans = max(ans, s)
        return ans