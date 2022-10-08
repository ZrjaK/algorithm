# 题目：2239.找到最接近 0 的数字
# 难度：EASY
# 最后提交：2022-04-16 22:33:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = 1e99
        for i in nums:
            if abs(i) < abs(ans):
                ans = i
            if abs(i) == abs(ans) and i > ans:
                ans = i
        return ans