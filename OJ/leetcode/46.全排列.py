# 题目：46.全排列
# 难度：MEDIUM
# 最后提交：2022-09-14 10:47:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))