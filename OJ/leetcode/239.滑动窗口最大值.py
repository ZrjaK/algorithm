# 题目：239.滑动窗口最大值
# 难度：HARD
# 最后提交：2022-04-13 10:06:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        n = len(nums)
        for i in range(min(n,k)):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        res = []
        for i in range(k, n):
            res.append(nums[queue[0]])
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if queue[0] == i-k:
                queue.popleft()
        res.append(nums[queue[0]])
        return res
