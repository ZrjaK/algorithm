# 题目：260.只出现一次的数字 III
# 难度：MEDIUM
# 最后提交：2022-08-25 00:36:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = 0
        for i in nums:
            s ^= i
        t = s & -s
        k = 0
        for i in nums:
            if i & t:
                k ^= i
        return [k, s^k]