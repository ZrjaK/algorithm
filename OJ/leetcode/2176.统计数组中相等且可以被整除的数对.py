# 题目：2176.统计数组中相等且可以被整除的数对
# 难度：EASY
# 最后提交：2022-04-11 18:15:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i*j % k == 0:
                    ans += 1
        return ans