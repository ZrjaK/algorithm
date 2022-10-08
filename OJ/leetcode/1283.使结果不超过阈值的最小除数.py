# 题目：1283.使结果不超过阈值的最小除数
# 难度：MEDIUM
# 最后提交：2022-05-01 14:38:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            mid = l+r>>1
            t = 0
            for i in nums:
                t += i // mid
                if i % mid != 0:
                    t += 1
            if t <= threshold:
                r = mid - 1
            else:
                l = mid + 1
        return l