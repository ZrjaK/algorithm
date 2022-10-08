# 题目：908.最小差值 I
# 难度：EASY
# 最后提交：2021-11-01 22:47:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - k * 2)