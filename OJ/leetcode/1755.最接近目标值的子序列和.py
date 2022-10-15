# 题目：1755.最接近目标值的子序列和
# 难度：HARD
# 最后提交：2022-10-11 12:52:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        m = n>>1
        ans = 1e99
        a = [0] * (1<<m)
        for i in range(m):
            a[1<<i] = nums[i]
        for i in range(1<<m):
            f = i & -i
            a[i] = a[i ^ f] + a[f]
        b = [0] * (1<<n-m)
        for i in range(n-m):
            b[1<<i] = nums[i+m]
        for i in range(1<<n-m):
            f = i & -i
            b[i] = b[i ^ f] + b[f]
        a = sorted(list(set(a)))
        b = set(b)
        for f in b:
            t = bisect_left(a, goal-f)
            if t < len(a):
                ans = min(ans, abs(goal-f-a[t]))
            if t > 0:
                ans = min(ans, abs(goal-f-a[t-1]))
        return ans