# 题目：2367.算术三元组的数目
# 难度：EASY
# 最后提交：2022-08-07 10:31:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[j]-nums[i] == nums[k]-nums[j] ==diff:
                        ans += 1
        return ans