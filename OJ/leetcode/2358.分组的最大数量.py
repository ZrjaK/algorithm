# 题目：2358.分组的最大数量
# 难度：MEDIUM
# 最后提交：2022-07-31 10:42:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        ans = len(grades)
        while ans * (ans+1) // 2 > n:
            ans -= 1
        return ans