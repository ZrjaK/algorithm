# 题目：2552.统计上升四元组
# 难度：HARD
# 最后提交：2023-01-29 17:04:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cnt = [0] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    ans += cnt[j]
            c = 0
            for j in range(i):
                if nums[i] < nums[j]:
                    cnt[j] += c
                if nums[i] > nums[j]:
                    c += 1
        return ans