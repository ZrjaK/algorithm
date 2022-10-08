# 题目：1313.解压缩编码列表
# 难度：EASY
# 最后提交：2022-04-03 01:00:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            for _ in range(nums[i]):
                res.append(nums[i+1])
            i+=2
        return res