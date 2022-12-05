# 题目：1752.检查数组是否经排序和轮转得到
# 难度：EASY
# 最后提交：2022-11-27 01:38:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        a = sorted(nums)
        for i in range(n):
            if a == nums[i:] + nums[:i]:
                return True
        return False