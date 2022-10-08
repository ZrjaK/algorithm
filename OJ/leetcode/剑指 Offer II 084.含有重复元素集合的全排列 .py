# 题目：剑指 Offer II 084.含有重复元素集合的全排列 
# 难度：MEDIUM
# 最后提交：2022-10-08 14:58:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(tuple(i) for i in permutations(nums)))