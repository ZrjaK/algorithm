# 题目：1.两数之和
# 难度：EASY
# 最后提交：2022-09-03 01:53:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []