# 题目：462.最小操作次数使数组元素相等 II
# 难度：MEDIUM
# 最后提交：2022-05-19 09:41:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        i, j, ans = 0, len(nums)-1, 0
        while i < j:
            ans += nums[j] - nums[i]
            j -= 1
            i += 1
        return ans