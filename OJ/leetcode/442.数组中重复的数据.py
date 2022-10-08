# 题目：442.数组中重复的数据
# 难度：MEDIUM
# 最后提交：2022-05-08 00:06:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] -= 1
        res = set()
        for i in range(n):
            if i == nums[i]:
                continue
            while i != nums[i]:
                if nums[nums[i]] == nums[i]:
                    res.add(nums[i]+1)
                    break
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return list(res)