# 题目：137.只出现一次的数字 II
# 难度：MEDIUM
# 最后提交：2022-08-24 23:54:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for i, j in d.items():
            if j == 1:
                return i