# 题目：795.区间子数组个数
# 难度：MEDIUM
# 最后提交：2022-06-04 18:03:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def p(m):
            res = 0
            t = 0
            for i in nums:
                if i <= m:
                    t += 1
                    res += t
                else:
                    t = 0
            return res
        return p(right) - p(left-1)
