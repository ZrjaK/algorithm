# 题目：2172.数组的最大与和
# 难度：HARD
# 最后提交：2022-10-14 12:30:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        @cache
        def p(i, mask):
            if i == n:
                return 0
            res = 0
            for j in range(1, numSlots+1):
                if mask // 3**j % 3 < 2:
                    res = max(res, (nums[i] & j) + p(i+1, mask + 3**j))
            return res
        return p(0, 0)