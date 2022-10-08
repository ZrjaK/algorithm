# 题目：2369.检查数组是否存在有效划分
# 难度：MEDIUM
# 最后提交：2022-08-07 10:40:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def p(i):
            if i < 1:
                return False
            if i == 1:
                return nums[0] == nums[1]
            if i == 2:
                p1 = nums[0] == nums[1] == nums[2]
                p2 = nums[2] == nums[1] + 1 == nums[0] + 2
                return p1 or p2
            res = False
            if nums[i-1] == nums[i]:
                res |= p(i-2)
            if nums[i-2] == nums[i-1] == nums[i]:
                res |= p(i-3)
            if nums[i-2]+2 == nums[i-1]+1 == nums[i]:
                res |= p(i-3)
            return res
                
        return p(len(nums)-1)