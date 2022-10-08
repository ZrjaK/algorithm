# 题目：剑指 Offer 57 - II.和为s的连续正数序列
# 难度：EASY
# 最后提交：2022-10-03 20:31:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l, r = 1, 1
        s = 0
        ans = []
        while r <= target//2+1:
            s += r
            while l + 1 < r and s > target:
                s -= l
                l += 1
            if s == target:
                ans.append(list(range(l,r+1)))
            r += 1
        return ans