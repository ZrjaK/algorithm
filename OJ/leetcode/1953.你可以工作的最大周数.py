# 题目：1953.你可以工作的最大周数
# 难度：MEDIUM
# 最后提交：2022-05-16 16:26:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        s = sum(milestones)
        k = max(milestones)
        if k > s-k:
            return (s-k)*2+1
        return s