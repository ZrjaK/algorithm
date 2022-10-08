# 题目：1674.使数组互补的最少操作次数
# 难度：MEDIUM
# 最后提交：2022-09-28 21:39:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(n//2):
            t = nums[i] + nums[n-i-1]
            mi = 1 + min(nums[i], nums[n-i-1])
            ma = limit+max(nums[i], nums[n-i-1]) + 1
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            diff[mi] += -1
            diff[ma] -= -1

            diff[t] += -1
            diff[t + 1] -= -1
        ans = n
        s = 0
        for i in diff[2:2*limit+1]:
            s += i
            ans = min(ans, s)
        return ans