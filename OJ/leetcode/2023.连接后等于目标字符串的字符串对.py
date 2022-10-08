# 题目：2023.连接后等于目标字符串的字符串对
# 难度：MEDIUM
# 最后提交：2022-04-06 11:22:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        return [i!=j and nums[i]+nums[j]==target for j in range(len(nums)) for i in range(len(nums))].count(True)