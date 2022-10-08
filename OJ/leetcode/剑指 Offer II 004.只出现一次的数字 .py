# 题目：剑指 Offer II 004.只出现一次的数字 
# 难度：MEDIUM
# 最后提交：2022-10-04 00:47:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i in c:
            if c[i] == 1:
                return i