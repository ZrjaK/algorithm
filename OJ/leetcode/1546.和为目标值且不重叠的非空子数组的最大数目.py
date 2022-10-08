# 题目：1546.和为目标值且不重叠的非空子数组的最大数目
# 难度：MEDIUM
# 最后提交：2022-09-07 10:40:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        v = set([0])
        s = 0
        ans = 0
        for i in nums:
            s += i
            if s - target in v:
                ans += 1
                v = set([0])
                s = 0
            else:
                v.add(s)
        return ans