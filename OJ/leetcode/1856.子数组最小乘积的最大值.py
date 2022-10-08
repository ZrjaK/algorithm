# 题目：1856.子数组最小乘积的最大值
# 难度：MEDIUM
# 最后提交：2022-09-16 09:25:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        nums = [0] + nums + [0]
        n = len(nums)
        h = list(accumulate(nums)) + [0]
        left = list(range(n))
        right = list(range(n))
        stack = []
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                right[stack.pop()] = i
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]:
                left[stack.pop()] = i
            stack.append(i)
        ans = 0
        for i in range(n):
            ans = max(ans, nums[i] * (h[right[i]-1]-h[left[i]]))
        return ans % int(1e9+7)