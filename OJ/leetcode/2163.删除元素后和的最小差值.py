# 题目：2163.删除元素后和的最小差值
# 难度：HARD
# 最后提交：2022-09-26 13:30:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        pq = [-i for i in nums[:n]]
        heapify(pq)
        s = -sum(pq)
        sl = [s] * (n*3)
        for i in range(n, n*2):
            s += nums[i] + heappushpop(pq, -nums[i])
            sl[i] = s
        pq = nums[-n:]
        heapify(pq)
        s = sum(pq)
        sr = [s] * (n*3)
        for i in range(n*2-1, n-1, -1):
            s += nums[i] - heappushpop(pq, nums[i])
            sr[i] = s
        ans = 1e99
        for i in range(n-1, n*2):
            ans = min(ans, sl[i]-sr[i+1])
        return ans