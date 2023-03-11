# 题目：2568.最小无法得到的或值
# 难度：MEDIUM
# 最后提交：2023-02-18 23:38:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        for i in range(31):
            if 1 << i not in nums:
                return 1 << i
        