# 题目：31.下一个排列
# 难度：MEDIUM
# 最后提交：2022-05-26 10:35:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        t1 = t2 = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                t1 = i
                break
        if t1 == -1:
            l, r = 0, n-1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return
        for i in range(n-1, i, -1):
            if nums[i] > nums[t1]:
                t2 = i
                break
        nums[t1], nums[t2] = nums[t2], nums[t1]
        for i in range(t1+1, n):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        