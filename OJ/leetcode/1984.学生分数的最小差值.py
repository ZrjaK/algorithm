# 题目：1984.学生分数的最小差值
# 难度：EASY
# 最后提交：2022-10-21 17:00:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1e99
        for i in range(len(nums)-k+1):
            ans = min(ans, nums[i+k-1]-nums[i])
        return ans