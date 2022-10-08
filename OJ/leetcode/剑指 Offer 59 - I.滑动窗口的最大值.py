# 题目：剑指 Offer 59 - I.滑动窗口的最大值
# 难度：HARD
# 最后提交：2022-10-03 20:37:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i-k == q[0]:
                q.popleft()
            ans.append(nums[q[0]])
        return ans