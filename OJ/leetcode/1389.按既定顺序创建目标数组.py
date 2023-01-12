# 题目：1389.按既定顺序创建目标数组
# 难度：EASY
# 最后提交：2023-01-06 13:14:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i, j in zip(nums, index):
            ans.insert(j, i)
        return ans