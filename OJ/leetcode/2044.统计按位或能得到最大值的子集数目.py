# 题目：2044.统计按位或能得到最大值的子集数目
# 难度：MEDIUM
# 最后提交：2022-08-27 01:36:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        for i in nums:
            s |= i
        ans = 0
        for i in range(1<<n):
            t = 0
            for j in range(n):
                if 1<<j & i:
                    t |= nums[j]
            if t == s:
                ans += 1
        return ans