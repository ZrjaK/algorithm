# 题目：1760.袋子里最少数目的球
# 难度：MEDIUM
# 最后提交：2022-12-20 00:50:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        a = sum(nums)
        l,r=max(1, a//(len(nums)+maxOperations)), a//maxOperations
        while l <= r:
            mid = l+r>>1
            t = 0
            for i in nums:
                t += i//mid
                t -= 1 if i % mid == 0 else 0
            if t <= maxOperations:
                r = mid - 1
            else:
                l = mid + 1
        return l