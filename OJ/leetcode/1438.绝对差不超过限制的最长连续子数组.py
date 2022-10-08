# 题目：1438.绝对差不超过限制的最长连续子数组
# 难度：MEDIUM
# 最后提交：2022-05-24 09:33:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        maxq = deque()
        minq = deque()
        l = 0
        for i in range(n):
            while maxq and nums[i] >= nums[maxq[-1]]:
                maxq.pop()
            maxq.append(i)
            while minq and nums[i] <= nums[minq[-1]]:
                minq.pop()
            minq.append(i)
            t = nums[maxq[0]] - nums[minq[0]]
            if t > limit:
                if l == maxq[0]:
                    maxq.popleft()
                if l == minq[0]:
                    minq.popleft()
                l += 1
        return n-l