# 题目：剑指 Offer 56 - I.数组中数字出现的次数
# 难度：MEDIUM
# 最后提交：2022-10-03 20:18:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        t = 0
        for i in nums:
            t ^= i
        c = t & -t
        f = 0
        for i in nums:
            if i & c:
                f ^= i
        return [f, t ^ f]