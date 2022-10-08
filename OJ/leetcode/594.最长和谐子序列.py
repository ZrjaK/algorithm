# 题目：594.最长和谐子序列
# 难度：EASY
# 最后提交：2021-10-23 00:32:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        r = []
        a = {}
        for i in nums:
            a[i] = a.get(i,0) + 1
        for i in a:
            if i+1 in a:
                r.append(a[i] + a[i+1])
        if r == []:
            return 0
        return max(r)