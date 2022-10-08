# 题目：1863.找出所有子集的异或总和再求和
# 难度：EASY
# 最后提交：2022-08-26 21:27:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        l = [0]
        for i in nums:
            t = len(l)
            for j in range(t):
                l.append(l[j] ^ i)
        return sum(l)