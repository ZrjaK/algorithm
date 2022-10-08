# 题目：1512.好数对的数目
# 难度：EASY
# 最后提交：2021-10-19 23:39:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count