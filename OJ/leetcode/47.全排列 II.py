# 题目：47.全排列 II
# 难度：MEDIUM
# 最后提交：2022-09-14 10:48:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l = list(permutations(nums))
        s = set()
        for i in l:
            s.add(tuple(i))
        return list(s)