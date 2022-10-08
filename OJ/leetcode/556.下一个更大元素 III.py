# 题目：556.下一个更大元素 III
# 难度：MEDIUM
# 最后提交：2022-06-03 09:38:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [int(i) for i in str(n)]
        if sorted(nums) == nums[::-1]:
            return -1
        m = len(nums)
        for i in range(m-1, 0, -1):
            if nums[i-1] < nums[i]:
                for j in range(m-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        nums[i:] = sorted(nums[i:])
                        break
                break
        ans = 0
        for i in nums:
            ans = ans * 10 + i
        return ans if ans < 2**31 else -1