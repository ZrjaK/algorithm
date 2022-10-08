# 题目：面试题 17.19.消失的两个数字
# 难度：HARD
# 最后提交：2022-09-26 08:11:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        nums = [0] + nums + [0]
        n = len(nums)
        for i in range(n):
            nums[i] -= 1
        for _ in range(20):
            for i in range(n):
                if nums[i] != i and 0 <= nums[i] < n:
                    t = nums[i]
                    # if nums[t] != t:
                    nums[t], nums[i] = nums[i], nums[t]
        ans = []
        for i in range(n):
            if nums[i] != i:
                ans.append(i+1)
        # print(nums)
        return ans