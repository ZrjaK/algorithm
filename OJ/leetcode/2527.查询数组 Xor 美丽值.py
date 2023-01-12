# 题目：2527.查询数组 Xor 美丽值
# 难度：MEDIUM
# 最后提交：2023-01-07 22:35:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(xor, nums)