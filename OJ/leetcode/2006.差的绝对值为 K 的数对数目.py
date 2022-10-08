# 题目：2006.差的绝对值为 K 的数对数目
# 难度：EASY
# 最后提交：2022-04-22 19:17:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        return sum(nums.count(i+k) for i in nums)