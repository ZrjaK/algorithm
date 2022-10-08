# 题目：747.至少是其他数字两倍的最大数
# 难度：EASY
# 最后提交：2021-10-24 11:35:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxnum = max(nums)
        index = nums.index(maxnum)
        nums.remove(maxnum)
        maxnum_sec = max(nums)
        if maxnum >= maxnum_sec * 2:
            return index
        return -1