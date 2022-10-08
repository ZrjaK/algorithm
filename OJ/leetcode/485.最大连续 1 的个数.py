# 题目：485.最大连续 1 的个数
# 难度：EASY
# 最后提交：2021-10-22 13:12:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
         return max(len (substr) for substr in ''.join([str(x) for x in nums]).split("0"))
        