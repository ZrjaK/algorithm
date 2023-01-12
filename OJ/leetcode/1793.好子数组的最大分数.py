# 题目：1793.好子数组的最大分数
# 难度：HARD
# 最后提交：2022-12-14 17:01:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [0] * n
        right = [n-1] * n
        q = []
        for i in range(n):
            while q and nums[q[-1]] > nums[i]:
                right[q.pop()] = i-1
            q.append(i)
        for i in range(n-1, -1, -1):
            while q and nums[q[-1]] > nums[i]:
                left[q.pop()] = i+1
            q.append(i)
        ans = 0
        for i in range(n):
            if left[i] <= k <= right[i]:
                ans = max(ans, nums[i] * (right[i] - left[i] + 1))
        return ans