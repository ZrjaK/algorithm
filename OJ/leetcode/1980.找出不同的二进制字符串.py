# 题目：1980.找出不同的二进制字符串
# 难度：MEDIUM
# 最后提交：2022-09-14 13:46:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        v = set([int(i, 2) for i in nums])
        for i in range(1<<len(nums[0])):
            if i not in v:
                t = bin(i)[2:]
                return "0" * (len(nums[0])-len(t)) + t