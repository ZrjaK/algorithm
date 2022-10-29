# 题目：862.和至少为 K 的最短子数组
# 难度：HARD
# 最后提交：2022-10-26 00:08:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = list(accumulate(nums)) + [0]
        q = deque([-1])
        ans = 1e99
        for i in range(n):
            while q and h[i] - h[q[0]] >= k:
                ans = min(ans, i-q.popleft())
            while q and h[q[-1]] >= h[i]:
                q.pop()
            q.append(i)
        return ans if ans < 1e90 else -1